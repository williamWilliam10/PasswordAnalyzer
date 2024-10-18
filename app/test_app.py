import pytest
from connect import app


@pytest.fixture
def client():
    """Créer un client de test pour l'application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_verify_password(client):
    """Test de la route /verifier."""
    response = client.post('/verifier', json={'password': 'monMotDePasse'})
    assert response.status_code == 200
    assert 'force' in response.get_json()

def test_generate_password(client):
    """Test de la route /generer."""
    response = client.get('/generer')
    assert response.status_code == 200
    data = response.get_json()
    assert 'password' in data
    assert 'encrypted_password' in data
    assert 'key' in data
    assert 'iv' in data
    assert 'hashed' in data

def test_brute_force_attack(client):
    """Test de la route /attacker/brute_force."""
    # Pour ce test, vous devrez fournir un mot de passe haché valide
    hashed_password = '$2B$12$5ITMR/I36MXDMBPYYMV4DOFQHNSJC/ZIOLCHH8U0KRM...'
    response = client.post('/attacker/brute_force', json={'hashed_password': hashed_password})
    assert response.status_code == 200
    assert 'result' in response.get_json()

def test_dictionary_attack(client):
    """Test de la route /attacker/dictionary."""
    # Pour ce test, vous devrez fournir un mot de passe haché valide
    hashed_password = '$2B$12$5ITMR/I36MXDMBPYYMV4DOFQHNSJC/ZIOLCHH8U0KRM...'
    response = client.post('/attacker/dictionary', json={'hashed_password': hashed_password, 'dictionary_file': 'dictionnaire.txt'})
    assert response.status_code == 200
    assert 'result' in response.get_json()
