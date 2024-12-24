montanttotal = float(input("entrez le montant total svp! "))
nbArticle = int(input("quel est le nombre de vous article? "))
Jsemaine = input("dans quel jour sommes-nous? ")


       

if nbArticle > 5:
    totalApresReduction = montanttotal * 0.05 
    
    if Jsemaine == "samedi" or Jsemaine == "dimanche":
        totalApresReduction = montanttotal * 0.25
        totalApresReduction = montanttotal - totalApresReduction
        print("le prix total apres reduction est: " + str(totalApresReduction)) 
        

    else:
        print("le prix total apres reduction est: " + str(totalApresReduction))    

if nbArticle <= 5:

 if Jsemaine == "samedi" or Jsemaine == "dimanche":
     totalApresReduction = montanttotal * 0.2
     totalApresReduction = montanttotal - totalApresReduction
     print("le prix total apres reduction est: " + str(totalApresReduction))

 else:
    totalApresReduction = montanttotal * 0.1
    totalApresReduction = montanttotal - totalApresReduction
    print("le prix total apres reduction est: " + str(totalApresReduction))
