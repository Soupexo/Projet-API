import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

#Définition de la fonction qui va génerer deux plats aléatoirement sous forme de dictionnaire
def plat_aleatoire():

    #Requête HTTP vers le lien de l'API
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    reponse1 = requests.get(url, verify=False)
    reponse2 = requests.get(url, verify=False)


    #Affectation après conversion JSON des données des deux plats dans les variables plat1 et plat2
    if reponse1.status_code == 200 and reponse2.status_code == 200:
        info1 = reponse1.json()
        info2 = reponse2.json()
        print(info1,info2)
        plat1 = info1['meals'][0]
        plat2 = info2['meals'][0]

        #Appel de la fonction où on va lui joindre les deux variables plat1 et plat2
        affiche_plat(plat1, plat2)
    else:

        #Cas où la requête ne réussi pas
        label1.config(text="Erreur: Impossible de récupérer les données depuis l'API.")
        label2.config(text="Erreur: Impossible de récupérer les données depuis l'API.")

#Définition de la fonction qui va afficher sur les deux labels les images correspondant aux deux plats et les modifier au clic
def affiche_plat(plat1, plat2):
    label1.config(text=plat1['strMeal'])
    label2.config(text=plat2['strMeal'])

    #Création et conversion de l'image 1
    image_url1 = plat1['strMealThumb']
    image_info1 = requests.get(image_url1, verify=False).content
    image1 = Image.open(BytesIO(image_info1))
    photo1 = ImageTk.PhotoImage(image1)

    #Création et conversion de l'image 2
    image_url2 = plat2['strMealThumb']
    image_info2 = requests.get(image_url2, verify=False).content
    image2 = Image.open(BytesIO(image_info2))
    photo2 = ImageTk.PhotoImage(image2)

    #Modification des images des labels par les images 1 et 2
    image_label1.config(image=photo1)
    image_label1.image = photo1

    image_label2.config(image=photo2)
    image_label2.image = photo2

    #Chaque label est lié au clic à une fonction en l'occurence "plat_aléatoire"
    image_label1.bind("<Button-1>", lambda event: plat_aleatoire())
    image_label2.bind("<Button-1>", lambda event: plat_aleatoire())


#Création des entités graphiques (label, frame...)
root = Tk()
root.title("Choix du Plat Préféré")

titre = Label(root, text="Choisissez votre plat préféré")
titre.pack(pady=10)

frame = Frame(root)
frame.pack()

frame1 = Frame(frame)
frame1.pack(side=LEFT, padx=10)

label1 = Label(frame1, text="")
label1.pack()

image_label1 = Label(frame1)
image_label1.pack()

frame2 = Frame(frame)
frame2.pack(side=LEFT, padx=10)

label2 = Label(frame2, text="")
label2.pack()

image_label2 = Label(frame2)
image_label2.pack()

#Appel à la fonction pour générer le premier couple d'image
plat_aleatoire()

root.mainloop()