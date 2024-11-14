import os
from random import *

if os.path.exists("meals.txt"):
    with open("meals.txt", "r") as file :
        meals_list = file.readlines()
        meals_list = [meal.strip() for meal in meals_list]
        
        if meals_list:
            meals_random_choice = random.choice(meals_list)
            print(f"je vous popose comme repas aurjourd'hui: {meals_random_choice}")
        else:
            print("le fichier est vide aucun repas à proposer")
            
else:
    print("le fichier n'existe pas! attention !!")    