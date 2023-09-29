def read(polynomial: list) -> str:
    """
    Convertit une liste de coefficients en une représentation sous forme de chaîne de caractères du polynôme.
    """
    p_r = []
    c = len(polynomial) - 1
    for coeff in polynomial:
        if coeff == 0:
            c -= 1
            continue
        if c == len(polynomial) - 1:
            term_str = f"{coeff}x^{c}" if c > 1 else f"{coeff}x" if c == 1 else f"{coeff}"
        else:
            if coeff < 0:
                term_str = f" - {-coeff}x^{c}" if c > 1 else f" - {-coeff}x" if c == 1 else f" - {-coeff}"
            else:
                term_str = f" + {coeff}x^{c}" if c > 1 else f" + {coeff}x" if c == 1 else f" + {coeff}"
        p_r.append(term_str)
        c -= 1
    return ''.join(p_r)
