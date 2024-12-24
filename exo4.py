age1 = int(input("entrez votre age s'il vouss plait? "))
age2 = int(input("entrez votre age s'il vous plait? "))

if age1 == age2 :
    print("vous avez le meme age!")

if age1 > age2 : 
    print("la personne la plus agee est celle avec l'age de " +str(age1))
else:
    print("la personne la plus agee est celle avec l'age de " +str(age2))