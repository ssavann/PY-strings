'''
Méthode:

split()		scinder, espace si pas délimiteur
join()		joindre des caractères


'''


prenoms = " Luc Paul Lana Loic Aurelie"

lst_prenom = prenoms.split(",")		#avec délimiteur
print(lst_prenom)

lst_prenom = prenoms.split()		#sans délimiteur
print(lst_prenom)



chaine = " ".join(lst_prenom)
print(chaine)

chaine = "-".join(lst_prenom)
print(chaine)


chaine2 = "1 2 3 4 5 6 7 8 9"
print(chaine2.partition("4"))	#"4" est mon délimiteur





