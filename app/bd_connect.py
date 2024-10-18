import mysql.connector
from mysql.connector import Error


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",  # Hôte
            user="root",       # Utilisateur MySQL
            password="",       # Mot de passe
            database="password_secure"  # Base de données
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Erreur lors de la connexion:", e)
        return None
