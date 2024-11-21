# Variables
IMAGE_NAME=health-calculator-service
PORT=5000

.PHONY: init run test build clean

# Initialiser les dépendances
init:
	@echo "Installation des dépendances..."
	pip install -r requirements.txt

# Lancer l'application localement
run:
	@echo "Démarrage de l'application Flask..."
	python app.py

# Exécuter les tests
test:
	@echo "Exécution des tests unitaires..."
	python -m unittest discover

# Construire l'image Docker
build:
	@echo "Construction de l'image Docker..."
	docker build -t $(IMAGE_NAME) .

# Nettoyer les fichiers temporaires
clean:
	@echo "Nettoyage des fichiers temporaires..."
	rm -rf __pycache__
