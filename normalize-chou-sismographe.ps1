# normalize-chou-sismographe.ps1
# Script de normalisation de l'arborescence CHOU-Sismographe

$root = "CHOU-Sismographe"

Write-Host "Normalisation de l'arborescence dans '$root'..." -ForegroundColor Cyan

# 1. Création des dossiers principaux
$dirs = @(
    "$root\data\raw",
    "$root\data\processed",
    "$root\data\metadata",
    "$root\logs\runs",
    "$root\logs\alerts",
    "$root\exports\reports",
    "$root\exports\tables",
    "$root\exports\visualisations",
    "$root\src\core",
    "$root\src\agents",
    "$root\src\utils",
    "$root\scripts",
    "$root\tests",
    "$root\app\android\api",
    "$root\app\android\ui",
    "$root\app\windows12\api",
    "$root\app\windows12\ui"
)

foreach ($d in $dirs) {
    if (-not (Test-Path $d)) {
        Write-Host "Création du dossier: $d"
        New-Item -ItemType Directory -Path $d | Out-Null
    }
}

# 2. Déplacement des fichiers core
$coreMoves = @(
    @{src="src\core\loader.py";        dst="$root\src\core\loader.py"},
    @{src="src\core\indices.py";       dst="$root\src\core\indices.py"},
    @{src="src\core\ruptures.py";      dst="$root\src\core\ruptures.py"},
    @{src="src\core\fractales.py";     dst="$root\src\core\fractales.py"},
    @{src="src\core\comparateur.py";   dst="$root\src\core\comparateur.py"}
)

foreach ($m in $coreMoves) {
    if (Test-Path $m.src) {
        Write-Host "Déplacement core: $($m.src) -> $($m.dst)"
        Move-Item $m.src $m.dst -Force
    }
}

# 3. Déplacement des agents
$agentMoves = @(
    @{src="src\agents\sismographe_agent.py";   dst="$root\src\agents\sismographe_agent.py"},
    @{src="src\agents\visualisation_agent.py"; dst="$root\src\agents\visualisation_agent.py"},
    @{src="src\agents\export_agent.py";        dst="$root\src\agents\export_agent.py"},
    @{src="src\agents\copilot_interface.py";   dst="$root\src\agents\copilot_interface.py"},
    @{src="src\agents\interpretation_ia.py";   dst="$root\src\agents\interpretation_ia.py"},
    @{src="src\agents\scheduler.py";           dst="$root\src\agents\scheduler.py"},
    @{src="src\agents\android_agent.py";       dst="$root\src\agents\android_agent.py"},
    @{src="src\agents\windows12_agent.py";     dst="$root\src\agents\windows12_agent.py"}
)

foreach ($m in $agentMoves) {
    if (Test-Path $m.src) {
        Write-Host "Déplacement agent: $($m.src) -> $($m.dst)"
        Move-Item $m.src $m.dst -Force
    }
}

# 4. Déplacement des utilitaires
$utilsMoves = @(
    @{src="src\utils\plotly_base.py";            dst="$root\src\utils\plotly_base.py"},
    @{src="src\utils\visualisation_interactive.py"; dst="$root\src\utils\visualisation_interactive.py"},
    @{src="src\utils\anomalies.py";             dst="$root\src\utils\anomalies.py"},
    @{src="src\utils\courbes.py";               dst="$root\src\utils\courbes.py"},
    @{src="src\utils\heatmap.py";               dst="$root\src\utils\heatmap.py"},
    @{src="src\utils\radar.py";                 dst="$root\src\utils\radar.py"},
    @{src="src\utils\timeline.py";              dst="$root\src\utils\timeline.py"},
    @{src="src\utils\sync.py";                  dst="$root\src\utils\sync.py"},
    @{src="src\utils\loader_wrapper.py";        dst="$root\src\utils\loader_wrapper.py"}
)

foreach ($m in $utilsMoves) {
    if (Test-Path $m.src) {
        Write-Host "Déplacement utilitaire: $($m.src) -> $($m.dst)"
        Move-Item $m.src $m.dst -Force
    }
}

# 5. Scripts
$scriptsMoves = @(
    @{src="scripts\sismographe.py"; dst="$root\scripts\sismographe.py"},
    @{src="scripts\visualisation.py"; dst="$root\scripts\visualisation.py"}
)

foreach ($m in $scriptsMoves) {
    if (Test-Path $m.src) {
        Write-Host "Déplacement script: $($m.src) -> $($m.dst)"
        Move-Item $m.src $m.dst -Force
    }
}

# 6. Tests
$testsMoves = @(
    @{src="tests\test_loader.py";     dst="$root\tests\test_loader.py"},
    @{src="tests\test_indices.py";    dst="$root\tests\test_indices.py"},
    @{src="tests\test_ruptures.py";   dst="$root\tests\test_ruptures.py"},
    @{src="tests\test_fractales.py";  dst="$root\tests\test_fractales.py"}
)

foreach ($m in $testsMoves) {
    if (Test-Path $m.src) {
        Write-Host "Déplacement test: $($m.src) -> $($m.dst)"
        Move-Item $m.src $m.dst -Force
    }
}

# 7. Android
$androidMoves = @(
    @{src="app\android\main.py";             dst="$root\app\android\main.py"},
    @{src="app\android\api\chou_api.py";     dst="$root\app\android\api\chou_api.py"},
    @{src="app\android\ui\android_app.py";   dst="$root\app\android\ui\android_app.py"}
)

foreach ($m in $androidMoves) {
    if (Test-Path $m.src) {
        Write-Host "Déplacement Android: $($m.src) -> $($m.dst)"
        Move-Item $m.src $m.dst -Force
    }
}

# 8. Windows 12
$winMoves = @(
    @{src="app\windows12\companion.py";      dst="$root\app\windows12\companion.py"},
    @{src="app\windows12\api\chou_api.py";   dst="$root\app\windows12\api\chou_api.py"}
)

foreach ($m in $winMoves) {
    if (Test-Path $m.src) {
        Write-Host "Déplacement Windows12: $($m.src) -> $($m.dst)"
        Move-Item $m.src $m.dst -Force
    }
}

# UI Windows12 (on déplace tout ce qui existe déjà)
if (Test-Path "app\windows12\ui") {
    Write-Host "Déplacement UI Windows12: app\windows12\ui\* -> $root\app\windows12\ui\"
    Move-Item "app\windows12\ui\*" "$root\app\windows12\ui\" -Force
}

Write-Host "`nNormalisation terminée. Vérifie avec :" -ForegroundColor Green
Write-Host "  tree $root /F"
