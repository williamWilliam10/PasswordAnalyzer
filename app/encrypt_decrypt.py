from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Fonction d'encryption
def encrypt_password(password):
    key = os.urandom(32)  # Génération d'une clé AES (256 bits)
    iv = os.urandom(16)   # Génération d'un vecteur d'initialisation (IV)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()  # Créer un padder
    padded_password = padder.update(password.encode()) + padder.finalize()  # Appliquer le padding

    encrypted_password = encryptor.update(padded_password) + encryptor.finalize()  # Chiffrer

    return encrypted_password, key, iv  # Retourner le mot de passe chiffré, la clé et l'IV

# Fonction de déchiffrement
def decrypt_password(encrypted_password, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_padded_password = decryptor.update(encrypted_password) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()  # Créer un unpadder
    unpadded_password = unpadder.update(decrypted_padded_password) + unpadder.finalize()  # Retirer le padding

    return unpadded_password.decode()  # Retourner le mot de passe en texte clair

# Test du déchiffrement
if __name__ == "__main__":
    "text du cryptage et du decryptage"
    original_password = "monMotDePasse123"  # Mot de passe à tester
    print("Mot de passe original :", original_password)

    # Chiffrer le mot de passe
    encrypted_password, key, iv = encrypt_password(original_password)
    print("Mot de passe chiffré :", encrypted_password.hex())  # Affiche le mot de passe chiffré en hexadécimal

    # Déchiffrer_le mot de passe
    decrypted_password = decrypt_password(encrypted_password, key, iv)
    print("Mot de passe déchiffré :", decrypted_password)

    # Vérifier si le déchiffrement est correct
    assert original_password == decrypted_password, "Le déchiffrement a échoué !"
    print("Le déchiffrement a réussi !")
