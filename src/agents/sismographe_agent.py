class SismographeAgent:
    """
    Agent principal du CHOU‑Sismographe.
    Orchestration : chargement, indices, visualisations.
    """

    def __init__(self, historique_path, actuel_path):
        self.historique_path = historique_path
        self.actuel_path = actuel_path
        self.historique = None
        self.actuel = None

    def charger_donnees(self):
        from src.utils.loader import charger_csv
        self.historique = charger_csv(self.historique_path)
        self.actuel = charger_csv(self.actuel_path)

    def calculer_indices(self):
        from src.utils.indices import calculer_indices
        return calculer_indices(self.historique, self.actuel)

    def visualiser_radar(self):
        from src.utils.radar import generer_radar
        generer_radar(self.historique, self.actuel)

    def visualiser_courbes(self):
        from src.utils.courbes import generer_courbes
        generer_courbes(self.historique, self.actuel)

    def visualiser_heatmap(self):
        from src.utils.heatmap import generer_heatmap
        generer_heatmap(self.historique, self.actuel)
