from tkinter import *
from random import choice, randint
from PIL import Image, ImageTk
import urllib.request
import io

# ---------------------------
# DONNEES
# ---------------------------

menu = {
    "biryani": 81,
    "burger": 87,
    "butter-chicken": 22,
    "dessert": 36,
    "dosa": 83,
    "idly": 77,
    "pasta": 34,
    "pizza": 95,
    "rice": 35,
    "samosa": 22
}

plat = list(menu.keys())

point = 0
cpt = 0
bonne_reponse = ""
img = None


# ---------------------------
# FONCTIONS
# ---------------------------

def charger_image():
    global bonne_reponse, img

    bonne_reponse = choice(plat)
    num = randint(1, menu[bonne_reponse])

    url = f"https://foodish-api.com/images/{bonne_reponse}/{bonne_reponse}{num}.jpg"

    try:
        with urllib.request.urlopen(url) as response:
            image_data = response.read()

        image = Image.open(io.BytesIO(image_data))
        image = image.resize((400, 400), Image.LANCZOS)

        img = ImageTk.PhotoImage(image)
        label_image.config(image=img)

    except:
        charger_image()


def generer_choix():
    choix = plat.copy()
    choix.remove(bonne_reponse)

    faux1 = choice(choix)
    choix.remove(faux1)

    faux2 = choice(choix)

    boutons = [bonne_reponse, faux1, faux2]

    # mélanger
    from random import shuffle
    shuffle(boutons)

    Bouton1.config(text=boutons[0], command=lambda: verifier(boutons[0]))
    Bouton2.config(text=boutons[1], command=lambda: verifier(boutons[1]))
    Bouton3.config(text=boutons[2], command=lambda: verifier(boutons[2]))


def verifier(reponse):
    global point, cpt

    cpt += 1

    if reponse == bonne_reponse:
        point += 1
        resultat.config(text="✔ Bonne réponse !", fg="#2ECC71")
    else:
        resultat.config(text=f"✘ Mauvaise réponse ! ({bonne_reponse})", fg="#E74C3C")

    Score.config(text=f"Points : {point} / {cpt}")

    root.after(1500, nouvelle_question)


def nouvelle_question():
    resultat.config(text="")
    charger_image()
    generer_choix()


# ---------------------------
# INTERFACE
# ---------------------------

root = Tk()
root.title("Quiz Food")
root.geometry("700x800")
root.configure(bg="#2C3E50")


# TITRE
Titre = Label(
    root,
    text="DEVINEZ LE PLAT 🍽",
    font=("Arial", 28, "bold"),
    bg="#2C3E50",
    fg="white"
)
Titre.pack(pady=20)


# SCORE
Score = Label(
    root,
    text="Points : 0 / 0",
    font=("Arial", 18),
    bg="#2C3E50",
    fg="#1ABC9C"
)
Score.pack(pady=10)


# CADRE IMAGE
cadre_image = Frame(root, bg="white", bd=3, relief=RIDGE)
cadre_image.pack(pady=20)

label_image = Label(cadre_image, bg="white")
label_image.pack(padx=10, pady=10)


# RESULTAT
resultat = Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#2C3E50"
)
resultat.pack(pady=10)


# CADRE BOUTONS
cadre_boutons = Frame(root, bg="#2C3E50")
cadre_boutons.pack(pady=30)


# STYLE BOUTONS
style_bouton = {
    "font": ("Arial", 16, "bold"),
    "width": 15,
    "height": 2,
    "bg": "#34495E",
    "fg": "white",
    "activebackground": "#1ABC9C",
    "activeforeground": "black",
    "bd": 0,
    "cursor": "hand2"
}

Bouton1 = Button(cadre_boutons, **style_bouton)
Bouton1.grid(row=0, column=0, padx=15, pady=10)

Bouton2 = Button(cadre_boutons, **style_bouton)
Bouton2.grid(row=0, column=1, padx=15, pady=10)

Bouton3 = Button(cadre_boutons, **style_bouton)
Bouton3.grid(row=0, column=2, padx=15, pady=10)


# DEMARRAGE
nouvelle_question()

root.mainloop()
