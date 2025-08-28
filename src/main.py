import sys

from buttons import ButtonsGrid, Button
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':

    # Cria a Aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Definir o Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Button
    # button = ButtonsGrid()
    button = Button('Test')
    window.addToVLayout(button)

    # Grid
    # buttonsGrid = ButtonsGrid(display, info, window)
    # window.vLayout.addLayout(buttonsGrid)

    # Executa Aplicação
    window.adjustFixedSize()  
    window.show()
    app.exec()