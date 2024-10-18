def extract_features(password):
    # Fonction qui extrait des caractéristiques d'un mot de passe donné

    features = {}  # Dictionnaire pour stocker les caractéristiques du mot de passe
    features['length'] = len(password)  # Longueur du mot de passe

    # Vérifie si le mot de passe contient au moins une lettre majuscule
    features['has_upper'] = int(any(c.isupper() for c in password))
    # Vérifie si le mot de passe contient au moins une lettre minuscule
    features['has_lower'] = int(any(c.islower() for c in password))
    # Vérifie si le mot de passe contient au moins un chiffre
    features['has_digit'] = int(any(c.isdigit() for c in password))
    # Vérifie si le mot de passe contient au moins un caractère spécial
    features['has_special'] = int(any(not c.isalnum() for c in password))

    return features  # Retourne le dictionnaire contenant les caractéristiques


if __name__ == "__main__":
    # Si ce fichier est exécuté directement, cette section sera exécutée
    password = "Passw0rd!123"  # Exemple de mot de passe à analyser
    features = extract_features(password)  # Extraction des caractéristiques du mot de passe
    print("le mot de passe est : ", password)
    print("Les caractéristiques sont :")
    print(features)  # Affichage des caractéristiques extraites
