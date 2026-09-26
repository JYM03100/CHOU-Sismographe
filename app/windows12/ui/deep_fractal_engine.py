"""
CHOU Deep-Fractal Engine
------------------------

Analyse fractale profonde :
- résonances entre fenêtres
- similarités mathématiques
- cycles
- motifs récurrents
"""

from src.core.fractales import analyser_fractales
from src.utils.loader_wrapper import load_windows

class DeepFractalEngine:

    def __init__(self):
        self.nom = "CHOU Deep-Fractal Engine"

    def analyser(self):
        historique, actuel = load_windows()
        fractales = analyser_fractales(historique, actuel)
        return fractales
