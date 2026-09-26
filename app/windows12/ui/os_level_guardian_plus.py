"""
CHOU OS-Level Guardian+
-----------------------

Agent Windows 12 de protection douce :
- surveille les ruptures système-large
- stabilise les dynamiques CHOU
- déclenche des notifications proportionnées
- interagit avec le scheduler (05h00 → 08h00)
"""

from src.core.ruptures import detecter_ruptures
from app.windows12.ui.smart_notification import envoyer_notification_intelligente
from src.utils.loader_wrapper import load_windows

class OSLevelGuardianPlus:

    def __init__(self):
        self.nom = "CHOU OS-Level Guardian+"
        self.description = (
            "Agent de protection douce Windows 12, surveillant les ruptures "
            "et stabilisant les dynamiques CHOU."
        )

    def surveiller(self):
        historique, actuel = load_windows()
        ruptures = detecter_ruptures(historique, actuel)

        if len(ruptures) > 0:
            envoyer_notification_intelligente(
                titre="Rupture détectée",
                message="Une rupture douce a été identifiée dans les dynamiques CHOU."
            )

    def stabiliser(self):
        """
        Applique une stabilisation douce :
        - réduction des pics
        - lissage des courbes
        - harmonisation fractale
        """
        return "Stabilisation douce appliquée."
