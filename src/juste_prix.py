from random import *

just_prize = randint(0, 1000)
request = 0
count_try = 2

while request != just_prize :
    count_try -= 1
    print(f"choisir un nombre entre 1 et 10000, {request}")
    request = int(input("entrer un prix: "))
    
    if count_try == 0:
        print(f"vous avez perdu, le juste prix était  {just_prize}")
        break
    else:
        print(f"il vous reste {count_try}, d'essaie")
    
    if request == just_prize:
        print(f"c'est gagné le juste prix était {just_prize}")
        
    elif request < just_prize:
        print("c'est plus")
        
    else:
        print("c'est moins")