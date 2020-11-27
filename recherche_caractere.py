'''
indice (position du caractère):

0 1 2 3 4 5 6 7 8 9 10
H e l l o   w o r l d

Méthode:

index()
find()
count()
startswith()
endswith()


'''

chaine = "Hello world"

print(chaine.index("o"))	#le "o" est à la position 4

print(chaine.index("w"))	#le "o" est à la position 6

print(chaine.find("z"))		#recherche le "z" dans la chaine: -1 n'a pas trouvé


print(chaine.find("r"))		#recherche le "z" dans la chaine: -1 n'a pas trouvé

print(chaine.count("o"))	#compte le nombre de "o" dans la chaine:  trouvé 2

print(chaine.count("world"))	#compte le nombre de "world" dans la chaine:  trouvé 1

print(chaine.startswith("world"))	#si ça démarre avec le mot "world" :  False

print(chaine.startswith("Hello"))	#si ça démarre avec le mot "Hello" :  True


print(chaine.endswith("world"))   #si ça termine avec le mot "world" :  True







