def U(start: int, end: int, func) -> list:
    """
    Génère une suite à l'aide d'une fonction personnalisée.
    """
    return [func(i) for i in range(start, end)]

def a_U(r: float, start=0, end=5) -> list:
    """
    Génère une progression arithmétique.
    """
    return U(start, end, lambda i: start + r * i)

def g_U(p: float, start=0, end=5) -> list:
    """
    Génère une progression géométrique.
    """
    return U(start, end, lambda i: 1 * p**i)
