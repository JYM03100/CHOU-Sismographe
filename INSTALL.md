# INSTALLATION

## 1. Prérequis

- Python 3.10 ou supérieur (3.14 recommandé)
- pip (installé automatiquement avec Python)
- GitHub Desktop (pour la gestion du dépôt)
- Git interne de GitHub Desktop (aucune installation supplémentaire nécessaire)

## 2. Cloner le dépôt

Ouvrez GitHub Desktop :

- File → Clone repository
- Entrez l’URL du projet :
  https://github.com/JYM03100/CHOU-Sismographe.git

Ou en ligne de commande (optionnel) :


## 3. Installer les dépendances Python

Dans un terminal : 
pip install -r requirements.txt



## 4. Créer les dossiers nécessaires

À la racine du projet, créez les dossiers :
data/
logs/
exports/

Ces dossiers sont ignorés par Git (voir `.gitignore`).

## 5. Ajouter vos données

Placez vos fichiers CSV dans :
data/historique_2016_2019.csv
data/actuel_2026_present.csv


## 6. Lancer l’agent
python chou_sismos_v3.py


Les visualisations générées apparaîtront dans :
exports/

