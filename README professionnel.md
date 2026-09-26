CHOU‑Sismographe‑1

Agent d’analyse de métadonnées sociales comparant deux fenêtres temporelles (2016–2019 vs 2026→présent).  

Détection des pics, ruptures, cycles, récurrences et similarités fractales, sans analyser de texte ni données personnelles.



📌 Présentation générale

CHOU‑Sismographe‑1 est un agent d’analyse temporelle basé sur des métadonnées sociales anonymes.

Il compare deux périodes distinctes :



Fenêtre historique : 2016–2019 (phase « Gilet Jaune »)



Fenêtre actuelle : 2026 → présent



L’objectif est de détecter :



pics d’activité



ruptures



cycles



récurrences



similarités mathématiques



motifs fractals CHOU



Le tout sans analyser de contenu textuel, sans données personnelles, et sans extraction intrusive.

L’agent travaille uniquement sur des indices quantitatifs (volumes, fréquences, rythmes, intensités).



🎯 Objectifs du projet

Construire un sismographe social fractal basé sur des métadonnées.



Comparer les dynamiques sociales entre deux périodes éloignées.



Détecter des motifs récurrents ou des ruptures significatives.



Produire des visualisations interactives et des exports (PNG, SVG, CSV).



Fournir un agent IA capable de surveiller en continu les signaux.



🧠 Philosophie CHOU

Le projet s’inscrit dans la logique du système CHOU, qui vise à :



modéliser les comportements humains sous forme de cycles,



détecter les récurrences fractales,



analyser les motifs temporels plutôt que les contenus,



rester non intrusif, non politique, non spéculatif.



🏗️ Architecture du dépôt

(Version mise à jour pour CHOU‑Sismographe‑1)



Code

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

│   ├─ indices.py          # Calcul des indices quantitatifs

│   ├─ sismographe.py      # Détection cycles, ruptures, comparaisons

│   ├─ visualisation.py    # Graphiques, timelines, exports

│   ├─ loader.py           # Chargement des données

│   └─ agentique.py        # Logique fractale CHOU (à ajouter)

│

├─ data/                   # Données locales (non versionnées)

│   ├─ historique\_2016\_2019.csv

│   └─ actuel\_2026\_present.csv

│

├─ logs/                   # Journaux d’exécution

├─ exports/                # Graphiques, rapports, images

└─ visualisations/         # Notebooks, figures

Les dossiers data/, logs/, exports/ sont ignorés par Git.



⚙️ Fonctionnement de l’agent

L’agent CHOU‑Sismographe‑1 :



Charge les données (CSV, JSON, etc.)



Agrège les indices (par jour, semaine, mois)



Calcule les métriques (volumes, variations, intensités)



Compare les deux fenêtres temporelles



Détecte les motifs (pics, creux, ruptures, corrélations)



Génère des visualisations



Produit des exports



Peut fonctionner en mode surveillance continue  



📊 Exemple de code (extrait simplifié)

python

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



🚀 Installation

1\. Cloner le dépôt

Code

git clone https://github.com/JYM03100/CHOU-Sismographe-1

2\. Installer les dépendances

Code

pip install -r requirements.txt

(Le fichier sera complété dans une étape future.)  



▶️ Utilisation

Lancer l’agent

Code

python chou\_sismos\_v3.py

Visualisations

Les graphiques générés apparaissent dans :



Code

exports/



🔒 Respect de la vie privée

CHOU‑Sismographe‑1 :



n’analyse aucun texte



ne collecte aucune donnée personnelle



ne traite aucune information sensible



ne réalise aucune extraction intrusive



Il travaille uniquement sur des métadonnées anonymes et des indices quantitatifs.



📄 Licence

Ce projet est sous licence MIT.



🤝 Contributions

Les contributions sont les bienvenues :



corrections



améliorations



visualisations



modules supplémentaires



documentation



Ouvrez une issue ou une pull request.



🧭 Feuille de route

\[ ] Module de détection de ruptures (changepoint)



\[ ] Module de similarité fractale



\[ ] Mode surveillance continue



\[ ] Tableau de bord interactif



\[ ] Fichier requirements.txt



\[ ] Tests unitaires

