# Créé par moula, le 15/04/2024 en Python 3.7
from tkinter import*
from random import*
from PIL import Image, ImageTk
import subprocess

root=Tk()
root.attributes("-fullscreen", True)
root.title("Tabemono Game")
bg1= Image.open("images/choix mode.png")
bg2= bg1.rotate(90)
fichier_a_executer1 = 'quizz.py'
fichier_a_executer2 = "recipe.py"
fichier_a_executer3= "tupreferes.py"
resize_image = bg2.resize((1600, 1080))
ph = ImageTk.PhotoImage(resize_image)
canvas = Canvas(root, width=1600, height=1080)
canvas.create_image(1600//2, 1080//2, image=ph)
canvas.pack()
def fonction(event):
    x, y=event.x, event.y
    if 607<x<994 and 252<y<396:
        root.destroy()
        subprocess.run(['python', fichier_a_executer1])
    elif 607<x<994 and 421<y<566:
        root.destroy()
        subprocess.run(['python', fichier_a_executer2])
    elif 607<x<994 and 587<y<735:
        root.destroy()
        subprocess.run(['python', fichier_a_executer3])
    elif 508<x<707 and 803<y<857:
        root.destroy()







root.bind("<Button-1>", fonction)
root.mainloop()