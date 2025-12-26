#Auteur : Adriano Alves Morais, Marc Schilter
#Date : 15.12.2025
#Présentation du programme : Programme du jeu du pendu en interface graphique

import random
import tkinter as tk
from PIL import Image, ImageTk  # Pillow

#######################################################################################################################
# Fonction mot aléatoire
def mots_aleatoires(index, lettre, proposition_vide):
    #listes_mots = ["python", "ordinateur", "jeu", "random", "chat", "chien", "soleil", "lune", "code", "apprentissage"]
    dict_mots = {"python": "Langage utilisé pour créer le jeu",
                 "ordinateur": "Utilisé pour lancer le jeu",
                 "jeu":"Qu'est-ce qu'un Pendu?",
                 "random":"1, 4, 2, 5, 3, ...",
                 "chat": "Animal",
                 "chien": "Animal",
                 "soleil": "Jour",
                 "lune": "nuit",
                 "code": "Programmation",
                 "apprentissage": "CPNV"
                 }
    listes_index = list(dict_mots.keys())

    mot_mystere = list(listes_index[index].upper())
    #mot_mystere = list(listes_mots[index].upper())

    if proposition_vide == "":
        affichage_mot = ["_"] * len(mot_mystere)
    else:
        affichage_mot = proposition_vide

    for i, char in enumerate(mot_mystere):
        if char == lettre:
            affichage_mot[i] = lettre

    return mot_mystere, affichage_mot, dict_mots[listes_index[index]]

#######################################################################################################################
# Fonction image pendu (JPG)
def dessiner_pendu(erreur):
    etapes_pendu = [
        "img_pendu/Pendu_1.jpg",
        "img_pendu/Pendu_2.jpg",
        "img_pendu/Pendu_3.jpg",
        "img_pendu/Pendu_4.jpg",
        "img_pendu/Pendu_5.jpg",
        "img_pendu/Pendu_6.jpg",
        "img_pendu/Pendu_7.jpg",
        "img_pendu/Pendu_8.jpg",
        "img_pendu/Pendu_9.jpg",
        "img_pendu/Pendu_10.jpg",
        "img_pendu/Pendu_11.jpg"
    ]

    max_erreur = len(etapes_pendu)
    idx = min(erreur, max_erreur - 1)  # évite de dépasser la dernière image
    return max_erreur, etapes_pendu[idx]

#######################################################################################################################
# Initialisation des variables
erreur = 0
lettre_choisi = ""
numero_random = random.randint(0, 9)
stockage = mots_aleatoires(numero_random, "", "")[1]
mot_visible = mots_aleatoires(numero_random, lettre_choisi, stockage)[0]  # mot aléatoire (liste de lettres)
indice = mots_aleatoires(numero_random, lettre_choisi, stockage)[2]
lettres_utilisees = [] # liste des lettres déjà proposées
message_indice = "Passe ta souris ici pour l'indice"

#######################################################################################################################
# Paramètre de la fenêtre
window_width = 550
window_height = 750
bg_color= "#f0f8ff"
text_color = "#333333"
titre_color = "#ff69b4"
cacher_color = "#00bfff"
highlight_color = "#ff4d4d"
utiliser_color = "#ff4500"
font_titre = ("Comic Sans MS", 20, "bold")
font_text = ("Comic Sans MS", 14)
font_entry = ("Comic Sans MS", 16, "bold")
font_cacher = ("Courier New", 24, "bold")

#######################################################################################################################
# Tkinter
root = tk.Tk()
root.title("Pendu")
root.configure(bg=bg_color)

# Dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcul les coordonnées x et y pour centrer la fenêtre
position_x = int((screen_width / 2) - (window_width / 2))
position_y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

#######################################################################################################################
# Titre
label_titre = tk.Label(root, text="Jeu du Pendu", bg=bg_color, font=font_titre, fg=titre_color)
label_titre.pack(side="top", pady=10)

# Zone saisie utilisateur
frame_User_Entry = tk.Frame(root, bg=bg_color)
frame_User_Entry.pack(side="top", pady=10)

label_Instruction = tk.Label(frame_User_Entry, text="Choisis une lettre :", bg=bg_color, font=font_text, fg=text_color)
label_Instruction.grid(row=0, column=0, padx=5)

entry_Lettre = tk.Entry(frame_User_Entry, width=10, font=font_entry, fg=text_color)
entry_Lettre.grid(row=0, column=1, padx=5)
entry_Lettre.focus()

label_Lettres = tk.Label(root, text=" ".join(stockage), font=font_cacher, bg=bg_color, fg=cacher_color)
label_Lettres.pack(side="top", pady=10)

# Lettres déjà utiisées
label_Utiliser = tk.Label(root, text="Lettres déjà utilisées : ", bg=bg_color, font=font_text, fg=utiliser_color)
label_Utiliser.pack(side="top", pady=50)

# indices
label_Indice = tk.Label(root, text=message_indice, width=len(message_indice), bg=bg_color, font=font_text, fg=text_color)
label_Indice.pack(side="bottom", pady=40)

#######################################################################################################################
# Frame du pendu (image) placé EN BAS avec place
frame_Pendu = tk.Frame(root, width=280, height=280, bd=2, relief="groove", bg=bg_color)
frame_Pendu.place(relx=0.5, rely=1.0, anchor="s", y=-130)

label_Pendu = tk.Label(frame_Pendu, bg=bg_color, fg=text_color)
label_Pendu.place(relx=0.5, rely=0.5, anchor="center")

photo_pendu = None  # référence (IMPORTANT)

def update_pendu():
    """Charge et affiche l'image JPG correspondant à l'erreur actuelle."""
    global photo_pendu

    _, image_path = dessiner_pendu(erreur)

    img = Image.open(image_path)
    img = img.resize((260, 260), Image.Resampling.LANCZOS)

    photo_pendu = ImageTk.PhotoImage(img)
    label_Pendu.config(image=photo_pendu)

# Image initiale
update_pendu()

#######################################################################################################################
# Reset complet de la partie
def reset_game():
    """Réinitialise la partie: erreur=0, nouveau mot, stockage reset, labels + image."""
    global erreur, lettre_choisi, numero_random, stockage, mot_visible, lettres_utilisees

    erreur = 0
    lettre_choisi = ""
    lettres_utilisees = []
    label_Utiliser.config(text="Lettres déjà utilisées : ")

    # Choisir un autre mot (différent si possible)
    ancien_index = numero_random
    numero_random = random.randint(0, 9)
    if numero_random == ancien_index:
        numero_random = (numero_random + 1) % 10

    stockage = mots_aleatoires(numero_random, "", "")[1]
    mot_visible = mots_aleatoires(numero_random, "", stockage)[0]

    label_Lettres.config(text=" ".join(stockage))
    update_pendu()
    entry_Lettre.delete(0, tk.END)
    entry_Lettre.focus()

#######################################################################################################################
# Popup générique (Win / Lose)
def show_end_popup(is_win: bool):
    """Affiche une popup de fin (victoire ou défaite) avec Recommencer / Quitter."""
    title = "Résultat du jeu"
    message = "Félicitations ! Vous avez gagné !" if is_win else "GAME OVER ! Vous avez perdu !"

    top = tk.Toplevel(root)
    top.title(title)
    top.configure(bg=bg_color)
    top.geometry(f"320x170+{position_x + 90}+{position_y + 120}")
    top.transient(root)
    # Évite les interactions avec la fenêtre principale
    top.grab_set()
    top.focus_force()

    lbl = tk.Label(top, text=message, font=("Arial", 14, "bold"), bg=bg_color)
    lbl.pack(side="top", pady=20)

    #Afficher le mot si défaite
    if not is_win:
        mot_str = "".join(mot_visible)
        lbl_mot = tk.Label(top, text=f"Le mot était : {mot_str}", font=("Arial", 12), bg=bg_color)
        lbl_mot.pack(side="top", pady=5)

    frame_btn = tk.Frame(top, bg=bg_color)
    frame_btn.pack(side="bottom", pady=12)

    def recommencer_et_fermer():
        reset_game()
        top.destroy()

    btn_relance = tk.Button(frame_btn, text="Rejouer", command=recommencer_et_fermer, font=font_text, bg=cacher_color, fg="white", width=10)
    btn_relance.grid(row=0, column=0, padx=6)

    btn_quit = tk.Button(frame_btn, text="Quitter", command=root.quit, font=font_text, bg=highlight_color, fg="white", width=10)
    btn_quit.grid(row=0, column=1, padx=6)

#######################################################################################################################
# Contrôle des propositions
def proposition(event):
    global erreur, stockage, lettre_choisi, lettres_utilisees

    lettre_choisi = entry_Lettre.get().strip().upper()
    entry_Lettre.delete(0, tk.END)

    # Contrôle : 1 lettre alpha
    if len(lettre_choisi) != 1 or not lettre_choisi.isalpha():
        return

    # Mauvaise lettre => erreur + update image et lettres utilisées
    if (lettre_choisi not in mot_visible) and (lettre_choisi not in lettres_utilisees):
        erreur += 1
        lettres_utilisees.append(lettre_choisi)
        label_Utiliser.config(text="Lettres déjà utilisées : " + " ".join(lettres_utilisees))
        update_pendu()

    # Met à jour l'affichage du mot
    stockage = mots_aleatoires(numero_random, lettre_choisi, stockage)[1]
    label_Lettres.config(text=" ".join(stockage))

    # Récupère le max d'erreurs autorisées (nombre d'images)
    max_erreur, _ = dessiner_pendu(erreur)

    # Victoire
    if stockage == mot_visible:
        show_end_popup(is_win=True)
        return

    # Défaite (dernière image atteinte)
    # Avec 11 images, on autorise erreur = 0..10 (10 mauvaises lettres)
    if erreur >= max_erreur - 1:
        show_end_popup(is_win=False)
        return

def survol_label(event):
    label_Indice.config(text="indice: " + indice)

def quitter_label(event):
    label_Indice.config(text=message_indice)

# bind pour la gestion des événements
label_Indice.bind("<Enter>", survol_label)
label_Indice.bind("<Leave>", quitter_label)
entry_Lettre.bind("<Return>", proposition)

#######################################################################################################################
root.mainloop()
