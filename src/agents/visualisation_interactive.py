"""
src/agents/visualisation_interactive.py
---------------------------------------

Visualisation interactive CHOU :
- défilement automatique des courbes
- interruption manuelle
- zoom tactile / souris
- reprise du défilement avec zoom conservé

Utilise Plotly pour compatibilité PC + Android.
"""

import time
import plotly.graph_objects as go
from threading import Thread


class VisualisationInteractive:

    def __init__(self, indices):
        self.indices = indices
        self.running = False
        self.position = 0
        self.zoom_range = None  # (min, max)

    # ---------------------------------------------------------
    # Génération de la figure Plotly
    # ---------------------------------------------------------
    def _generer_figure(self):
        labels = []
        h_vals = []
        a_vals = []

        for cle, val in self.indices.items():
            if isinstance(val, dict):
                labels.append(cle)
                h_vals.append(val["historique"])
                a_vals.append(val["actuel"])

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=list(range(len(labels))),
            y=h_vals,
            mode="lines",
            name="Historique"
        ))

        fig.add_trace(go.Scatter(
            x=list(range(len(labels))),
            y=a_vals,
            mode="lines",
            name="Actuel"
        ))

        fig.update_layout(
            title="Défilement interactif CHOU",
            xaxis_title="Index",
            yaxis_title="Valeur",
            dragmode="pan"
        )

        return fig

    # ---------------------------------------------------------
    # Défilement automatique
    # ---------------------------------------------------------
    def _defilement(self, fig):
        self.running = True

        while self.running and self.position < len(self.indices):
            # Mise à jour de la fenêtre de zoom si définie
            if self.zoom_range:
                fig.update_xaxes(range=self.zoom_range)

            # Mise à jour de la position
            fig.update_traces(
                selector=dict(name="Actuel"),
                x=list(range(self.position))
            )

            time.sleep(0.2)
            self.position += 1

    def lancer_defilement(self):
        fig = self._generer_figure()
        thread = Thread(target=self._defilement, args=(fig,))
        thread.start()
        return fig

    # ---------------------------------------------------------
    # Interruption
    # ---------------------------------------------------------
    def interrompre(self):
        self.running = False

    # ---------------------------------------------------------
    # Zoom manuel
    # ---------------------------------------------------------
    def definir_zoom(self, min_x, max_x):
        self.zoom_range = (min_x, max_x)

    # ---------------------------------------------------------
    # Reprise du défilement
    # ---------------------------------------------------------
    def reprendre(self):
        fig = self._generer_figure()
        thread = Thread(target=self._defilement, args=(fig,))
        thread.start()
        return fig
