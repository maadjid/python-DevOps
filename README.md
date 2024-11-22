# Health Calculator Service

## Description
Cette application permet de calculer :
- **BMI (Body Mass Index)** pour évaluer votre poids par rapport à votre taille.
- **BMR (Basal Metabolic Rate)** pour estimer les besoins caloriques journaliers.

L'application utilise Flask pour l'API, est containerisée avec Docker, et est déployée sur Azure avec un pipeline CI/CD automatisé.

---

## Fonctionnalités
- API REST légère pour calculer le BMI et le BMR.
- Tests unitaires pour garantir la fiabilité des calculs.
- CI/CD configuré avec GitHub Actions pour tester, construire et déployer automatiquement.
- Hébergement sur Azure avec un accès en ligne.

---

## Prérequis
- Python 3.9 ou supérieur.
- Docker installé.
- Accès à GitHub et Azure.

---

## Installation et Exécution

### En local (sans Docker)
1. **Clonez le dépôt :**
   ```bash
   git clone https://github.com/maadjid/python-DevOps.git
   cd python-DevOps

    Créez un environnement virtuel et installez les dépendances :

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Lancez l'application :

    python app.py

    L'API sera disponible à l'adresse http://localhost:5000.

Avec Docker

    Construisez l'image Docker :

docker build -t health-calculator-service .

Lancez le conteneur :

    docker run -p 5000:5000 health-calculator-service

Utilisation de l'API
Endpoint /bmi

    Méthode : POST
    Description : Calcule le BMI (Body Mass Index).
    Exemple d'entrée :

{
    "height": 1.75,
    "weight": 70
}

Exemple de réponse :

    {
        "bmi": 22.86
    }

Endpoint /bmr

    Méthode : POST
    Description : Calcule le BMR (Basal Metabolic Rate).
    Exemple d'entrée :

{
    "height": 175,
    "weight": 70,
    "age": 25,
    "gender": "male"
}

Exemple de réponse :

    {
        "bmr": 1666.5
    }

Tests

    Exécutez les tests unitaires avec la commande :

    python -m unittest discover

    Les tests vérifient la fiabilité des calculs pour le BMI et le BMR.

Déploiement CI/CD

Le pipeline GitHub Actions effectue les étapes suivantes :

    Installation des dépendances.
    Exécution des tests unitaires.
    Construction et push de l'image Docker.
    Déploiement sur Azure.

Accès à l'application déployée

Application déployée sur Azure :
https://bennouarapp-dmbqb9cee7fvfthw.francecentral-01.azurewebsites.net/
Auteur

Projet réalisé par Majid Bennouar dans le cadre du cours MSI DevOps.