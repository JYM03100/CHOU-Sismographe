\# ARCHITECTURE — CHOU‑Sismographe‑1



Ce document décrit l’architecture interne du projet CHOU‑Sismographe‑1, telle qu’elle apparaît dans le dépôt GitHub.



\---



\# 1. Vue d’ensemble



CHOU‑Sismographe‑1 est un agent d’analyse temporelle basé sur des métadonnées sociales.  

Il compare deux fenêtres temporelles (2016–2019 vs 2026→présent) et détecte :



\- pics

\- ruptures

\- cycles

\- récurrences

\- similarités fractales



L’architecture est conçue pour être :



\- simple

\- modulaire

\- extensible

\- compatible Copilot (Windows 12 agentique)



\---



\# 2. Structure du dépôt

CHOU-Sismographe-1/

├─ README.md

├─ LICENSE

├─ .gitignore

├─ INSTALL.md

├─ PUBLISHING.md

├─ TESTS.md

├─ requirements.txt

│

├─ src/

│   ├─ indices.py

│   ├─ sismographe.py

│   ├─ visualisation.py

│   ├─ loader.py

│   └─ agentique.py   ← logique fractale CHOU

│

├─ data/

│   ├─ historique\_2016\_2019.csv

│   └─ actuel\_2026\_present.csv

│

├─ logs/

├─ exports/

└─ visualisations/



\---



\# 3. Description des modules



\## 3.1. indices.py  

Calcule les indices quantitatifs :



\- volume total

\- variation moyenne

\- intensité (écart-type)

\- agrégation par date



\## 3.2. sismographe.py  

Détection :



\- cycles courts / moyens / longs

\- ruptures

\- pics

\- anomalies

\- comparaison des fenêtres temporelles



\## 3.3. visualisation.py  

Génère :



\- timelines

\- courbes comparatives

\- exports PNG / SVG



\## 3.4. loader.py  

Charge les données :



\- CSV

\- JSON

\- formats simples



\## 3.5. agentique.py  

Logique fractale CHOU :



\- similarité fractale

\- invariants

\- résumé agentique

\- interprétation douce



\---



\# 4. Pipeline interne



1\. Chargement des données  

2\. Calcul des indices  

3\. Analyse fractale  

4\. Détection des cycles  

5\. Détection des ruptures  

6\. Comparaison des fenêtres  

7\. Synthèse agentique  

8\. Visualisation  

9\. Export



\---



\# 5. Extension Copilot



Le module Copilot utilise :



\- FastAPI

\- endpoints internes

\- manifest Windows 12 agentique



Voir \*\*COPILOT.md\*\* pour les détails.



\---



\# 6. Évolutions prévues



\- module changepoint

\- surveillance continue

\- tableau de bord interactif

\- API publique

\- packaging PyPI





