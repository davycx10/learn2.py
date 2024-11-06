class Player:
    
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur", self.pseudo, " /point d'attack: ", self.attack, " /points de vie", self.health)
        
    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack_value(self, target_player):
        return self.attack
    
    
    def damage(self, damage):
        self.health -= damage
        
    def attack_player(self, target_player):
        damage = self.attack  # L'attaque de base du joueur
        if self.has_weapon():
            damage += self.weapon.get_damage_amount()  # Si le joueur a une arme, on ajoute les dégâts de l'arme
        
        target_player.damage(damage)   
        
    def get_weapon(self):
        return self.weapon    
    
    def set_weapon(self, weapon):
        self.weapon = weapon  
        
    def has_weapon(self):
        return self.weapon is not None
                  