from io import BytesIO
from tkinter import*
from random import*
from PIL import Image, ImageTk
import urllib.request
import io






def Relance():
    global menu,plat
    plat_aleatoire=choice(plat)
    entier_aleatoire=randint(1,menu[plat_aleatoire])
    p=list(plat)
    p.remove(plat_aleatoire)
    p1=choice(p)
    p.remove(p1)
    p2=choice(p)
    choix_plat=[p2,p1,plat_aleatoire]

    url="https://foodish-api.com/images/"+plat_aleatoire+"/"+plat_aleatoire+str(entier_aleatoire)+".jpg"

    with urllib.request.urlopen(url) as response:
        image_data = response.read()
    image = Image.open(io.BytesIO(image_data))


    largeur = 500
    hauteur = 500
    image_redimensionnee = image.resize((largeur, hauteur), Image.LANCZOS)
    img.paste(image_redimensionnee)
    label_image.configure(image=img)
    print(choix_plat)

    txt_1=choice(choix_plat)
    if txt_1==plat_aleatoire:
        Bouton1.config(command=Trouvé)
    else:
        Bouton1.config(command=Perdu)

    Bouton1.config(text=txt_1)
    choix_plat.remove(txt_1)

    txt_2=choice(choix_plat)
    if txt_2==plat_aleatoire:
        Bouton2.config(command=Trouvé)
    else:
        Bouton2.config(command=Perdu)

    Bouton2.config(text=txt_2)
    choix_plat.remove(txt_2)


    txt_3=choix_plat[0]
    Bouton3.config(text=txt_3)
    if txt_3==plat_aleatoire:
        Bouton3.config(command=Trouvé)
    else:
        Bouton3.config(command=Perdu)
def Trouvé():
    global point,cpt
    point+=1
    cpt+=1
    Score.config(text="Points : "+str(point)+"/"+str(cpt))
    Relance()
def Perdu():
    global cpt
    cpt+=1
    Score.config(text="Points : "+str(point)+"/"+str(cpt))
    Relance()




root=Tk()
root.geometry("1000x1000")
menu={"biryani" : 81,
"burger" : 87,
"butter-chicken" : 22,
"dessert" : 36,
"dosa" : 83,
"idly" : 77,
"pasta" : 34,
"pizza" : 95,
"rice" : 35,
"samosa" : 22}
point=0
cpt=0

plat=list(menu.keys())
plat_aleatoire=choice(plat)
entier_aleatoire=randint(1,menu[plat_aleatoire])
p=list(plat)
p.remove(plat_aleatoire)
p1=choice(p)
p.remove(p1)
p2=choice(p)
choix_plat=[p2,p1,plat_aleatoire]

url="https://foodish-api.com/images/"+plat_aleatoire+"/"+plat_aleatoire+str(entier_aleatoire)+".jpg"
print(url)
with urllib.request.urlopen(url) as response:
        image_data = response.read()

# Ouvrir l'image avec PIL
image = Image.open(io.BytesIO(image_data))


largeur = 500
hauteur = 500
image_redimensionnee = image.resize((largeur, hauteur), Image.LANCZOS)

img=ImageTk.PhotoImage(image_redimensionnee)
label_image = Label(root, image=img)


Titre= Label(root, text="Devinez le plat !",font=("Arial",30))
Titre.pack()

Score= Label(root, text="Points : "+str(point)+"/"+str(cpt),font=("Arial", 20))
Score.pack()

label_image.place(x=(root.winfo_width() - label_image.winfo_width()) // 2, y=(root.winfo_height() - label_image.winfo_height()) // 2)
label_image.pack()

cadre_boutons = Frame(root)
cadre_boutons.pack()
txt_1=choice(choix_plat)
if txt_1==plat_aleatoire:

    Bouton1 = Button(cadre_boutons, text=txt_1, font=("Arial", 20),command=Trouvé)
    Bouton1.pack(side=LEFT, padx=10)
else:
    Bouton1 = Button(cadre_boutons, text=txt_1, font=("Arial", 20),command=Perdu)
    Bouton1.pack(side=LEFT, padx=10)

choix_plat.remove(txt_1)
txt_2=choice(choix_plat)

if txt_2==plat_aleatoire:

    Bouton2 = Button(cadre_boutons, text=txt_2, font=("Arial", 20),command=Trouvé)
    Bouton2.pack(side=LEFT, padx=10)
else:
    Bouton2 = Button(cadre_boutons, text=txt_2, font=("Arial", 20),command=Perdu)
    Bouton2.pack(side=LEFT, padx=10)

choix_plat.remove(txt_2)
txt_3=choix_plat[0]
if txt_3==plat_aleatoire:

    Bouton3 = Button(cadre_boutons, text=txt_3, font=("Arial", 20),command=Trouvé)
    Bouton3.pack(side=LEFT, padx=10)
else:
    Bouton3 = Button(cadre_boutons, text=txt_3, font=("Arial", 20),command=Perdu)
    Bouton3.pack(side=LEFT, padx=10)



choix_plat.remove(txt_3)


root.mainloop()