from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
)

class MainWindow(QMainWindow):
    def __init__(self, parent : QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configuração do Layout Basíco
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
         
         # Titulo do Programa
        self.setWindowTitle('CALCULADORA')

    def adjustFixedSize(self):
            # Tamnho da Janela
            self.adjustSize()
            self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

