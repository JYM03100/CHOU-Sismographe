import streamlit as st
from pathlib import Path

from src.agents.sismographe_agent import SismographeAgent
from src.agents.copilot_interface import CopilotInterface

# -------------------------------------------------------------------
# Configuration de la page
# -------------------------------------------------------------------
st.set_page_config(
    page_title="CHOU-Sismographe",
    layout="wide"
)

st.title("CHOU-Sismographe – Tableau de bord Streamlit")
st.markdown(
    "Lecture douce et proportionnée des dynamiques sociales entre "
    "deux fenêtres temporelles."
)

# -------------------------------------------------------------------
# Sélection des fichiers de données
# -------------------------------------------------------------------
st.sidebar.header("Données")
historique_path = st.sidebar.text_input(
    "Chemin CSV historique",
    value="exports/tables/historique.csv"
)
actuel_path = st.sidebar.text_input(
    "Chemin CSV actuel",
    value="exports/tables/actuel.csv"
)

if st.sidebar.button("Lancer l'analyse"):
    agent = SismographeAgent(historique_path, actuel_path)
    synthese = agent.analyser()

    # ----------------------------------------------------------------
    # Synthèse CHOU / Copilot
    # ----------------------------------------------------------------
    st.subheader("Synthèse CHOU")
    copilot = CopilotInterface(synthese)
    st.markdown(copilot.interpretation())

    # ----------------------------------------------------------------
    # Visualisations statiques
    # ----------------------------------------------------------------
    st.subheader("Visualisations statiques")

    agent.visualiser_radar()
    agent.visualiser_courbes()
    agent.visualiser_heatmap()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Radar des indices**")
        st.image("exports/visualisations/radar.png")

    with col2:
        st.markdown("**Courbes historique vs actuel**")
        st.image("exports/visualisations/courbes.png")

    with col3:
        st.markdown("**Heatmap des variations**")
        st.image("exports/visualisations/heatmap.png")

    # ----------------------------------------------------------------
    # Visualisation interactive
    # ----------------------------------------------------------------
    st.subheader("Visualisation interactive (défilement + zoom)")

    fig = agent.lancer_visualisation_interactive()
    if fig is not None:
        plot_container = st.empty()
        plot_container.plotly_chart(fig, use_container_width=True)

        col_int1, col_int2, col_int3 = st.columns(3)

        with col_int1:
            if st.button("Interrompre le défilement"):
                agent.interrompre_defilement()

        with col_int2:
            st.markdown("**Zoom (indices)**")
            min_x = st.number_input("Min", min_value=0, value=0)
            max_x = st.number_input("Max", min_value=min_x + 1, value=min_x + 10)
            if st.button("Appliquer le zoom"):
                agent.definir_zoom(min_x, max_x)

        with col_int3:
            if st.button("Reprendre le défilement"):
                fig2 = agent.reprendre_defilement()
                if fig2 is not None:
                    plot_container.plotly_chart(fig2, use_container_width=True)

    # ----------------------------------------------------------------
    # Questions à Copilot
    # ----------------------------------------------------------------
    st.subheader("Questions à Copilot (lecture dialogique)")

    question = st.text_input("Pose une question sur les dynamiques, les ruptures, les fractales…")
    if question:
        reponse = copilot.dialoguer(question)
        st.markdown(reponse)
else:
    st.info("Configure les chemins CSV dans la barre latérale, puis clique sur « Lancer l'analyse ».")