# TESTS

CHOU‑Sismographe inclut des tests simples pour vérifier le bon fonctionnement de l’agent.

## ✔ Test 1 — Chargement des données

python -c "from chou_sismos_v3 import SismographeAgent; a=SismographeAgent('data/historique_2016_2019.csv','data/actuel_2026_present.csv'); a.charger_donnees(); print('Chargement OK')"


## ✔ Test 2 — Calcul des indices

python -c "from chou_sismos_v3 import SismographeAgent; a=SismographeAgent('data/historique_2016_2019.csv','data/actuel_2026_present.csv'); a.charger_donnees(); print(a.calculer_indices())"


## ✔ Test 3 — Génération de visualisation

python -c "from chou_sismos_v3 import SismographeAgent; a=SismographeAgent('data/historique_2016_2019.csv','data/actuel_2026_present.csv'); a.charger_donnees(); a.visualiser()"


Le fichier généré doit apparaître dans :

exports/comparaison.png

