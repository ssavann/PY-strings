'''
Gestion des espaces dans les chaines de caractères

methode : 

Strip 	> Supprimer les espaces en début et fin de chaine
lstrip	> left strip : supprimer l'espage de la gauche


'''

chaine = " Le Python c'est fantastique "

print("***" + chaine + "***")


chaine2 = " Le Python c'est fantastique "

print("***" + chaine2.strip() + "***")


chaine3 = " Le Python c'est fantastique "

print("***" + chaine3.lstrip() + "***")


chaine4 = " Le Python c'est fantastique "

print("***" + chaine4.strip().upper() + "***")








