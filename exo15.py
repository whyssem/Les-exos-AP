

chaine = input("Veuillez entrer une chaîne de caractères (en minuscules) : ")


voyelles = "aeo"

for voyelle in voyelles:
    if voyelle in chaine:
        print(f"La voyelle '{voyelle}' est présente dans la chaîne.")
    else:
        print(f"La voyelle '{voyelle}' n'est pas présente dans la chaîne.")
