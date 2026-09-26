# PUBLISHING — CHOU‑Sismographe‑1

Ce guide explique comment publier le projet :
- sur GitHub (version stable)
- sur PyPI (package Python)
- en tant qu’extension Copilot (Windows 12 agentique)

---

# 1. Publication GitHub

## 1.1. Créer une release

1. Aller sur le dépôt GitHub  
2. Cliquer sur **Releases**  
3. Créer une nouvelle release  
4. Tag : `v0.1.0`  
5. Titre : “CHOU‑Sismographe‑1 — Première version stable”  
6. Description :  
   - ajout des modules d’analyse  
   - ajout des visualisations  
   - ajout du manifest Copilot  
   - ajout des endpoints API

---

# 2. Publication PyPI (optionnel)

## 2.1. Préparer la structure

Créer un dossier :
chou_sismographe/
init.py
agent.py
indices.py
sismographe.py
visualisation.py

## 2.2. Créer `pyproject.toml`
[project]
name = "chou-sismographe"
version = "0.1.0"
description = "Analyse fractale et cycles sociaux"
authors = [{name="Le"}]
dependencies = ["pandas", "numpy", "matplotlib"]


## 2.3. Build

python -m build

## 2.4. Upload

twine upload dist/*


---

# 3. Publication Copilot (Windows 12 agentique)

## 3.1. Structure requise
app/windows12/
manifest/extension.json
api/
ui/

## 3.2. Vérifier le manifest

Le fichier `extension.json` doit contenir :

- nom de l’extension  
- version  
- endpoints API  
- pages UI  

## 3.3. Déployer

Via Copilot Studio :

1. Créer une nouvelle extension  
2. Importer le manifest  
3. Ajouter les endpoints  
4. Tester l’agent  
5. Publier

---

# 4. Versioning

Utiliser SemVer :

- `MAJOR.MINOR.PATCH`
- `0.1.0` → première version stable
- `0.2.0` → ajout de nouvelles analyses
- `1.0.0` → version publique

---

# 5. Bonnes pratiques

- Toujours tester avant de publier  
- Documenter chaque changement  
- Ne jamais publier de données personnelles  
- Garder les exports hors du dépôt  


