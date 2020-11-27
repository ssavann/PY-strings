'''
Suppression ou remplacement de caractère

replace()	Pour supprimer les caractères


'''


phrase = "L'assembleur c'est facile à apprendre, pas comme le Python."
phrase = phrase.replace(", pas comme le Python" , "")

print(phrase)



phrase2 = "L'assembleur c'est facile à apprendre."
phrase2 = phrase2.replace("L'assembleur", "Le python")

print(phrase2)