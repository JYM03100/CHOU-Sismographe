\# TESTS — CHOU‑Sismographe‑1



Ce fichier décrit la structure des tests unitaires et d’intégration.



\---



\# 1. Structure des tests

tests/

unit/

test\_indices.py

test\_sismographe.py

test\_agentique.py

integration/

test\_pipeline.py

test\_visualisation.py





\---



\# 2. Tests unitaires



\## 2.1. test\_indices.py



Vérifie :



\- calcul du volume  

\- variation moyenne  

\- intensité (écart-type)  

\- absence d’erreurs si données vides  



\## 2.2. test\_sismographe.py



Vérifie :



\- détection des cycles  

\- détection des ruptures  

\- comparaison des fenêtres  

\- cohérence des résultats  



\## 2.3. test\_agentique.py



Vérifie :



\- similarité fractale  

\- cohérence des invariants  

\- résumé agentique CHOU  



\---



\# 3. Tests d’intégration



\## 3.1. test\_pipeline.py



Vérifie :



\- chargement des données  

\- calcul des indices  

\- analyse fractale  

\- comparaison des fenêtres  

\- génération du résumé  



\## 3.2. test\_visualisation.py



Vérifie :



\- génération des graphiques  

\- absence d’erreurs matplotlib  

\- création des fichiers dans `exports/`  



\---



\# 4. Exemple de test (pytest)

import pandas as pd

from src.indices import calculer\_indices



def test\_calculer\_indices():

df = pd.DataFrame({

"date": \["2026-01-01", "2026-01-02"],

"volume\_posts": \[10, 20]

})



indices = calculer\_indices(df, df)

assert indices\["historique"]\["volume"] == 30



\---



\# 5. Lancer les tests

pytest -q



\---



\# 7. Bonnes pratiques



\- Un test = un comportement  

\- Pas de dépendance réseau  

\- Pas de dépendance aux fichiers réels  

\- Tests rapides (< 1 seconde chacun)  









