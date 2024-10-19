import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'; // Assurez-vous d'importer votre fichier CSS personnalisé

function App() {
  const [motDePasse, setMotDePasse] = useState('');
  const [resultat, setResultat] = useState('');
  const [motDePasseGenere, setMotDePasseGenere] = useState('');
  const [error, setError] = useState('');

  const verifierMotDePasse = async () => {
    try {
      const response = await axios.post('https://web-production-b62ae.up.railway.app/verifier', { password: motDePasse });
      setResultat(`Le mot de passe est : ${response.data.force}`);
      setError('');
    } catch (error) {
      console.error("Erreur lors de la vérification :", error);
      setError('Erreur lors de la vérification du mot de passe.');
    }
  };

  const genererMotDePasse = async () => {
    try {
      const response = await axios.get('https://web-production-b62ae.up.railway.app/generer');
      setMotDePasseGenere(response.data.password);
      setError('');
    } catch (error) {
      console.error("Erreur lors de la génération du mot de passe :", error);
      setError("Erreur lors de la génération du mot de passe.");
    }
  };

  return (
    <section>
      {[...Array(100)].map((_, i) => (
        <span key={i}></span>
      ))}
      <div className="signin">
        <div className="content">
          <h2 className="text-center">SecureGen</h2>
          <div className="form">
            <div className="input-group">
              <input
                type="password"
                className="form-control"
                id="motDePasse"
                value={motDePasse}
                onChange={(e) => setMotDePasse(e.target.value)}
                placeholder="Entrez votre mot de passe"
                aria-label="Mot de passe"
              />
              <button className="btn" type="button" style={{ backgroundColor: "#0f0" }} onClick={verifierMotDePasse}>
                Vérifier
              </button>
            </div>
            {resultat && <p className="mt-2 text-white">{resultat}</p>}
            {error && <div className="alert alert-danger mt-2">{error}</div>}

            <button className="btn btn-secondary mt-1" type="button" onClick={genererMotDePasse}>
              Générer un mot de passe
            </button>
            {motDePasseGenere && <p className="text-success">Mot de passe généré : <strong style={{ color: "white" }}>{motDePasseGenere}</strong></p>}
          </div>
          <div className="card-footer text-success">
            Créez un mot de passe fort pour protéger vos informations !
          </div>
        </div>
      </div>
    </section>
  );
}

export default App;
