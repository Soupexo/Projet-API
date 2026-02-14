import requests
import tkinter as tk
from tkinter import Frame, Label, Button
from PIL import Image, ImageTk
from io import BytesIO

# ---------------------------
# VARIABLES
# ---------------------------

score_gauche = 0
score_droite = 0
total = 0

photo1 = None
photo2 = None

# ---------------------------
# FONCTIONS
# ---------------------------

def plat_aleatoire():

    global plat1, plat2

    url = "https://www.themealdb.com/api/json/v1/1/random.php"

    try:
        reponse1 = requests.get(url, verify=False)
        reponse2 = requests.get(url, verify=False)

        if reponse1.status_code == 200 and reponse2.status_code == 200:

            plat1 = reponse1.json()['meals'][0]
            plat2 = reponse2.json()['meals'][0]

            affiche_plat()

    except:
        titre.config(text="Erreur connexion API", fg="red")


def affiche_plat():

    global photo1, photo2

    label1.config(text=plat1['strMeal'])
    label2.config(text=plat2['strMeal'])

    # image gauche
    img1 = requests.get(plat1['strMealThumb'], verify=False).content
    image1 = Image.open(BytesIO(img1))
    image1 = image1.resize((300, 300), Image.LANCZOS)
    photo1 = ImageTk.PhotoImage(image1)

    # image droite
    img2 = requests.get(plat2['strMealThumb'], verify=False).content
    image2 = Image.open(BytesIO(img2))
    image2 = image2.resize((300, 300), Image.LANCZOS)
    photo2 = ImageTk.PhotoImage(image2)

    image_label1.config(image=photo1)
    image_label2.config(image=photo2)


def choix_gauche(event=None):

    global score_gauche, total

    score_gauche += 1
    total += 1

    resultat.config(
        text=f"✔ Vous préférez : {plat1['strMeal']}",
        fg="#2ECC71"
    )

    update_score()
    root.after(1000, plat_aleatoire)


def choix_droite(event=None):

    global score_droite, total

    score_droite += 1
    total += 1

    resultat.config(
        text=f"✔ Vous préférez : {plat2['strMeal']}",
        fg="#2ECC71"
    )

    update_score()
    root.after(1000, plat_aleatoire)


def update_score():

    score_label.config(
        text=f"Gauche : {score_gauche}    Droite : {score_droite}    Total : {total}"
    )


def hover_enter(widget):
    widget.config(bg="#1ABC9C")


def hover_leave(widget):
    widget.config(bg="#34495E")


# ---------------------------
# INTERFACE
# ---------------------------

root = tk.Tk()
root.title("Choix du plat préféré")
root.geometry("800x600")
root.configure(bg="#2C3E50")


# TITRE
titre = Label(
    root,
    text="CHOISISSEZ LE MEILLEUR PLAT 🍽",
    font=("Arial", 26, "bold"),
    bg="#2C3E50",
    fg="white"
)
titre.pack(pady=20)


# SCORE
score_label = Label(
    root,
    text="Gauche : 0    Droite : 0    Total : 0",
    font=("Arial", 16),
    bg="#2C3E50",
    fg="#1ABC9C"
)
score_label.pack()


# RESULTAT
resultat = Label(
    root,
    text="Cliquez sur une image",
    font=("Arial", 16),
    bg="#2C3E50",
    fg="white"
)
resultat.pack(pady=10)


# FRAME PRINCIPAL
frame = Frame(root, bg="#2C3E50")
frame.pack(pady=20)


# FRAME GAUCHE
frame1 = Frame(frame, bg="#34495E", bd=3, relief="ridge")
frame1.pack(side="left", padx=20)

label1 = Label(
    frame1,
    text="",
    font=("Arial", 14, "bold"),
    bg="#34495E",
    fg="white"
)
label1.pack(pady=10)

image_label1 = Label(frame1, bg="#34495E", cursor="hand2")
image_label1.pack(padx=10, pady=10)

image_label1.bind("<Button-1>", choix_gauche)
image_label1.bind("<Enter>", lambda e: hover_enter(frame1))
image_label1.bind("<Leave>", lambda e: hover_leave(frame1))


# FRAME DROITE
frame2 = Frame(frame, bg="#34495E", bd=3, relief="ridge")
frame2.pack(side="left", padx=20)

label2 = Label(
    frame2,
    text="",
    font=("Arial", 14, "bold"),
    bg="#34495E",
    fg="white"
)
label2.pack(pady=10)

image_label2 = Label(frame2, bg="#34495E", cursor="hand2")
image_label2.pack(padx=10, pady=10)

image_label2.bind("<Button-1>", choix_droite)
image_label2.bind("<Enter>", lambda e: hover_enter(frame2))
image_label2.bind("<Leave>", lambda e: hover_leave(frame2))


# BOUTON NOUVEAU
bouton = Button(
    root,
    text="Nouveaux plats",
    font=("Arial", 14, "bold"),
    bg="#3498DB",
    fg="white",
    bd=0,
    cursor="hand2",
    command=plat_aleatoire
)
bouton.pack(pady=10)


# DEMARRAGE
plat_aleatoire()

root.mainloop()
