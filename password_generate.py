from tkinter import *
from PIL import Image, ImageTk

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
generate_password_button = Button(right_frame, text="générer", font=("Helvetica", 20), bg="#10b9da", fg="white")
generate_password_button.pack(fill=X)

#on place la sous boite à droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)


#afficher la frame
frame.pack(expand=YES)



#afficher la fenetre
window.mainloop()