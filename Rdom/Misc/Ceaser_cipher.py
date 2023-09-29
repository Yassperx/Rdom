# Constantes globales
ABC_LOWER = "abcdefghijklmnopqrstuvwxyz"
ABC_UPPER = ABC_LOWER.upper()

def save_state(text: str) -> list:
    """
    Sauvegarde l'état de casse de chaque caractère dans une liste.
    Les minuscules sont représentées par 0, les majuscules par 1 et les non-alphabétiques par -1.
    """
    return [0 if char in ABC_LOWER else 1 if char in ABC_UPPER else -1 for char in text]

def apply_state(text: str, states: list) -> str:
    """
    Applique un état de casse à une chaîne de caractères.
    """
    return ''.join([char.lower() if state == 0 else char.upper() if state == 1 else char for char, state in zip(text, states)])

def ceaser_cipher(text: str, shift: int = 1) -> str:
    """
    Code ou décode une chaîne de caractères en utilisant le codage de César.
    """
    states = save_state(text)
    ciphered_text = []

    for char in text.lower():
        if char in ABC_LOWER:
            index = (ABC_LOWER.index(char) + shift) % 26
            ciphered_text.append(ABC_LOWER[index])
        else:
            ciphered_text.append(char)

    return apply_state(''.join(ciphered_text), states)

