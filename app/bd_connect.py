import mysql.connector
from mysql.connector import Error
import os

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST", "junction.proxy.rlwy.net"),  # Hôte par défaut
            port=int(os.environ.get("MYSQL_PORT", 10659)),  # Port par défaut
            user=os.environ.get("MYSQL_USER", "root"),  # Utilisateur MySQL par défaut
            password=os.environ.get("MYSQL_PASSWORD", "koNVTUXkFZcbxYpQUfxPvyWQdZJyFYrA"),  # Mot de passe MySQL par défaut
            database=os.environ.get("MYSQL_DATABASE", "railway")  # Nom de la base de données par défaut
        )
        if connection.is_connected():
            print("Connexion réussie à la base de données")
            return connection
    except Error as e:
        print("Erreur lors de la connexion à la base de données:", e)
        return None
