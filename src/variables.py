from pathlib import Path

# ============================
# Diretórios e arquivos do projeto
# ============================
ROOT_DIR = Path(__file__).parent       # Diretório raiz do projeto
FILES_DIR = ROOT_DIR / 'files'         # Pasta de arquivos (ícones, etc.)
WINDOW_ICON_PATH = FILES_DIR / 'icon.png'  # Caminho do ícone da janela

# ============================
# Cores principais da aplicação
# ============================
PRIMARY_COLOR = "#b01e1e"        # Cor primária dos botões
DARKER_PRIMARY_COLOR = "#8a1616" # Cor do botão em hover
DARKEST_PRIMARY_COLOR = "#701111" # Cor do botão pressionado

# ============================
# Tamanhos e margens
# ============================
BIG_FONT_SIZE = 40      # Fonte do display
MEDIUM_FONT_SIZE = 24   # Fonte dos botões
SMALL_FONT_SIZE = 18    # Fonte de informações
TEXT_MARGIN = 15        # Margem interna do display
MINIMUM_WITGH = 500     # Largura mínima da janela
