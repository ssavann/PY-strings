'''
Gestion de la casse

upper()		   Majuscule
lower()		   Minuscule
capitalize()   Premier mot commence en majuscule
title()        Chaque mot commence par une majuscule 

isupper()      True si chaine en majuscule
islower()      True si chaine en minuscule
'''

phrase = "Le python est fantastique."

print(phrase.upper())


phrase2 = "LE PYTHON EST FANTASTIQUE."

print(phrase2.lower())


phrase3 = "LE PYTHON EST FANTASTIQUE."

print(phrase3.capitalize())


phrase4 = "LE PYTHON EST FANTASTIQUE."

print(phrase4.title())



phrase5 = "LE PYTHON EST FANTASTIQUE."
if phrase5.isupper():
    print("C'est en majuscule")


phrase6 = "le python est fantastique."
if phrase6.islower():
    print("C'est en minuscule")



