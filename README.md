# CHOU -Sismographe     

Agent d’analyse de métadonnées sociales comparant deux fenêtres temporelles "Gilet Jaune" (2016–2019 et 2026→présent). CHOU-Sismographe détecte pics, ruptures, similarités mathématiques et génère des visualisations interactives, sans analyser de contenu textuel ni données personnelles.


\# CHOU‑Sismographe  

Agent d’analyse de métadonnées sociales sur deux fenêtres temporelles



\---



\## 📌 Présentation générale



\*\*CHOU‑Sismographe\*\* est un agent d’analyse de métadonnées sociales conçu pour comparer deux périodes distinctes :



\- \*\*Fenêtre historique :\*\* 2016–2019 (phase « Gilet Jaune »)  

\- \*\*Fenêtre actuelle :\*\* 2026 → présent



L’objectif est de détecter :



\- pics d’activité  

\- ruptures  

\- cycles  

\- récurrences  

\- similarités mathématiques entre les deux fenêtres temporelles  



Le tout \*\*sans analyser de contenu textuel\*\*, \*\*sans données personnelles\*\*, et \*\*sans extraction intrusive\*\*.  

CHOU‑Sismographe travaille uniquement sur des \*\*indices quantitatifs\*\* (volumes, fréquences, rythmes, intensités).



\---



\## 🎯 Objectifs du projet



\- Construire un \*\*sismographe social fractal\*\* basé sur des métadonnées.  

\- Comparer les dynamiques sociales entre deux périodes éloignées.  

\- Détecter des motifs récurrents ou des ruptures significatives.  

\- Produire des \*\*visualisations interactives\*\* et des exports (PNG, SVG, CSV).  

\- Fournir un agent IA capable de \*\*surveiller en continu\*\* les signaux.



\---



\## 🧠 Philosophie CHOU



CHOU‑Sismographe s’inscrit dans la logique du système \*\*CHOU\*\*, qui vise à :



\- modéliser les comportements humains sous forme de \*\*cycles\*\*,  

\- détecter les \*\*récurrences fractales\*\*,  

\- analyser les \*\*motifs temporels\*\* plutôt que les contenus,  

\- rester \*\*non intrusif\*\*, \*\*non politique\*\*, \*\*non spéculatif\*\*.



\---



\## 🏗️ Architecture du projet



```

CHOU-Sismographe/

├─ README.md

├─ LICENSE

├─ .gitignore

├─ chou\_sismos\_v3.py          ← code principal de l’agent

├─ data/                      ← données locales (non versionnées)

│   ├─ historique\_2016\_2019.csv

│   └─ actuel\_2026\_present.csv

├─ logs/                      ← journaux d’exécution

├─ exports/                   ← graphiques, rapports, images

└─ visualisations/            ← notebooks, figures

```



Les dossiers `data/`, `logs/`, `exports/` sont ignorés par Git (voir `.gitignore`).



\---



\## ⚙️ Fonctionnement de l’agent



L’agent CHOU‑Sismographe :



1\. \*\*Charge les données\*\* (CSV, JSON, etc.)  

2\. \*\*Agrège les indices\*\* (par jour, semaine, mois)  

3\. \*\*Calcule les métriques\*\* (volumes, variations, intensités)  

4\. \*\*Compare les deux fenêtres temporelles\*\*  

5\. \*\*Détecte les motifs\*\* (pics, creux, ruptures, corrélations)  

6\. \*\*Génère des visualisations\*\*  

7\. \*\*Produit des exports\*\*  

8\. Peut fonctionner en \*\*mode surveillance continue\*\*



\---



\## 📊 Exemple de code (extrait simplifié)



```python

import pandas as pd

import matplotlib.pyplot as plt



class SismographeAgent:

&#x20;   def \_\_init\_\_(self, historique\_path, actuel\_path):

&#x20;       self.historique\_path = historique\_path

&#x20;       self.actuel\_path = actuel\_path



&#x20;   def charger\_donnees(self):

&#x20;       self.historique = pd.read\_csv(self.historique\_path)

&#x20;       self.actuel = pd.read\_csv(self.actuel\_path)



&#x20;   def calculer\_indices(self):

&#x20;       hist = self.historique.groupby("date")\["volume\_posts"].sum()

&#x20;       act = self.actuel.groupby("date")\["volume\_posts"].sum()

&#x20;       return hist, act



&#x20;   def comparer(self):

&#x20;       hist, act = self.calculer\_indices()

&#x20;       return {

&#x20;           "correlation": hist.corr(act),

&#x20;           "diff\_moyenne": act.mean() - hist.mean()

&#x20;       }



&#x20;   def visualiser(self, output="exports/comparaison.png"):

&#x20;       hist, act = self.calculer\_indices()

&#x20;       plt.figure(figsize=(12, 6))

&#x20;       plt.plot(hist.index, hist.values, label="2016–2019")

&#x20;       plt.plot(act.index, act.values, label="2026→présent")

&#x20;       plt.legend()

&#x20;       plt.savefig(output)

&#x20;       plt.close()

```



\---



\## 🚀 Installation



\### 1. Cloner le dépôt

```

git clone https://github.com/JYM03100/CHOU-Sismographe.git

```



\### 2. Installer les dépendances

```

pip install -r requirements.txt

```



\*(Le fichier `requirements.txt` sera ajouté dans une étape future.)\*



\---



\## ▶️ Utilisation



\### Lancer l’agent

```

python chou\_sismos\_v3.py

```



\### Visualisations

Les graphiques générés apparaissent dans :



```

exports/

```



\---



\## 🔒 Respect de la vie privée



CHOU‑Sismographe :



\- n’analyse \*\*aucun texte\*\*  

\- ne collecte \*\*aucune donnée personnelle\*\*  

\- ne traite \*\*aucune information sensible\*\*  

\- ne réalise \*\*aucune extraction intrusive\*\*  



Il travaille uniquement sur des \*\*métadonnées anonymes\*\* et des \*\*indices quantitatifs\*\*.



\---



\## 📄 Licence



Ce projet est sous licence \*\*MIT\*\*.  

Vous êtes libre de l’utiliser, le modifier et le redistribuer.



\---



\## 🤝 Contributions



Les contributions sont les bienvenues :



\- corrections  

\- améliorations  

\- visualisations  

\- modules supplémentaires  

\- documentation  



Ouvrez une \*\*issue\*\* ou une \*\*pull request\*\*.



\---



\## 🧭 Feuille de route



\- \[ ] Ajout du module de détection de ruptures (changepoint)  

\- \[ ] Ajout du module de similarité fractale  

\- \[ ] Ajout du mode surveillance continue  

\- \[ ] Ajout du tableau de bord interactif  

\- \[ ] Ajout du fichier `requirements.txt`  

\- \[ ] Ajout des tests unitaires  



\---



