BASE = 4
fromage = 800.00
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne conviés à la fondue :"))
fromage = 800.00 * nbConvives / BASE
eau = 2 * nbConvives / BASE
ail = 2 * nbConvives / BASE
pain = 400 * nbConvives / BASE

print("Pour faire faire une fondue fribourgeoise pour:" ,nbConvives, "il vous faut : \n-", fromage, "gr de fromage" "\n-", eau, "dl d'eau" "\n-", ail, "gousses d'ail" "\n-", pain, "gr de pain")
