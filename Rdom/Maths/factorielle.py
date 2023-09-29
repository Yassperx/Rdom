def factorielle(n: int) -> int:
    """
    Calcule la factorielle de n de manière récursive.
    """
    if n < 0:
        raise ValueError("La valeur de n doit être non négative.")
    
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
