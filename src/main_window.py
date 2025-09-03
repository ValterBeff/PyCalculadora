from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QMessageBox
)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # ============================
        # Configuração do Layout Básico
        # ============================
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
         
        # ============================
        # Título do Programa
        # ============================
        self.setWindowTitle('CALCULADORA')

    # ============================
    # Ajusta a janela para tamanho fixo
    # ============================
    def adjustFixedSize(self):
        # Ajusta o tamanho da janela e fixa
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # ============================
    # Adiciona widget ao layout vertical
    # ============================
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    # ============================
    # Cria e retorna uma caixa de diálogo
    # ============================
    def makeMsgBox(self):
        return QMessageBox(self)
