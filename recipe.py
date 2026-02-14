import requests
import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, Entry, Listbox, Scrollbar, END

# ---------------------------
# FONCTIONS
# ---------------------------

def barre_de_recherche():

    nom_plat = entry.get().strip()

    if not nom_plat:
        messagebox.showinfo("Info", "Veuillez entrer un nom de plat.")
        return

    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={nom_plat}"

    try:
        reponse = requests.get(url, verify=False)
    except:
        messagebox.showerror("Erreur", "Problème de connexion.")
        return

    if reponse.status_code == 200:

        info = reponse.json()

        liste_plat.delete(0, END)

        if info['meals']:

            for plat in info['meals']:
                liste_plat.insert(END, plat['strMeal'])

            status_label.config(text=f"{len(info['meals'])} résultat(s) trouvé(s)", fg="#2ECC71")

        else:
            status_label.config(text="Aucun résultat", fg="#E74C3C")

    else:
        messagebox.showerror("Erreur", "Impossible de récupérer les données.")


def affichage():

    selection = liste_plat.curselection()

    if not selection:
        messagebox.showinfo("Info", "Sélectionnez un plat.")
        return

    plat = liste_plat.get(selection)

    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={plat}"

    try:
        reponse = requests.get(url)
    except:
        messagebox.showerror("Erreur", "Problème de connexion.")
        return

    if reponse.status_code == 200:

        info = reponse.json()

        recette = info['meals'][0]['strInstructions']

        fenetre_recette = tk.Toplevel(root)
        fenetre_recette.title(plat)
        fenetre_recette.geometry("600x500")
        fenetre_recette.configure(bg="#2C3E50")

        titre = Label(
            fenetre_recette,
            text=plat,
            font=("Arial", 20, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        titre.pack(pady=10)

        texte = tk.Text(
            fenetre_recette,
            wrap="word",
            font=("Arial", 12),
            bg="#34495E",
            fg="white"
        )
        texte.insert("1.0", recette)
        texte.config(state="disabled")
        texte.pack(padx=10, pady=10, fill="both", expand=True)

    else:
        messagebox.showerror("Erreur", "Impossible de récupérer la recette.")


# ---------------------------
# INTERFACE
# ---------------------------

root = tk.Tk()
root.title("Recherche de recettes")
root.geometry("600x700")
root.configure(bg="#2C3E50")


# TITRE
titre = Label(
    root,
    text="RECHERCHE DE RECETTES 🍽",
    font=("Arial", 24, "bold"),
    bg="#2C3E50",
    fg="white"
)
titre.pack(pady=20)


# CADRE RECHERCHE
cadre_recherche = Frame(root, bg="#2C3E50")
cadre_recherche.pack(pady=10)


entry = Entry(
    cadre_recherche,
    font=("Arial", 14),
    width=25,
    bg="#34495E",
    fg="white",
    insertbackground="white",
    bd=0
)
entry.grid(row=0, column=0, padx=10)


bouton_recherche = Button(
    cadre_recherche,
    text="Rechercher",
    font=("Arial", 14, "bold"),
    bg="#1ABC9C",
    fg="black",
    bd=0,
    cursor="hand2",
    command=barre_de_recherche
)
bouton_recherche.grid(row=0, column=1)


# STATUS
status_label = Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#2C3E50"
)
status_label.pack()


# CADRE LISTE
cadre_liste = Frame(root, bg="#2C3E50")
cadre_liste.pack(pady=20)


scrollbar = Scrollbar(cadre_liste)

liste_plat = Listbox(
    cadre_liste,
    width=40,
    height=15,
    font=("Arial", 14),
    bg="#34495E",
    fg="white",
    selectbackground="#1ABC9C",
    bd=0,
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=liste_plat.yview)

liste_plat.pack(side="left")
scrollbar.pack(side="right", fill="y")


# BOUTON AFFICHER
bouton_affichage = Button(
    root,
    text="Afficher la recette",
    font=("Arial", 16, "bold"),
    bg="#3498DB",
    fg="white",
    bd=0,
    cursor="hand2",
    command=affichage
)
bouton_affichage.pack(pady=20)


root.mainloop()
