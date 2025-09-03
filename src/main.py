import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

# Importações dos módulos do projeto
from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # ============================
    # Criação da Aplicação
    # ============================
    app = QApplication(sys.argv)

    # Aplicar tema customizado
    setupTheme(app)

    # Criar janela principal
    window = MainWindow()

    # ============================
    # Configurar ícone da aplicação
    # ============================
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # ============================
    # Adicionar widget de informações
    # ============================
    info = Info('')  # Pode ser usado para mensagens ou status
    window.addWidgetToVLayout(info)

    # ============================
    # Adicionar display da calculadora
    # ============================
    display = Display()
    window.addWidgetToVLayout(display)

    # ============================
    # Adicionar grid de botões
    # ============================
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # ============================
    # Ajustar tamanho da janela e executar
    # ============================
    window.adjustFixedSize()
    window.show()
    app.exec()
