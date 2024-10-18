import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def decrypt_password(encrypted_password, key, iv):
    # Création du chiffre AES
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Déchiffrement du mot de passe
    decrypted_padded_password = decryptor.update(encrypted_password) + decryptor.finalize()

    # Retirer le padding PKCS#7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_password = unpadder.update(decrypted_padded_password) + unpadder.finalize()

    return unpadded_password.decode()  # Retourner le mot de passe en texte clair

