def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral to its integer value.

    Args:
    - s (str): Roman numeral as string.

    Returns:
    - int: Integer representation of the Roman numeral.
    """
    number = 0
    ROMAN_MAP = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    prev_value = 0

    for char in s:
        current_value = ROMAN_MAP[char]
        if current_value > prev_value:
            number += current_value - 2 * prev_value
        else:
            number += current_value
        prev_value = current_value

    return number

def int_to_roman(num: int) -> str:
    """
    Convert an integer to its Roman numeral representation.

    Args:
    - num (int): Integer value.

    Returns:
    - str: Roman numeral representation of the integer.
    """
    VALUES = [
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    ]
    SYMBOLS = [
        "M", "CM", "D", "CD", "C", "XC", 
        "L", "XL", "X", "IX", "V", "IV", "I"
    ]

    roman_numeral = ''
    i = 0

    while num > 0:
        for _ in range(num // VALUES[i]):
            roman_numeral += SYMBOLS[i]
            num -= VALUES[i]
        i += 1

    return roman_numeral
