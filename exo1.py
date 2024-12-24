prixoneticket=15.33
nom = input("Entrez votre nom : ")

if nom == "VIP" or "vip":
    print("voila votre ticket, profitez du spectacle!")

else:
    n = int(input("combien de tickets souhaitez vous en acheter? "))
    cout = n * prixoneticket
print("voila le cout total " + str(cout) + "DA" )
