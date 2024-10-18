from .train_model import run_model  # Importation de la fonction run_model depuis le fichier train_model
from .extract_features import extract_features  # Importation de la fonction extract_features depuis le fichier extract_features
from .password_generator import generate_secure_password
import pandas as pd  # Importation de la bibliothèque pandas pour la manipulation de données



# Fonction pour charger les mots de passe à tester
def load_test_passwords(file_path='passwords_no_categories.txt'):
    """Charge les mots de passe à partir d'un fichier texte."""
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    return [pwd.strip() for pwd in passwords]  # Nettoyer les espaces

# Fonction pour tester le modèle sur des mots de passe
def test_model_on_passwords(model, passwords):
    """Teste le modèle sur une liste de mots de passe."""
    for password in passwords:
        features = pd.DataFrame([extract_features(password)])  # Extraction des caractéristiques
        prediction = model.predict(features)  # Prédiction avec le modèle
        print(f"Le mot de passe '{password}' est classé comme : {prediction[0]}")  # Affichage de la prédiction

def main():
    # Fonction principale pour exécuter le modèle KNN et tester un nouveau mot de passe
    model = run_model()  # Exécution de la fonction run_model pour obtenir le modèle KNN

    # Tester avec un nouveau mot de passe
    nouveau_mot_de_passe = 'AZER'  # Définition d'un nouveau mot de passe à tester
    caracteristiques_nouveau = pd.DataFrame([extract_features(nouveau_mot_de_passe)])  # Extraction des caractéristiques du mot de passe et conversion en DataFrame
    prediction = model.predict(caracteristiques_nouveau)  # Prédiction du modèle sur les caractéristiques du nouveau mot de passe
    print(f"Le mot de passe '{nouveau_mot_de_passe}' est classé comme : {prediction[0]}")  # Affichage de la classification du mot de passe

 #Générer un nouveau mot de passe sécurisé
    nouveau_mot_de_passe = generate_secure_password(length=12)  # Génération d'un mot de passe aléatoire
    print(f"Nouveau mot de passe généré : {nouveau_mot_de_passe}")  # Affichage du mot de passe généré

    # Extraction des caractéristiques du mot de passe et conversion en DataFrame
    caracteristiques_nouveau = pd.DataFrame([extract_features(nouveau_mot_de_passe)])
    prediction = model.predict(caracteristiques_nouveau)  # Prédiction du modèle sur les caractéristiques du nouveau mot de passe

    # Affichage de la classification du mot de passe

    print(f"Le mot de passe '{nouveau_mot_de_passe}' est classé comme : {prediction[0]}")
    # Charger les mots de passe à tester et les évaluer
    test_passwords = load_test_passwords('passwords_no_categories.txt')  # Charger les mots de passe
    if model:  # S'assurer que le modèle a été entraîné avec succès
        test_model_on_passwords(model, test_passwords)  # Teste le modèle sur les mots de passe


if __name__ == "__main__":
    main()  # Appel de la fonction principale si le fichier est exécuté directement
