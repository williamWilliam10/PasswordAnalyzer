import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from .extract_features import extract_features

# Fonction pour charger et préparer les données
def load_data(test_file='weak_passwords.txt',
              medium_file='medium_passwords.txt',
              strong_file='strong_passwords.txt'):
    """print("Chargement des fichiers...")"""
    try:
        # Chargement des mots de passe à partir des fichiers
        test_passwords = pd.read_csv(test_file, header=None, names=['password'], on_bad_lines='skip')
        medium_passwords = pd.read_csv(medium_file, header=None, names=['password'], on_bad_lines='skip')
        strong_passwords = pd.read_csv(strong_file, header=None, names=['password'], on_bad_lines='skip')
    except pd.errors.ParserError as e:
        print(f"Erreur lors de la lecture des fichiers : {e}")
        return pd.DataFrame()  # Retourne un DataFrame vide en cas d'erreur

    # Assignation des labels
    test_passwords['label'] = 0   # Faible
    medium_passwords['label'] = 1  # Moyen
    strong_passwords['label'] = 2   # Fort

    # Concaténation des données
    data = pd.concat([test_passwords, medium_passwords, strong_passwords], ignore_index=True)
    """print(f"Total des mots de passe chargés : {len(data)}")  Affiche le nombre total de mots de passe chargés"""

    return data

# Fonction pour extraire les caractéristiques et créer le jeu de données
def prepare_data(data):
    features = data['password'].apply(extract_features).tolist()  # Extraire les caractéristiques des mots de passe
    X = pd.DataFrame(features)  # Convertir en DataFrame
    y = data['label'].values      # Labels des mots de passe
    return X, y

# Fonction pour entraîner le modèle KNN
def train_knn(X_train, y_train):
    """ print("Entraînement du modèle KNN...")"""
    knn = KNeighborsClassifier(n_neighbors=3)  # Choix du nombre de voisins
    knn.fit(X_train, y_train)  # Entraînement du modèle
    return knn

def run_model():
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
   # print(f"Précision du modèle KNN : {precision * 100:.2f}%")
    from sklearn.metrics import confusion_matrix

    # Calcul de la matrice de confusion
    cm = confusion_matrix(y_test, y_pred)
    # print("Matrice de confusion :")
    # print(cm)

    # Calculer le temps écoulé
    """elapsed_time = time.time() - start_time  # Temps écoulé en secondes"""
    """print(f"Temps d'entraînement : {elapsed_time:.2f} secondes")  # Affichage du temps d'entraînement"""
    return model

if __name__ == "__main__":
    run_model()
