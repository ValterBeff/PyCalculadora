from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WITGH
from utils import isEmpty, isNumOrDot


# ============================
# Classe Display da Calculadora
# ============================
class Display(QLineEdit):
    # Sinais personalizados para a calculadora
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)
    negativePressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    # ============================
    # Configuração visual do display
    # ============================
    def configStyle(self):
        """Aplica fonte, tamanho, alinhamento e margens do display."""
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WITGH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    # ============================
    # Tratamento de eventos de teclado
    # ============================
    def keyPressEvent(self, event: QKeyEvent) -> None:
        """Interpreta teclas e emite sinais correspondentes."""
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        # Mapear teclas
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isNegative = key in [KEYS.Key_N]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, 
            KEYS.Key_Asterisk, KEYS.Key_P,
        ]

        # ============================
        # Teclas especiais
        # ============================
        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isNegative:
            self.negativePressed.emit(text)
            return event.ignore()

        if isOperator:
            # Transformar 'P' em operador de potência
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        # ============================
        # Inserção de números ou ponto
        # ============================
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
