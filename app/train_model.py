import pandas as pd
import time
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from .extract_features import extract_features


# Fonction pour charger et préparer les données
def load_data(
        test_file='weak_passwords.txt',
        medium_file='medium_passwords.txt',
        strong_file='strong_passwords.txt'):
    """
    Charge les mots de passe à partir des fichiers spécifiés et les étiquette.

    Args:
        test_file (str): Le nom du fichier contenant les mots de passe faibles.
        medium_file (str): Le nom du fichier contenant les mots de passe moyens.
        strong_file (str): Le nom du fichier contenant les mots de passe forts.

    Returns:
        pd.DataFrame: Un DataFrame contenant les mots de passe et leurs étiquettes.
    """
    # Obtenir le répertoire actuel du fichier
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construire les chemins complets vers les fichiers
    test_file_path = os.path.join(current_dir, test_file)
    medium_file_path = os.path.join(current_dir, medium_file)
    strong_file_path = os.path.join(current_dir, strong_file)

    try:
        # Chargement des mots de passe à partir des fichiers
        test_passwords = pd.read_csv(test_file_path, header=None, names=['password'], on_bad_lines='skip')
        medium_passwords = pd.read_csv(medium_file_path, header=None, names=['password'], on_bad_lines='skip')
        strong_passwords = pd.read_csv(strong_file_path, header=None, names=['password'], on_bad_lines='skip')
    except FileNotFoundError as e:
        print(f"Fichier non trouvé : {e}")
        return pd.DataFrame()  # Retourne un DataFrame vide en cas d'erreur
    except pd.errors.ParserError as e:
        print(f"Erreur lors de la lecture des fichiers : {e}")
        return pd.DataFrame()  # Retourne un DataFrame vide en cas d'erreur

    # Assignation des labels
    test_passwords['label'] = 0  # Faible
    medium_passwords['label'] = 1  # Moyen
    strong_passwords['label'] = 2  # Fort

    # Concaténation des données
    data = pd.concat([test_passwords, medium_passwords, strong_passwords], ignore_index=True)
    print(f"Total des mots de passe chargés : {len(data)}")  # Affiche le nombre total de mots de passe chargés

    return data


# Fonction pour extraire les caractéristiques et créer le jeu de données
def prepare_data(data):
    """
    Extrait les caractéristiques des mots de passe et crée les jeux de données X et y.

    Args:
        data (pd.DataFrame): Le DataFrame contenant les mots de passe et leurs étiquettes.

    Returns:
        tuple: Un tuple contenant le DataFrame des caractéristiques et les labels.
    """
    features = data['password'].apply(extract_features).tolist()  # Extraire les caractéristiques des mots de passe
    X = pd.DataFrame(features)  # Convertir en DataFrame
    y = data['label'].values  # Labels des mots de passe
    return X, y


# Fonction pour entraîner le modèle KNN
def train_knn(X_train, y_train):
    """
    Entraîne un modèle KNN sur les données fournies.

    Args:
        X_train (pd.DataFrame): Les caractéristiques d'entraînement.
        y_train (np.array): Les labels d'entraînement.

    Returns:
        KNeighborsClassifier: Le modèle KNN entraîné.
    """
    knn = KNeighborsClassifier(n_neighbors=3)  # Choix du nombre de voisins
    knn.fit(X_train, y_train)  # Entraînement du modèle
    return knn


def run_model():
    """
    Fonction principale pour exécuter le modèle : chargement des données, préparation, entraînement et évaluation.
    """
    start_time = time.time()

    # Charger les données
    data = load_data()

    # Vérifier si les données sont vides
    if data.empty:
        print("Aucune donnée à traiter. Vérifiez vos fichiers.")
        return None

    # Préparer les données
    X, y = prepare_data(data)

    # Séparation des données en ensemble d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Entraîner le modèle KNN
    model = train_knn(X_train, y_train)

    # Prédire sur l'ensemble de test
    y_pred = model.predict(X_test)

    # Évaluer la précision du modèle
    precision = accuracy_score(y_test, y_pred)
    print(f"Précision du modèle KNN : {precision * 100:.2f}%")  # Affichage de la précision

    # Calcul de la matrice de confusion
    cm = confusion_matrix(y_test, y_pred)
    print("Matrice de confusion :")
    print(cm)

    # Calculer le temps écoulé
    elapsed_time = time.time() - start_time  # Temps écoulé en secondes
    print(f"Temps d'entraînement : {elapsed_time:.2f} secondes")  # Affichage du temps d'entraînement

    return model


if __name__ == "__main__":
    run_model()
