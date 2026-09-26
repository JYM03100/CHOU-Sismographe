
---

# 🛡 Respect de la vie privée

Le CHOU‑Sismographe :
- n’analyse aucun texte
- ne lit aucun message
- ne collecte aucune donnée personnelle
- ne stocke aucune information sensible

Il ne manipule que des **métadonnées agrégées**.

---

# 🚀 Installation

```bash
pip install -r requirements.txt
python scripts/sismographe.py




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
CHOU-SISMOGRAPHE
├───app
│   ├───android
│   │   │   main.py
│   │   │
│   │   ├───api
│   │   │       chou_api.py
│   │   │
│   │   └───ui
│   │           android_app.py
│   │
│   └───windows12
│       │   companion.py
│       │
│       ├───api
│       │       chou_api.py
│       │
│       └───ui
│               adaptive_companion.py
│               auto_healing.py
│               auto_refresh.py
│               chou_service.py
│               cloud_sync.py
│               copilot_card.py
│               copilot_integration.py
│               dashboard.py
│               deep_telemetry.py
│               desktop_overlay.py
│               event_0500.py
│               hyper_companion.py
│               installer.py
│               kernel_bridge.py
│               live_dashboard.py
│               live_tile.py
│               meta_companion.py
│               multi_device.py
│               multi_user.py
│               notification_center.py
│               os_autopilot.py
│               os_guardian.py
│               scheduler_integration.py
│               secure_mode.py
│               shortcut.py
│               sidebar.py
│               sidebar_copilot.py
│               smart_notification.py
│               system_healing.py
│               system_wide_companion.py
│               taskbar_companion.py
│               telemetry.py
│               tile.py
│               voice-copilot.py
│               voice_command.py
│               widget.py
│               widget_animated.py
│               wigget_dynamic.py
│
├───data
│   ├───metadata
│   ├───processed
│   └───raw
├───exports
│   ├───reports
│   ├───tables
│   └───visualisations
├───logs
│   ├───alerts
│   └───runs
├───scripts
│       sismographe.py
│       visualisation.py
│
├───src
│   ├───agents
│   │       android_agent.py
│   │       copilot_interface.py
│   │       export_agent.py
│   │       interpretation_ia.py
│   │       scheduler.py
│   │       sismographe_agent.py
│   │       visualisation_agent.py
│   │       windows12_agent.py
│   │
│   ├───core
│   │       comparateur.py
│   │       fractales.py
│   │       indices.py
│   │       loader.py
│   │       ruptures.py
│   │
│   └───utils
│           anomalies.py
│           courbes.py
│           heatmap.py
│           radar.py
│           sync.py
│           timeline.py
│           visualisation_interactive.py
│
└───tests
        test_fractales.py
        test_indices.py
        test_loader.py
        test_ruptures.py


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



