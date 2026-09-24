class Synchroniseur:
    """
    Synchronise tous les graphes avec le radar.
    """

    def __init__(self, radar, courbe, heatmap, anomalies):
        self.radar = radar
        self.courbe = courbe
        self.heatmap = heatmap
        self.anomalies = anomalies

    def afficher_etape(self, index):
        print(f"[SYNC] Étape {index}")
