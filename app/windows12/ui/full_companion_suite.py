"""
CHOU Full-Companion Suite
-------------------------

Suite complète du compagnon Windows 12 :
- dashboard
- widgets
- tiles
- guardian+
- orchestrator
- fractal engine
- stabilizer
- notifications
"""

from app.windows12.ui.system_orchestrator import SystemOrchestrator

class FullCompanionSuite:

    def __init__(self):
        self.orchestrator = SystemOrchestrator()

    def activer(self):
        return self.orchestrator.orchestrer()
