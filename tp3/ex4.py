x = int(input("Entre 1 pour que le programme utilise une boucle while ou 2 pour qu'il utilise la boucle for: "))
n = int(input("Entrez un nombre dont vous voulez la factorielle:"))
a = 1

if x==1:
    print("Vous avez choisi la boucle while")
    while n !=1:
        a = a*n
        n -=1
        print(a)
    print("Voici votre nombre", a)

if x == 2:
    print("Vous avez choisi la boucle for")
    for i in range(1, n+1):
        a = a*i
        print(a)
    print("Voici votre nombre", a)
