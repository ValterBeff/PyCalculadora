import re

# ============================
# Expressão regular para números ou ponto
# ============================
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

# ============================
# Função para verificar se é número ou ponto
# ============================
def isNumOrDot(string: str):
    """Retorna True se a string for um dígito ou ponto '.'"""
    return bool(NUM_OR_DOT_REGEX.search(string))

# ============================
# Função para converter string em número
# ============================
def converToNumber(string: str):
    """
    Converte string em float ou int.
    Se o número for inteiro, retorna int.
    """
    number = float(string)

    if number.is_integer():
        number = int(number)
    return number

# ============================
# Função para verificar se string é um número válido
# ============================
def isValidNumber(string: str):
    """
    Retorna True se a string puder ser convertida para float.
    Caso contrário, retorna False.
    """
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        ...
    return valid

# ============================
# Função para verificar se string está vazia
# ============================
def isEmpty(string: str):
    """Retorna True se a string estiver vazia."""
    return len(string) == 0
