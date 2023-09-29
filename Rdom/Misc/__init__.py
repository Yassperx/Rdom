"""
Rdom Package
-------------
This package contains a collection of random projects and utilities 
including neural networks, mathematical functions, and miscellaneous utilities.
For more details, check the respective module documentation.
"""

# version of the Rdom package
__version__ = '0.1.0'

from .Misc import Ceaser_cipher, DFS, GroupAnagrams, Love_calc, Roman_Calc

# Other nice functions


def use(a, func):
    """
    Simplify printing function results.

    Args:
    - a : The input argument for the function.
    - func : The function to execute.

    Returns:
    - The result of the function execution.
    """
    result = func(a)
    print(result)
    return result

def tree():
    """
    Display the package and modules tree structure.
    """
    structure = """
    Rdom Package Structure:
    ├── DeepLearning
    │   ├── Neural_Network.py
    │   └── data.json
    ├── Maths
    │   ├── Conjecture_de_syracuse.py
    │   ├── Fibonacci.py
    │   ├── ReadPoly.py
    │   ├── Suites.py
    │   └── factorielle.py
    ├── Misc
    │   ├── Ceaser_cipher.py
    │   ├── DFS.py
    │   ├── GroupAnagrams.py
    │   ├── Love_calc.py
    │   ├── Roman_Calc.py
    │   └── Sorting.py
    └── __init__.py
    """
    print(structure)