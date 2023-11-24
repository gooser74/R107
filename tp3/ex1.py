print("Quel est votre nombre?")
n = int(input())
s = 0
while n > 0:
    s += n
    n = n - 1
print(s)

#

x = 0
while x != 100:
    print("Entrez un nombre")
    x =int(input())


#

def read_values():
    values = []
    for i in range(10):
        value = float(input(f"Entrez la valeur {i+1} : "))
        while value < 0 or value > 20:
            print("La valeur doit être comprise entre 0 et 20.")
            value = float(input(f"Entrez la valeur {i+1} : "))
        values.append(value)
    return values

def analyze_values(values):
    count_below_10 = 0
    count_below_15 = 0
    count_above_15 = 0

    for value in values:
        if value < 10:
            count_below_10 += 1
        elif value < 15:
            count_below_15 += 1
        else:
            count_above_15 += 1

    return count_below_10, count_below_15, count_above_15

def print_results(count_below_10, count_below_15, count_above_15):
    print("Résultats :")
    print(f"- Nombre de valeurs inférieur à 10 : {count_below_10}")
    print(f"- Nombre de valeurs supérieur ou égale à 10 et inférieur à 15 : {count_below_15}")
    print(f"- Nombre de valeurs supérieur ou égale à 15 : {count_above_15}")

values = read_values()
count_below_10, count_below_15, count_above_15 = analyze_values(values)
print_results(count_below_10, count_below_15, count_above_15)

#


z = int(input("Entrez la valeur de X: "))
M = 0
while M*(M+1)/2 <= z:
    M += 1
print("Le nombre M recherché est:", M-1)
