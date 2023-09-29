def fibonacci_numbers(n: int) -> list:
    """
    Retourne une liste contenant les nombres de Fibonacci jusqu'à n.
    """
    fib_sequence = []
    a, b = 0, 1
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
