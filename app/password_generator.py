import random
import string
from .nlp_filter import contains_common_words
from .utils import is_sequential

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_secure_password(length=12):
    while True:
        password = generate_random_password(length)
        if not contains_common_words(password) and not is_sequential(password):
            return password
