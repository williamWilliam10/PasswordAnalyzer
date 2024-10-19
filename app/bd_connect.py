import mysql.connector
from mysql.connector import Error
import os  # Importation pour lire les variables d'environnement

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get("mysql.railway.internal"),          # Hôte MySQL fourni par Railway
            user=os.environ.get("root"),          # Utilisateur MySQL fourni par Railway
            password=os.environ.get("koNVTUXkFZcbxYpQUfxPvyWQdZJyFYrA"),  # Mot de passe MySQL fourni par Railway
            database=os.environ.get("railway"),  # Base de données MySQL
            port=os.environ.get("3306")           # Port MySQL fourni par Railway
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Erreur lors de la connexion:", e)
        return None
