import pandas as pd
from src.loader import charger_csv
from src.sismographe import SismographeAgent
from src.visualisation import tracer_timelines, tracer_heatmap

# ---------------------------------------------------------
# CHOU‑Sismographe — Script principal
# ---------------------------------------------------------

def main():
    print("=== CHOU‑Sismographe — Analyse des métadonnées sociales ===")

    # -----------------------------------------------------
    # 1. Chargement des données
    # -----------------------------------------------------
    historique_path = "data/historique_2016_2019.csv"
    actuel_path = "data/actuel_2026_present.csv"

    print("Chargement des données...")
    historique_df = charger_csv(historique_path)
    actuel_df = charger_csv(actuel_path)

    # -----------------------------------------------------
    # 2. Initialisation de l’agent
    # -----------------------------------------------------
    agent = SismographeAgent(historique_path, actuel_path)
    agent.historique_df = historique_df
    agent.actuel_df = actuel_df

    # -----------------------------------------------------
    # 3. Analyse fractale CHOU
    # -----------------------------------------------------
    print("Analyse fractale CHOU...")
    fractale = agent.analyse_fractale()
    print("Similarité fractale :", fractale["similarite_fractale"])

    # -----------------------------------------------------
    # 4. Détection des cycles
    # -----------------------------------------------------
    print("Détection des cycles...")
    cycles = agent.detecter_cycles()
    print("Cycles historiques :", cycles["historique"])
    print("Cycles actuels :", cycles["actuel"])

    # -----------------------------------------------------
    # 5. Détection des ruptures
    # -----------------------------------------------------
    print("Détection des ruptures...")
    ruptures = agent.detecter_ruptures()
    print("Ruptures historiques :", ruptures["historique"])
    print("Ruptures actuelles :", ruptures["actuel"])

    # -----------------------------------------------------
    # 6. Comparaison des fenêtres temporelles
    # -----------------------------------------------------
    print("Comparaison des fenêtres...")
    comparaison = agent.comparer_fenetres()
    print("Corrélation :", comparaison["correlation"])
    print("Différence moyenne :", comparaison["diff_moyenne"])

    # -----------------------------------------------------
    # 7. Résumé agentique CHOU
    # -----------------------------------------------------
    print("Résumé CHOU...")
    resume = agent.resume()
    print(resume)

    # -----------------------------------------------------
    # 8. Visualisations
    # -----------------------------------------------------
    print("Génération des visualisations...")
    tracer_timelines(historique_df, actuel_df)
    tracer_heatmap(historique_df, actuel_df)

    print("Exports générés dans le dossier 'exports/'.")
    print("=== Analyse terminée ===")


if __name__ == "__main__":
    main()
