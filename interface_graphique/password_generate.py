from tkinter import *
from PIL import Image, ImageTk
import string
from random import *


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
        

#créer une fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.config(background="#10b9da")

#créer la frame de principale
frame = Frame(window, bg="#10b9da")


#création de l'image avec Pillow
image_path = '/home/disrael/Downloads/hellsing.jpeg'

image = Image.open(image_path)
image = image.resize((300, 300))  # Redimensionner l'image
photo = ImageTk.PhotoImage(image)  # Convertir l'image pour Tkinter

# Créer un canvas pour afficher l'image
canvas = Canvas(frame, width=300, height=300, bg="#10b9da", bd=0, highlightthickness=0)
canvas.create_image(150, 150, image=photo)  # Placer l'image au centre du canvas
canvas.grid(row=0, column=0, sticky=W)

#créer une sous boite
right_frame = Frame(frame, bg="#10b9da")

#créer une nouvelle instance (titre)
label_title = Label(right_frame, text="mot de passe", font=("Helvetica", 20), bg="#10b9da", fg="white")
label_title.pack()

#créer un champs/entrée/input
password_entry = Entry(right_frame, text="mot de passe", font=("Helvetica", 20), bg="#10b9da", fg="white")
password_entry.pack()

#créer un bouton
generate_password_button = Button(right_frame, text="générer", font=("Helvetica", 20), bg="#10b9da", fg="white", command=generate_password)
generate_password_button.pack(fill=X)

#on place la sous boite à droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)


#afficher la frame
frame.pack(expand=YES)

#création d'une barre de menu
menu_barre = Menu(window)

#créer un premier menu
file_menu = Menu(menu_barre, tearoff=0)
file_menu.add_command(label="nouveau", command=generate_password)
file_menu.add_command(label="Quit", command=window.quit)
menu_barre.add_cascade(label="fichier", menu=file_menu)

#configurer notre fenetre pour ajouter cette menu bar
window.config(menu=menu_barre)



#afficher la fenetre
window.mainloop() 
