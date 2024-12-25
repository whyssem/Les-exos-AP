
numbers = [1, 2, 3, 4, 5]

while True:
    
    index = int(input("Entrez l'index de l'élément à remplacer : "))
    
   
    if index == -1:
        break
    
   
    if 0 <= index < len(numbers):
        new_value = int(input("Entrez la nouvelle valeur : "))
        
        
        numbers[index] = new_value
        
        
        print("Liste mise à jour :", numbers)
    else:
        print("Index invalide. Essayez encore.")
