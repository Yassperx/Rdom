import matplotlib.pyplot as plt
import numpy as np

def syracuse(n):
    """Ploting the jumps of a number in syracuse operation"""
    n_values = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        n_values.append(n)
    return n_values

def plot_syracuse_sequence(a):
    """Ploting syracuse Sequence"""
    jumps = {}
    for i in range(1, a):
        plt.plot(syracuse(i), marker=".", lw=1, alpha=0.6, c='purple')
        jumps[i] = len(syracuse(i)) - 1

    plt.xlabel("Iterations")
    plt.ylabel("Syracuse Values")
    plt.title("Syracuse Sequence")
    x = np.ones(2 * a)
    plt.plot(x, lw=1, c='black')
    b = max(jumps, key=jumps.get)
    print(f"Biggest jump is {jumps[b]} for the number {b}.")
    plt.show()
