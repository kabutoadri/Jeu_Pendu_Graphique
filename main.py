#Auteur : Adriano Alves Morais, Marc Schilter
#Date : 15.12.2025
#Présentation du programme : Programme du jeu du pendu en interface graphique

import random
import tkinter as tk
from PIL import Image, ImageTk  # Pillow

#######################################################################################################################
# Fonction mot aléatoire
def mots_aleatoires(index, lettre, proposition_vide):
    listes_mots = ["python", "ordinateur", "jeu", "random", "chat", "chien", "soleil", "lune", "code", "apprentissage"]

    mot_mystere = list(listes_mots[index].upper())

    if proposition_vide == "":
        affichage_mot = ["_"] * len(mot_mystere)
    else:
        affichage_mot = proposition_vide

    for i, char in enumerate(mot_mystere):
        if char == lettre:
            affichage_mot[i] = lettre

    return mot_mystere, affichage_mot

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

window_width = 500
window_height = 650
Bg_Color= "#a6a7ab"
#######################################################################################################################
# Tkinter
root = tk.Tk()
root.title("Pendu")
root.configure(bg=Bg_Color)

# Dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcul les coordonnées x et y pour centrer la fenêtre
position_x = int((screen_width / 2) - (window_width / 2))
position_y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

#######################################################################################################################
# Zone saisie utilisateur
frame_User_Entry = tk.Frame(root, bg=Bg_Color)
frame_User_Entry.pack(side="top", pady=10)

label_Instruction = tk.Label(frame_User_Entry, text="Choisis une lettre :", bg=Bg_Color)
label_Instruction.pack(side="top")
label_Instruction.grid(row=0, column=0, padx=5)

entry_Lettre = tk.Entry(frame_User_Entry, width=10)
entry_Lettre.grid(row=0, column=1, padx=5)
entry_Lettre.focus()

label_Lettres = tk.Label(root, text=" ".join(stockage), font=("Arial", 22), bg=Bg_Color)
label_Lettres.pack(side="top", pady=10)

#######################################################################################################################
# Frame du pendu (image) placé EN BAS avec place
frame_Pendu = tk.Frame(root, width=280, height=280, bd=2, relief="groove", bg=Bg_Color)
frame_Pendu.place(relx=0.5, rely=1.0, anchor="s", y=-130)

label_Pendu = tk.Label(frame_Pendu, bg=Bg_Color)
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
    global erreur, lettre_choisi, numero_random, stockage, mot_visible

    erreur = 0
    lettre_choisi = ""

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
    top.configure(bg=Bg_Color)
    top.geometry(f"320x170+{position_x + 90}+{position_y + 120}")
    top.transient(root)
    top.grab_set()

    lbl = tk.Label(top, text=message, font=("Arial", 14, "bold"), bg=Bg_Color)
    lbl.pack(side="top", pady=20)

    #Afficher le mot si défaite
    if not is_win:
        mot_str = "".join(mot_visible)
        lbl_mot = tk.Label(top, text=f"Le mot était : {mot_str}", font=("Arial", 12), bg=Bg_Color)
        lbl_mot.pack(side="top", pady=5)

    frame_btn = tk.Frame(top, bg=Bg_Color)
    frame_btn.pack(side="bottom", pady=12)

    def recommencer_et_fermer():
        reset_game()
        top.destroy()

    btn_relance = tk.Button(frame_btn, text="Recommencer", command=recommencer_et_fermer)
    btn_relance.grid(row=0, column=0, padx=6)

    btn_quit = tk.Button(frame_btn, text="Quitter", command=root.quit)
    btn_quit.grid(row=0, column=1, padx=6)

#######################################################################################################################
# Contrôle des propositions
def proposition(event):
    global erreur, stockage, lettre_choisi

    lettre_choisi = entry_Lettre.get().strip().upper()
    entry_Lettre.delete(0, tk.END)

    # Contrôle: 1 lettre alpha
    if len(lettre_choisi) != 1 or not lettre_choisi.isalpha():
        return

    # Mauvaise lettre => erreur + update image
    if lettre_choisi not in mot_visible:
        erreur += 1
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

entry_Lettre.bind("<Return>", proposition)

#######################################################################################################################
root.mainloop()
