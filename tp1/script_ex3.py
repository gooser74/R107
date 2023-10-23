print ("Quel jour est-il?")
jour=int(input())
print ("Quelle heure est-il?")
heure=int(input())
print ("Quelles minutes est-il?")
minute=int(input())

total=jour*24*60+heure*60+minute

print ("Il s'est écoulé un total de", total, "minutes depuis le début du mois")

