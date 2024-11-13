from tkinter import *
from PIL import Image, ImageTk

class Cookies:
    
    def __init__(self):
        
        self.window = Tk()
        self.window.title("Cookie clicker")
        self.window.geometry("720x480")
        self.window.config(background="#950101")
        
        #intialisation d'une boite
        self.frame = Frame(self.window, bg="#950101") 
        self.frame.pack(expand=YES)
        
        #initialisation d'une sous boite
        self.right_frame = Frame(self.frame, bg="#950101")
        self.right_frame.pack(side="right", anchor="w") #frame à droite de la frame principale
        
        self.left_frame = Frame(self.frame, bg="#950101") #frame a gauche de la frame principale
        self.left_frame.pack(side="left", anchor="e")
        
        self.cout_click = 0
        
        self.count_label = Label(self.left_frame, text=str(self.cout_click), font=("Helvetica", 25), bg="#950101", fg="black")
        
        # création des composant de l'interface 
        self.create_widgets()
        
        #création des composant de l'image
        self.picture_widget()
        
        #creation d'un composant button
        self.button_click()
        
        #création d'un composant qui ajout +1 a chaque fois que on clique sur le button
        self.count_click()
        
        #création d'un composant qui affiche le score de clique
        self.click_score()
        
    def picture_widget(self):
        
        image_path = '/home/disrael/Downloads/cookies-internet.png'

        image = Image.open(image_path)
        image = image.resize((200, 200))  # Redimensionner l'image
        photo = ImageTk.PhotoImage(image)    
        
        self.image_label = Label(self.frame, image=photo)
        self.image_label.image = photo  # Sauvegarde une référence à l'image
        self.image_label.pack(side="top", anchor="w")
       
    # création des composant de l'interface 
    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
    
    
    def create_title(self):
        label_title = Label(self.frame, text="Cookie", font=("Arial", 30),  bg="#950101", fg="white")
        label_title.pack()
        
    def create_subtitle(self):
            label_subtitle = Label(self.right_frame, text="click", font=("Arial", 25),  bg="#950101", fg="white")
            label_subtitle.pack()         
        
        
    def count_click(self):
        self.cout_click += 1
        self.count_label.config(text=str(self.cout_click)) #change count_click en str
        self.count_label.pack()
          
        
        
    def button_click(self):
        button_click = Button(self.right_frame, text="cliquer", font=("Helvetica", 15), bg="#950101", fg="white", command=self.count_click)
        button_click.pack(fill=X)    
    
    def click_score(self):
        label_score = Label(self.left_frame, text="nombre", font=("Arial", 25),  bg="#950101", fg="white")
        label_score.pack()         



app = Cookies()
app.window.mainloop()