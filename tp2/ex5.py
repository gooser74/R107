x = int(input("Donnez le nombre a vérifié : "))

if x<0 :
        if (x % 2) == 0:
            print(x,"Négatif et Pair")
        else :
            print(x, "Négatif et Impair")

elif x>0:
    if (x % 2) == 0:
        print(x,"Positif et Pair")
    else:
        print(x, "Positif et Impair")
else :
    print("Le nombre est zéro (et il est pair)")
