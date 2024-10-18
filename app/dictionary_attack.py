import time
import hashlib

def dictionary_attack(hashed_password, dictionary_file):
    start_time = time.time()
    attempts = 0
    cracked_password = None

    try:
        with open(dictionary_file, 'r') as file:
            for line in file:
                attempts += 1
                password_attempt = line.strip()  # Supprimer les espaces
                hashed_attempt = hashlib.sha256(password_attempt.encode()).hexdigest()

                # Vérifier si le hachage correspond
                if hashed_attempt == hashed_password:
                    cracked_password = password_attempt
                    break
    except FileNotFoundError:
        return {'error': 'Le fichier de dictionnaire est introuvable.'}

    elapsed_time = time.time() - start_time
    return {
        'cracked_password': cracked_password,
        'attempts': attempts,
        'elapsed_time': elapsed_time
    }
