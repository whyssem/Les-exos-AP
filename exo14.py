
chaine = input("Veuillez entrer une chaîne de caractères : ")

largeur_cadre = 30


espaces_totaux = largeur_cadre - len(chaine)
espaces_gauche = espaces_totaux // 2
espaces_droite = espaces_totaux - espaces_gauche


print("*" * largeur_cadre)  
print("*" + " " * (largeur_cadre - 2) + "*")  
print("*" + " " * espaces_gauche + chaine + " " * espaces_droite + "*")  
print("*" + " " * (largeur_cadre - 2) + "*")  
print("*" * largeur_cadre)  
