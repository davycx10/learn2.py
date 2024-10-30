just_prize = 10000
request = 0

while request != just_prize:
    print(f"choisir un nombre entre 1 et 10000, {request}")
    request = int(input("entrer un prix: "))
    
    if request == just_prize:
        print(f"c'est gagné le juste prix était {just_prize}")
    else:
        request != just_prize
        print("c'est plus") or print("c'est moins")

























































# utilisation de la boucle for : pour une valeur de départ, jusqu'à une valeur d'arrivée
#for num_client in range(1, 6):
#    print(f"Vous ếtes le client n°{num_client}")
    
# for each : pour chaque valeur d'une liste données    
#
#emails = ["dave.israel@gmail.com", "graven@gmail.com", "davycx@gmail.com"]
#
## pour chacunes des valeurs, j'affiche email envoyé à 
#for email in emails:
#    print("Email envoyé à :", email)

#while : tant qu'une condition est vrai
#salarié qui oerçoit 1500€

# un youtubeur "gravinon", 2500 abonnées
#il gagne 10% d'audience supplémentaire par mois
#on souhaite estimer, combien aura t'il d'abonnes, après 2 ans

#suscribers_count = 2500
#
#months = 0
#
#while months <= 24:
#    suscribers_count *= 1.10
#    print(f"vous avez actuellement {suscribers_count:.0f} d'abonnés")
#    months+= 1
    

    
























#from random import shuffle
 
#chaine = input("donner une chaine de la forme (mot1/mot2/mot3/mot4): ").split("/")
#print(chaine)
#shuffle(chaine)
#print(chaine)

#if len(chaine) < 10:
#    print(f" les deux premier chaine de caractère de cette liste sont: {chaine[0]}, {chaine[1]}")
#else:
#    len(chaine) >= 10
#    print(f"les trois dernier chaine de caractère de cette liste sont: {chaine[7:]}")    

 
 
 
#génarateur de phrases
#demander en console une chaine de la forme mot1/mot2/mot3/mot4 ...
# transformer cette en une liste
#mélanger la liste
#si le nombre d'éléments de cette liste est inférieur à 10 -> afficher que les 2 premier mot
# si le nombre d'éléments de cette liste est supérieur ou égal à 10 -> afficher les 3 dernier mots



































#text = input("entrer une chazine de caractère de la forme (email-pseudo-mdp) ").split("-")
#print(text)
#print(f"salut {text[1]}, ton email est {text[0]}, et ton mot de passe est {text[2]}")





#from statistics import mean
#import random

# exemple jeux du professeur

#notes = [
#    8, 12, 10, 16,
#    9, 20, 4, 15, 
#    ]
#print(notes)

##module statistics
#result = mean(notes)
#print(f"la moyenne de l'élève est de {result}")














#créer une liste vas stocker des pseudos pour simuler un jeu en ligne
#
#online_players =  ["davycx", "Lounart", "overlord"]
#
##modifier 'davycx' -> 'davycx10'
#online_players[0] = "davycx10"
#online_players [2:] = ["Jack", "Scorpio"]
#online_players.insert(2, "over")
#online_players.append("hellsing")
#online_players.extend(["Gomui", "Aroke", "ieuze", "march"])
##del online_players[1]
#online_players.clear()
#print(online_players)
#
#que le joueur lournart se déconnecte

##online_players.
#online_players.clear()
















# place de cinéma
#age_user = int(input("Quel est votre âge ? "))
#po_request= input("souhaitez-vous du pop corn ? ")

            
#if age_user < 18:
#    cost = 7
#    print(f"la place de cinéma vous couteras {cost}€ car vous avez {age_user}ans")
    
#elif  po_request == "yes":
#    cost_with_pop = cost + 5
#    print(cost_with_pop)  
      
#else:
#    cost = 12
#    print(f"la place vous couteras {cost}€ car vous avez {age_user}ans")
    
#if po_request == "yes":
#    cost += 5
#    print(f"le prix total vous feras {cost}€ car vous avez demander du pop corn")
    
#else:
#    po_request != "yes"
#    print(f"le prix total vous feras {cost}€ car vous ne souhaitez pas de pop corn")    





#password = input("Entrer votre mot de passe: ")
#password_length = len(password)
#print(password_length)
#
##vérifier que le mot de passe est inférieur à 8 caractères
#
#if password_length <= 8:
#    print("mot de passe trop court")
#elif 8 < password_length < 12:
#    print("mot de passe moyen")    
#else:
#    print("mot de passe parfait")    





















#def main():
#    
#    
#    wallet = int(input("quel est la valeur de votre porte monnaie: "))
#    produit = 50
#    result = (wallet - produit)
#    print(f"après votre achat, voici la nouvelle valeur de votre porte monnaie {result}€")
    
#    #note1 = int(input("Donnez la première note "))
#    #note2 = int(input("Donnez la seconde note "))
#    #note3 = int(input("Donnez la derniere note "))
#    #result = int((note1 + note2 + note3) / 3)
#    #print(f" votre moyenne est de : {result:.2f}")
##def moyenne(a, b ,c):
##    return (a + b + c)/3
##moyenne(13.75, 10, 12.50)
##print(moyenne(13.75, 10, 12.50))
    
    
    
#    # création d'une variable 'username' dans lequel on affecte la valeur Dave 
#    #username = "Dave"
#    #creation d'une variable 'age' dans lequel on affecte la valeur 19
#    #age = 19
#    #création d'une variable 'wallet' dans lequel on affecte la valeur 12.7
#    #wallet = 12.7
#    #print(f"Salut {username}, tu as {age}ans et il te reste {wallet}€ dans ton portefeuille")

##    print("hello world")   
    
#if __name__ == '__main__':
#   main()     
    
    
    
    