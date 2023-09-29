import random as rd

def love_cal(nom1: str, nom2: str) -> None:
    """
    Simule un calculateur d'amour qui détermine le pourcentage d'amour entre 
    deux noms donnés en entrée en utilisant un générateur de nombres aléatoires.

    Le programme continue de générer des pourcentages jusqu'à ce qu'il atteigne 
    100%, où il affiche "Jackpot!" et le nombre d'essais nécessaires pour atteindre ce résultat.

    Args:
    - nom1 (str): Premier nom à tester.
    - nom2 (str): Deuxième nom à tester.

    Returns:
    - None
    """
    
    count = 0
    pourcentage = rd.randint(0, 100)

    # La boucle while tourne jusqu'à ce que pourcentage soit égal à 100
    while pourcentage != 100:
        pourcentage = rd.randint(0, 100)
        count += 1
         
        print(nom1 , "+", nom2, "=", pourcentage , "%")

    # Affichage lorsque le pourcentage atteint 100%
    print("Jackpot!")
    print(nom1 , "+", nom2, "=",  pourcentage , "%")
    print(count, "essais !")
