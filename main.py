#Auteur : Adriano Alves Morais, Marc Schilter
#Date : 15.12.2025
#Présentation du programme : Programme du jeu du pendu en interface graphique

#importation de librairie
import random
import tkinter as tk
from PIL import Image, ImageTk  # Pillow

#######################################################################################################################
#Fonction mot aléatoire
def mots_aleatoires(index,lettre, proposition_vide):
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
#Fonction image pendu (JPG)
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
    idx = min(erreur, max_erreur - 1)  #évite de dépasser la dernière image
    return max_erreur, etapes_pendu[idx]

#######################################################################################################################
#initialisation des variables
erreur = 0
lettre_choisi = ""
numero_random = random.randint(0,9)
stockage = mots_aleatoires(numero_random, "", "")[1]
mot_visible = mots_aleatoires(numero_random, lettre_choisi, stockage)[0] #récuperation du mot aléatoire
window_width = 500
window_height = 650

#######################################################################################################################
#tkinter
root = tk.Tk()
root.title("Pendu")
# dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcul les coordonnées x et y pour centrer la fenêtre
position_x = int((screen_width / 2) - (window_width / 2))
position_y = int((screen_height / 2) - (window_height / 2))
root.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')

#Zone saisie utilisateur
frame_User_Entry = tk.Frame(root)
frame_User_Entry.pack(side="top", pady=10)

label_Instruction = tk.Label(frame_User_Entry, text="Choisis une lettre :")
label_Instruction.grid(row=0, column=0, padx=5)

entry_Lettre = tk.Entry(frame_User_Entry, width=10)
entry_Lettre.grid(row=0, column=1, padx=5)
entry_Lettre.focus()

label_Lettres = tk.Label(root, text=" ".join(stockage), font=("Arial", 22))
label_Lettres.pack(side="top", pady=10)

#######################################################################################################################
#controle des proposition
def proposition(event):
    global erreur, stockage, lettre_choisi

    #stocke la lettre majuscule de la saisie et le supprime
    lettre_choisi = entry_Lettre.get().strip().upper()
    entry_Lettre.delete(0, tk.END)

    #controle que la proposition soit une seule lettre et pas de chiffre
    if len(lettre_choisi) != 1 or not lettre_choisi.isalpha():
        return

    #affiche le pendu si la proposition est fausse
    if lettre_choisi not in str(mot_visible):
        erreur += 1
        update_pendu()

    #met à jour l'affichage du mot
    stockage = mots_aleatoires(numero_random, lettre_choisi, stockage)[1]
    label_Lettres.config(text=" ".join(stockage))

    if stockage == mot_visible:
        # Fin de partie
        win = tk.Toplevel(root)
        win.title("Résultat du jeu")
        win.geometry(f'300x150+{position_x + 100}+{position_y + 100}')
        win_label = tk.Label(win, text="Félicitations ! Vous avez gagné !", font=("Arial", 14))
        win_label.pack(side="top", pady=20)
        frame_win = tk.Frame(win)
        frame_win.pack(side="bottom", pady=10)
        btn_win_relance = tk.Button(frame_win, text="Recommencer", command=win.destroy)
        btn_win_relance.grid(row=0, column=0, padx=5)
        btn_win_quit = tk.Button(frame_win, text="Quitter", command=root.quit)
        btn_win_quit.grid(row=0, column=1, padx=5)
        return

entry_Lettre.bind("<Return>", proposition)

#######################################################################################################################
#Frame du pendu (image) placé EN BAS avec place
frame_Pendu = tk.Frame(root, width=280, height=280, bd=2, relief="groove")
frame_Pendu.place(relx=0.5, rely=1.0, anchor="s", y=-130)

label_Pendu = tk.Label(frame_Pendu)
label_Pendu.place(relx=0.5, rely=0.5, anchor="center")

photo_pendu = None  # référence (IMPORTANT)

def update_pendu():
    """Charge et affiche l'image JPG correspondant à l'erreur actuelle."""
    global photo_pendu

    _, image_path = dessiner_pendu(erreur)

    #Ouvre l'image (JPG) avec Pillow
    img = Image.open(image_path)

    #Redimensionne pour qu'elle rentre dans le frame (optionnel mais conseillé)
    #Ici: 260x260 (tu peux ajuster)
    img = img.resize((260, 260), Image.Resampling.LANCZOS)

    #Convertit en image Tkinter
    photo_pendu = ImageTk.PhotoImage(img)

    #Affiche
    label_Pendu.config(image=photo_pendu)

#image initiale
update_pendu()

#######################################################################################################################


root.mainloop()