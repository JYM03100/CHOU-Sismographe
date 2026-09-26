# INSTALLATION — CHOU‑Sismographe‑1

Ce guide explique comment installer, configurer et exécuter l’agent CHOU‑Sismographe‑1.

---

## 1. Prérequis

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets)
- Git
- Environnement virtuel recommandé (venv)

---

## 2. Cloner le dépôt

git clone https://github.com/JYM03100/CHOU-Sismographe-1
cd CHOU-Sismographe-1

---

## 3. Créer un environnement virtuel

python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

---

## 4. Installer les dépendances

pip install -r requirements.txt


*(Si le fichier n’existe pas encore, il sera généré dans une étape future.)*

---

## 5. Préparer les données

Placez vos fichiers CSV dans :
data/
historique_2016_2019.csv
actuel_2026_present.csv

Les fichiers doivent contenir au minimum :

- `date` (YYYY-MM-DD)
- `volume_posts` (entier)

---

## 6. Lancer l’agent

python chou_sismos_v3.py

---

## 7. Visualisations

Les exports apparaissent dans :

exports/

---

## 8. Dépannage

### Problème : Module introuvable
Solution :
export PYTHONPATH=.

### Problème : dépendances manquantes
Solution :
pip install -r requirements.txt

---

## 9. Mise à jour
git pull origin master

---

## 10. Désinstallation

Supprimez simplement le dossier du projet et l’environnement virtuel.






