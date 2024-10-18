import itertools
import time
import hashlib

def brute_force_attack(hashed_password):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&]=àç_è-(éù*$^µù$^!:;,<>* ' # Ensemble de caractères à tester
    max_length = 6  # Longueur maximale des mots de passe à tester
    start_time = time.time()

    # Pour stocker le résultat
    cracked_password = None
    attempts = 0

    # Tester toutes les combinaisons possibles jusqu'à max_length
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempts += 1
            password_attempt = ''.join(attempt)
            # Hachage de la tentative de mot de passe
            hashed_attempt = hashlib.sha256(password_attempt.encode()).hexdigest()  # Utiliser le même algorithme de hachage

            # Vérifier si le hachage correspond
            if hashed_attempt == hashed_password:
                cracked_password = password_attempt
                break
        if cracked_password:
            break

    elapsed_time = time.time() - start_time
    return {
        'cracked_password': cracked_password,
        'attempts': attempts,
        'elapsed_time': elapsed_time
    }
