class Cars:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = 0 
        
    def get_marque(self):
        return self.marque
    
    def get_couleur(self):
        return self.couleur
    
    def get_rouler(self):
        self.vitesse += 100
        return self.vitesse
        
    def get_freiner(self):
        self.vitesse -= 10
        if self.vitesse <= 0:
            self.vitesse = 0
            return self.vitesse            
        