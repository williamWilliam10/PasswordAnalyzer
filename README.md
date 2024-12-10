# SmartPass

## Description
**SecurePassGen** est un système de génération de mots de passe sécurisés utilisant des modèles probabilistes et des techniques de traitement du langage naturel (NLP). Le système permet de générer des mots de passe robustes tout en excluant les séquences faciles à deviner et les mots courants.

## Fonctionnalités
- Génération de mots de passe aléatoires.
- Filtrage des mots de passe basés sur des mots courants à l'aide de techniques de NLP.
- Évaluation des mots de passe avec un modèle de classification KNN.
- Classification des mots de passe en faibles, moyennes et fortes.
- Chiffrement et hachage des mots de passe pour une sécurité renforcée.
- Tests d'attaques par force brute et par dictionnaire pour évaluer la robustesse des mots de passe.

## Prérequis
- Python 3.7 ou supérieur
- Pip

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/williamWilliam10/SecurePassGen.git
   cd SecurePassGen
