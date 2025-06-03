import requests
import tkinter as tk
from tkinter import messagebox

#Fonction qui s'occupe de traiter les données entrer dans le champs
def barre_de_recherche():

    #Requête HTTP à partir de l'url formé et formaté à partir de ce que l'utilisateur a entré (entry.get)
    nom_plat = entry.get()
    if nom_plat:
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={nom_plat}"
    else:
        return
    reponse = requests.get(url, verify=False)
    print(reponse)

    #Vérification du succès de la requête et insertion des différents plats dans liste_plat
    if reponse.status_code == 200:
        info = reponse.json()
        print(info)
        if info['meals']:
            print(info)
            liste_plat.delete(0, tk.END)
            for plat in info['meals']:
                liste_plat.insert(tk.END, plat['strMeal'])
        else:
            messagebox.showinfo("Aucun résultat", "Aucun plat trouvé pour ce terme de recherche.")
    else:
        messagebox.showerror("Erreur", "Impossible de récupérer les données depuis l'API.")

def affichage():

    #L'indice du résultat cliqué par l'utilisateur est enregistré dans cette variable
    affiche = liste_plat.curselection()

    if affiche:

        #plat est ici le plat correspondant à l'indice affiche
        plat = liste_plat.get(affiche)
        print(plat)
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={plat}"
        reponse = requests.get(url, verify=False)

        #Vérification du succès de la requête et affichage de la recette du plat sélectionné
        if reponse.status_code == 200:
            info = reponse.json()
            recette = info['meals'][0]['strInstructions']
            messagebox.showinfo(affiche, recette)
        else:
            messagebox.showerror("Erreur", "Impossible de récupérer les données depuis l'API.")
    else:
        messagebox.showinfo("Sélectionnez un plat", "Veuillez sélectionner un plat dans la liste.")

# Interface Tkinter
root = tk.Tk()
root.title("Recherche de plats")

label = tk.Label(root, text="Entrez un plat à rechercher:")
label.pack()

entry = tk.Entry(root)
entry.pack()

bouton_recherche= tk.Button(root, text="Rechercher", command=barre_de_recherche)
bouton_recherche.pack()

liste_plat= tk.Listbox(root, width=50, height=20)
liste_plat.pack()

bouton_affichage= tk.Button(root, text="Afficher la recette", command=affichage)
bouton_affichage.pack()

root.mainloop()