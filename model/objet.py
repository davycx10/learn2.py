from model.player import *
from model.Weapon import *
         
knife = Weapon("couteau", 5)                  
player1 = Player("Graven", 20, 3)
player2 = Player("davycx", 20, 5)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())



print("Bienvenue au joueur", player1.get_pseudo(), " /point d'attack: ", player1.get_attack(), " /points de vie", player1.get_health())
print("Bienvenue au joueur", player2.get_pseudo(), " /point d'attack: ", player2.get_attack(), " /points de vie", player2.get_health())

print("")



#def base():
    #taille = 0
    #séquence = 1
    #séquence += taille
    #print(base)
    #taille += 1 
    #print(séquence)

#week_day = [ "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche" ]
#print(week_day[0:5])
#print(week_day[5:])
#print(len(week_day))
#print(week_day[3])

#hiver = ["janvier", "février", "mars"]
#printemps = ["avril", "mai", "juin"]
#été = ["juillet", "aout", "septembre"]
#automne = ["octobre", "novembre", "décembre"]
#saison1 = ["hiver", "printemps", "été", "automne"]
#print(saison1[0] [2])
#print(hiver[2])
 
#color = [ "dark", "gray", "red" ]
#for i in range(len(color)):
 #   print(f"la couleur {i} est {color[i]} ")
 


#liste = ["vache", "souris", "levure", "bactéries"]
#a = 0
#while a <=3:
    #print(liste[a])
    #a = a + 1
    
    
#for a in range(len(liste)):
#    print(f"la l'élément {a} dans la liste est {liste[a]}")
#   #print(a#)


#day = [ "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche" ]
#for d in day:
#    print(d)
#    if d == "vendredi":
#        break
#print()
#    
#da = 5
#while da <= 6:
#    print(day[da])    
#    da = da + 1
    
    
#def moyenne (a,b,c,d,e):
#    return(a+b+c+d+e)/5
#moyenne(14,9,12,6,8)
##print(f" le moyenne de l'étudiant est de {moyenne(14,9,12,6,8):.2f}") 

#saut = 0
#while saut <= 5:
#    print(saut)
#    saut = saut + 1

#nombres = (4, 5, 6)
#for nb in nombres:
#    if nb == 5:
#        print(f"le test est vrai")
#        print(f"car la variable nb vaut {nb}")
#

#x = 2 
#y = 5
#if x == 2 and y == 2:
#    print("le test est vrai")  
#else:
#    print("le test est faux")

#def moyenne(a,b,c):
#    return (a+b+c)/3
#moyenne(13.75,10,12.50)
##print(moyenne(14, 10, 13))
#print(f"ma moyenne est de {moyenne(13.75,10,12.50):.2f}")    