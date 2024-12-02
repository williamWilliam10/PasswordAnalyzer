from flask import Flask, request, jsonify
import pandas as pd
from .extract_features import extract_features
from .train_model import run_model
from flask_cors import CORS
from .password_generator import generate_secure_password
from .bd_connect import get_db_connection
from .encrypt_decrypt import encrypt_password
from .hash import hash_password
import mysql.connector
from .brute_force import brute_force_attack
from .dictionary_attack import dictionary_attack
import os
app = Flask(__name__)

# Configuration de CORS pour autoriser uniquement le domaine de votre frontend
CORS(app, resources={
    r"/*": {
        "origins": [
            "https://smartpass-production.up.railway.app",
            "https://smartpass.lowewilliam.com",
            "https://web-production-b62ae.up.railway.app"

        ]
    }
})

# Charger le modèle KNN
model = run_model()

@app.route('/verifier', methods=['POST'])
def verify_password():
    """Vérifie la force d'un mot de passe."""
    data = request.get_json()  # Récupérer les données JSON de la requête
    mot_de_passe = data.get('password')  # Récupérer le mot de passe

    if not mot_de_passe:
        return jsonify({'error': 'Aucun mot de passe fourni.'}), 400

    # Extraction des caractéristiques
    caracteristiques = pd.DataFrame([extract_features(mot_de_passe)])

    # Prédiction avec le modèle
    prediction = model.predict(caracteristiques)

    # Interpréter la prédiction
    resultats = {0: "faible", 1: "moyen", 2: "fort"}
    force_mot_de_passe = resultats[prediction[0]]

    return jsonify({'force': force_mot_de_passe})

@app.route('/generer', methods=['GET'])
def generate_password():
    """Génère un mot de passe sécurisé."""
    password = generate_secure_password()

    # Chiffrement du mot de passe
    encrypted_password, key, iv = encrypt_password(password)

    # Hachage pour la comparaison future
    hashed_password = hash_password(password)

    # Connexion à la base de données
    connection = get_db_connection()

    if not connection:
        return jsonify({'error': 'Erreur de connexion à la base de données'}), 500

    cursor = connection.cursor()

    try:
        # Sauvegarder encrypted_password, key, iv, et hashed_password dans la base de données
        sql = """
        INSERT INTO passwords_list (password_plain, encrypted_password, key_base64, iv_base64, hashed_password)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            password,
            encrypted_password.hex(),
            key.hex(),
            iv.hex(),
            hashed_password.decode()
        ))
        connection.commit()

    except mysql.connector.Error as err:
        print(f"Erreur MySQL: {err}")
        return jsonify({'error': 'Erreur lors de l\'enregistrement dans la base de données.'}), 500

    finally:
        cursor.close()
        connection.close()

    return jsonify({
        'password': password,
        'encrypted_password': encrypted_password.hex(),
        'key': key.hex(),
        'iv': iv.hex(),
        'hashed': hashed_password.decode()
    })

@app.route('/attacker/brute_force', methods=['POST'])
def attack_brute_force():
    """Teste la résistance d'un mot de passe avec une attaque brute-force."""
    data = request.get_json()
    hashed_password = data.get('hashed_password')

    if not hashed_password:
        return jsonify({'error': 'Aucun hachage de mot de passe fourni.'}), 400

    result = brute_force_attack(hashed_password)
    return jsonify(result)

@app.route('/attacker/dictionary', methods=['POST'])
def attack_dictionary():
    """Teste la résistance d'un mot de passe avec une attaque par dictionnaire."""
    data = request.get_json()
    hashed_password = data.get('hashed_password')
    dictionary_file = data.get('dictionary_file', 'dictionnaire.txt')  # Nom de fichier par défaut

    if not hashed_password:
        return jsonify({'error': 'Aucun hachage de mot de passe fourni.'}), 400

    result = dictionary_attack(hashed_password, dictionary_file)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)