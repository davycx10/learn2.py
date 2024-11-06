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