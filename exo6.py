prix = float(input("veuillez entrer le prix en dinars: "))
while prix < 0 :
    print ("le prix doit etre positif!")
    prix = float(input("veuillez entrer le prix en dinars: "))


dinars = int(prix)  
centimes = round((prix - dinars) * 100)  


print(f"Dinars: {dinars}")
print(f"Centimes: {centimes}")
