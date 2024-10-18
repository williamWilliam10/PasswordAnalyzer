import spacy

# Charger le modèle NLP
nlp = spacy.load("en_core_web_sm")

def contains_common_words(password):
    doc = nlp(password)
    for token in doc:
        if token.is_stop or token.lemma_ in nlp.vocab:
            return True  # Mot courant détecté
    return False
