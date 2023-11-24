import random

x = random.randint(0, 100)
nombre_tours = 0
nombre_saisi = None

while nombre_saisi != x:
    nombre_saisi = int(input("Entrez un nombre entre 0 et 100: "))
    nombre_tours += 1
    if nombre_saisi > x:
        print("Le nombre saisi est plus grand que x.")
    elif nombre_saisi < x:
        print("Le nombre saisi est plus petit que x.")
    else:
        print("Bravo, vous avez trouvé le nombre mystère!")

print(f"Le nombre mystère était {x}.")
print(f"Il a fallu {nombre_tours} tours pour le deviner.")