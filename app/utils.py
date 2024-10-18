def is_sequential(password):
    """
    Vérifie si le mot de passe contient une séquence continue de caractères ou de chiffres.
    Exemples de séquences : "abc", "123", "xyz", "zyx", "321", etc.
    """
    # Vérifie les séquences croissantes et décroissantes de lettres ou de chiffres
    for i in range(len(password) - 1):
        if (ord(password[i + 1]) - ord(password[i]) == 1) or \
           (ord(password[i]) - ord(password[i + 1]) == 1):
            return True  # Séquence détectée
    return False
