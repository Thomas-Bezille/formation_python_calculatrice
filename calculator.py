# CONSIGNE:
# créer une calculatrice en ligne de commande qui demande à l'utilisateur de saisir deux nombres
# et qui affiche ensuite le résultat de l'addition de ces deux nombres.

while True:
    nbr1 = input("Entrez un premier nombre: ")
    nbr2 = input("Entrez un deuxième nombre: ")
    
    if not nbr1.isnumeric() or not nbr2.isnumeric():
        print("Veuillez entrer des nombres entiers")
        continue
    else:
        result = int(nbr1) + int(nbr2)
        print(f"Le résultat de l'addition de {nbr1} et {nbr2} est: {result}")
        break