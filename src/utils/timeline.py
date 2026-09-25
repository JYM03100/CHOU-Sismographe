class Timeline:
    """
    Barre de progression (auto + manuel).
    Version squelette.
    """

    def __init__(self, data):
        self.data = data
        self.index = 0
        self.max_index = len(data)

    def auto(self):
        print("[TIMELINE] Défilement automatique…")

    def avant(self):
        print("[TIMELINE] Avance d'une étape…")

    def arriere(self):
        print("[TIMELINE] Recule d'une étape…")
