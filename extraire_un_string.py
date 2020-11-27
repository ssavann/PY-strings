'''
Découper une chaine de caractère

[n<indice de départ> : <indice d'arrivé>]
[n:]    -> indice n ----> fin
[:n]    -> début ----> n
[n]     -> caractère indice n

'''

txt = "Hello world!"

print(txt[6])		#extraire sixième caractère "w"

print(txt[6:11])	#extraire à partir du sixième et onzième moins un

print(txt[6:])		#extraire à partir du sixième jusqu'à la fin

print(txt[:5])      #extraire tout ce qui est avant la cinquième caractère

print(txt[-5])      #extraire un seul caractère qui est avant la cinquième caractère


print(len(txt))     #compter le nombre de caractère dans la variable



for lettre in txt:  #afficher tous les lettres qui se trouve dans la variable
    print(lettre)


