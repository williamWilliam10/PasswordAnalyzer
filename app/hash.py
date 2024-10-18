import bcrypt

def hash_password(password):
    # Génération du sel et du hachage avec bcrypt
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def verify_password(password, hashed_password):
    # Vérification du mot de passe en comparant avec le haché
    return bcrypt.checkpw(password.encode(), hashed_password)
