"""
src/utils/plotly_base.py
------------------------

Base Plotly pour toutes les visualisations CHOU :
- thème graphique
- palette CHOU
- symboles (étoile / cercle)
- styles de traits
- export PNG
- export HTML
"""

import plotly.graph_objects as go
import plotly.io as pio
from pathlib import Path

# ---------------------------------------------------------
# Thème Plotly CHOU
# ---------------------------------------------------------
pio.templates["chou_theme"] = go.layout.Template(
    layout=dict(
        font=dict(family="Segoe UI", size=14, color="#FFFFFF"),
        paper_bgcolor="#0A0A0A",
        plot_bgcolor="#0A0A0A",
        margin=dict(l=40, r=40, t=40, b=40),
        polar=dict(
            bgcolor="#0A0A0A",
            radialaxis=dict(showgrid=True, gridcolor="#333333"),
            angularaxis=dict(showgrid=True, gridcolor="#333333"),
        ),
    )
)

pio.templates.default = "chou_theme"

# ---------------------------------------------------------
# Palette CHOU
# ---------------------------------------------------------
PALETTE_CHOU = {
    "historique": "#FFD700",   # or doux
    "actuel": "#1E90FF",       # bleu CHOU
    "rupture": "#FF4500",      # orange rupture
    "fractale": "#32CD32",     # vert fractal
}

# ---------------------------------------------------------
# Symboles CHOU
# ---------------------------------------------------------
def symbole_ip(is_foreign: bool):
    return "star" if is_foreign else "circle"

# ---------------------------------------------------------
# Styles de traits CHOU
# ---------------------------------------------------------
STYLES = [
    "solid",
    "dot",
    "dash",
    "dashdot",
    "longdash",
    "longdashdot"
]

def style_annee(annee: int):
    return STYLES[annee % len(STYLES)]

# ---------------------------------------------------------
# Export PNG
# ---------------------------------------------------------
def export_png(fig, filename: str):
    path = Path("exports/visualisations")
    path.mkdir(parents=True, exist_ok=True)
    fig.write_image(path / filename)

# ---------------------------------------------------------
# Export HTML (optionnel)
# ---------------------------------------------------------
def export_html(fig, filename: str):
    path = Path("exports/visualisations")
    path.mkdir(parents=True, exist_ok=True)
    fig.write_html(path / filename)
