runner1 = input("quel est le nom de la premiere condidate? ")
tmp1 = int(input("quel est le temps de course pour la premiere condidate? "))

while tmp1 <= 0 :
    print("le temps doit etre positif! ")
    tmp1 = int(input("quel est le temps de course pour la premiere condidate? "))

runner2 = input("quel est le nom de la deuxieme condidate? ")
tmp2 = int(input("quel est le temps de course pour la deuxieme condidate? "))

while tmp2 <= 0 :
    print("le temps doit etre positif! ")
    tmp2 = int(input("quel est le temps de course pour la deuxieme condidate? "))



if tmp1 > tmp2 :
    print("the faster runner is: " + runner1)
    
if tmp2 > tmp1 :
    print("the faster runner is: " + runner2)

if tmp1 == tmp2 :
    print( runner1 + " and " + runner2 + " have the same time")
