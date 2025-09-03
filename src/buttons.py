import math
from typing import TYPE_CHECKING
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber, converToNumber

if TYPE_CHECKING:
    from display import Display
    from main_window import MainWindow
    from info import Info


# ============================
# Classe Button personalizada
# ============================
class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        """Configura o estilo do botão (tamanho e fonte)."""
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


# ============================
# Grid de botões da calculadora
# ============================
class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow',
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Máscara do grid (texto dos botões)
        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window

        # Estado da operação
        self._equation = ''
        self._equationInitialValue = ' '
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue

        # Criar grid de botões
        self._makeGrid()

    # ============================
    # Propriedade para atualizar o display de info
    # ============================
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    # ============================
    # Montagem do grid e conexão de sinais
    # ============================
    def _makeGrid(self):
        # Conectar sinais do display
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._inserToDisplay)
        self.display.operatorPressed.connect(self._configLeftOP)
        self.display.negativePressed.connect(self._invertNumber)

        # Criar botões
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                # Configurar botões especiais
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                # Adicionar botão ao grid
                self.addWidget(button, i, j)
                slot = self._makeSlot(self._inserToDisplay, buttonText)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        """Conecta um botão a um slot."""
        button.clicked.connect(slot)

    # ============================
    # Configuração de botões especiais
    # ============================
    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)
        elif text == 'D':
            self._connectButtonClicked(button, self.display.backspace)
        elif text == 'N':
            self._connectButtonClicked(button, self._invertNumber)
        elif text == '=':
            self._connectButtonClicked(button, self._eq)
        elif text in '+-/*^':
            self._connectButtonClicked(button, self._makeSlot(self._configLeftOP, text))

    # ============================
    # Criar um slot dinâmico
    # ============================
    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    # ============================
    # Inverter o sinal do número
    # ============================
    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            return
        number = converToNumber(displayText) * -1
        self.display.setText(str(number))

    # ============================
    # Inserir valor no display
    # ============================
    @Slot()
    def _inserToDisplay(self, text):
        newDisplayValue = self.display.text() + text
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(text)
        self.display.setFocus()

    # ============================
    # Limpar operação
    # ============================
    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    # ============================
    # Configurar número esquerdo e operador
    # ============================
    @Slot()
    def _configLeftOP(self, text):
        displayText = self.display.text()
        self.display.clear()
        self.display.setFocus()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('Ausência do valor inicial')
            return

        if self._left is None:
            self._left = converToNumber(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    # ============================
    # Executar operação
    # ============================
    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Ausência do valor final')
            return

        self._right = converToNumber(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, (int, float)):
                result = math.pow(self._left, self._right)
                result = converToNumber(str(result))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero')
            result = 'None'
        except OverflowError:
            self._showError('Conta não efetuada')

        self.display.clear()
        self.info.setText(f'{result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result != 'error':
            self._left = None

    # ============================
    # Backspace
    # ============================
    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    # ============================
    # Caixa de diálogo
    # ============================
    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
