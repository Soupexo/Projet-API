from tkinter import*
from random import*
from PIL import Image, ImageTk
import subprocess

root=Tk()
root.title("Tabemono Game")

root.attributes("-fullscreen", True)
fichier_a_executer1 = 'images/choix_mode.py'

bg= Image.open("images/page d'accueil.png")

resize_image = bg.resize((1600, 1080))
ph = ImageTk.PhotoImage(resize_image)
canvas = Canvas(root, width=1600, height=1080)
canvas.create_image(1600//2, 1080//2, image=ph)
canvas.pack()
def fonction(event):
    x, y=event.x, event.y
    if 317<x<700 and 530<y<674:
        root.destroy()
        subprocess.run(['python', fichier_a_executer1])
    elif 894<x<1277 and 526<y<675:
        root.destroy()

root.bind("<Button-1>", fonction)

root.mainloop()