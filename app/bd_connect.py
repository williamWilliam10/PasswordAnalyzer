import mysql.connector
from mysql.connector import Error
import os  # Importation pour lire les variables d'environnement


def get_db_connection():
    try:
        # Récupérer les variables d'environnement
        host = os.environ.get("MYSQL_HOST")  # Hôte MySQL
        user = os.environ.get("MYSQL_USER")  # Utilisateur MySQL
        password = os.environ.get("MYSQL_PASSWORD")  # Mot de passe MySQL
        database = os.environ.get("MYSQL_DATABASE")  # Base de données MySQL
        port = os.environ.get("MYSQL_PORT")  # Port MySQL

        # Vérifier que toutes les variables d'environnement sont définies
        if None in [host, user, password, database, port]:
            print("Erreur: Une ou plusieurs variables d'environnement ne sont pas définies.")
            return None

        # Conversion du port en entier
        port = int(port)

        # Connexion à la base de données
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )

        if connection.is_connected():
            return connection
    except Error as e:
        print("Erreur lors de la connexion:", e)
        return None
