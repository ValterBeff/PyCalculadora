from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import SMALL_FONT_SIZE


# ============================
# Classe Info (exibe informações)
# ============================
class Info(QLabel):
    """
    Widget para exibir mensagens ou status da calculadora.
    Herdado de QLabel.
    """

    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    # ============================
    # Configuração visual
    # ============================
    def configStyle(self):
        """Define fonte e alinhamento do texto."""
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
