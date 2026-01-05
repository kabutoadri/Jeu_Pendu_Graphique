#Auteur : Adriano Alves Morais, Marc Schilter
#Date : 15.12.2025
#Présentation du programme : Programme du jeu du pendu en interface graphique

import random
import tkinter as tk
from PIL import Image, ImageTk  # Pillow

#######################################################################################################################
# Fonction mot aléatoire
def random_words(index, letter, empty_proposal):
    dict_words = {"python": "Langage utilisé pour créer le jeu",
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
    index_list = list(dict_words.keys())

    mystery_word = list(index_list[index].upper())

    if empty_proposal == "":
        display_word = ["_"] * len(mystery_word)
    else:
        display_word = empty_proposal

    for i, char in enumerate(mystery_word):
        if char == letter:
            display_word[i] = letter

    return mystery_word, display_word, dict_words[index_list[index]]

#######################################################################################################################
# Fonction image pendu (JPG)
def draw_pendu(mistake):
    stage_pendu = [
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

    mistake_max = len(stage_pendu)
    idx = min(mistake, mistake_max - 1)  # évite de dépasser la dernière image
    return mistake_max, stage_pendu[idx]

#######################################################################################################################
# Initialisation des variables
mistake = 0
choice_letter = ""
random_numero = random.randint(0, 9)
storage = random_words(random_numero, "", "")[1]
visible_word = random_words(random_numero, choice_letter, storage)[0]  # mot aléatoire (liste de lettres)
hint = random_words(random_numero, choice_letter, storage)[2]
used_letter = [] # liste des lettres déjà proposées
hint_message = "Passe ta souris ici pour l'indice"

#######################################################################################################################
# Paramètre de la fenêtre
window_width = 550
window_height = 750
bg_color= "#f0f8ff"
text_color = "#333333"
title_color = "#ff69b4"
hidden_color = "#00bfff"
highlight_color = "#ff4d4d"
used_color = "#ff4500"
font_title = ("Comic Sans MS", 20, "bold")
font_text = ("Comic Sans MS", 14)
font_entry = ("Comic Sans MS", 16, "bold")
font_hidden = ("Courier New", 24, "bold")

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
label_title = tk.Label(root, text="Jeu du Pendu", bg=bg_color, font=font_title, fg=title_color)
label_title.pack(side="top", pady=10)

# Zone saisie utilisateur
frame_user_entry = tk.Frame(root, bg=bg_color)
frame_user_entry.pack(side="top", pady=10)

label_instruction = tk.Label(frame_user_entry, text="Choisis une lettre :", bg=bg_color, font=font_text, fg=text_color)
label_instruction.grid(row=0, column=0, padx=5)

entry_letter = tk.Entry(frame_user_entry, width=10, font=font_entry, fg=text_color)
entry_letter.grid(row=0, column=1, padx=5)
entry_letter.focus()

label_letter = tk.Label(root, text=" ".join(storage), font=font_hidden, bg=bg_color, fg=hidden_color)
label_letter.pack(side="top", pady=10)

# Lettres déjà utiisées
label_used_letter = tk.Label(root, text="Lettres déjà utilisées : ", bg=bg_color, font=font_text, fg=used_color)
label_used_letter.pack(side="top", pady=50)

# indices
label_hint = tk.Label(root, text=hint_message, width=len(hint_message), bg=bg_color, font=font_text, fg=text_color)
label_hint.pack(side="bottom", pady=40)

#######################################################################################################################
# Frame du pendu (image) placé EN BAS avec place
frame_pendu = tk.Frame(root, width=280, height=280, bd=2, relief="groove", bg=bg_color)
frame_pendu.place(relx=0.5, rely=1.0, anchor="s", y=-130)

label_pendu = tk.Label(frame_pendu, bg=bg_color, fg=text_color)
label_pendu.place(relx=0.5, rely=0.5, anchor="center")

photo_pendu = None  # référence (IMPORTANT)

def update_pendu():
    """Charge et affiche l'image JPG correspondant à l'erreur actuelle."""
    global photo_pendu

    _, image_path = draw_pendu(mistake)

    img = Image.open(image_path)
    img = img.resize((260, 260), Image.Resampling.LANCZOS)

    photo_pendu = ImageTk.PhotoImage(img)
    label_pendu.config(image=photo_pendu)

# Image initiale
update_pendu()

#######################################################################################################################
# Reset complet de la partie
def reset_game():
    """Réinitialise la partie: erreur=0, nouveau mot, stockage reset, labels + image."""
    global mistake, choice_letter, random_numero, storage, visible_word, used_letter

    mistake = 0
    choice_letter = ""
    used_letter = []
    label_used_letter.config(text="Lettres déjà utilisées : ")

    # Choisir un autre mot (différent si possible)
    old_index = random_numero
    random_numero = random.randint(0, 9)
    if random_numero == old_index:
        random_numero = (random_numero + 1) % 10

    storage = random_words(random_numero, "", "")[1]
    visible_word = random_words(random_numero, "", storage)[0]

    label_letter.config(text=" ".join(storage))
    update_pendu()
    entry_letter.delete(0, tk.END)
    entry_letter.focus()

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
        word_str = "".join(visible_word)
        lbl_word = tk.Label(top, text=f"Le mot était : {word_str}", font=("Arial", 12), bg=bg_color)
        lbl_word.pack(side="top", pady=5)

    frame_btn = tk.Frame(top, bg=bg_color)
    frame_btn.pack(side="bottom", pady=12)

    def restart_and_quit():
        reset_game()
        top.destroy()

    btn_restart = tk.Button(frame_btn, text="Rejouer", command=restart_and_quit, font=font_text, bg=hidden_color, fg="white", width=10)
    btn_restart.grid(row=0, column=0, padx=6)

    btn_quit = tk.Button(frame_btn, text="Quitter", command=root.quit, font=font_text, bg=highlight_color, fg="white", width=10)
    btn_quit.grid(row=0, column=1, padx=6)

#######################################################################################################################
# Contrôle des propositions
def proposal(event):
    global mistake, storage, choice_letter, used_letter

    choice_letter = entry_letter.get().strip().upper()  # Récupère la lettre saisie
    entry_letter.delete(0, tk.END)  # Efface la saisie après validation

    if len(choice_letter) != 1:
        if list(choice_letter) == visible_word:
            # Met à jour l'affichage du mot
            label_letter.config(text=" ".join(choice_letter))
            #popup victoire
            show_end_popup(is_win=True)
            return

    # Contrôle : 1 lettre alpha
    if len(choice_letter) != 1 or not choice_letter.isalpha():
        return

    # Mauvaise lettre => erreur + update image et lettres utilisées
    if (choice_letter not in visible_word) and (choice_letter not in used_letter):
        mistake += 1
        used_letter.append(choice_letter)
        label_used_letter.config(text="Lettres déjà utilisées : " + " ".join(used_letter))
        update_pendu()

    # Met à jour l'affichage du mot
    storage = random_words(random_numero, choice_letter, storage)[1]
    label_letter.config(text=" ".join(storage))

    # Récupère le max d'erreurs autorisées (nombre d'images)
    mistake_max, _ = draw_pendu(mistake)

    # Victoire
    if storage == visible_word:
        show_end_popup(is_win=True)
        return

    # Défaite (dernière image atteinte)
    # Avec 11 images, on autorise erreur = 0..10 (10 mauvaises lettres)
    if mistake >= mistake_max - 1:
        show_end_popup(is_win=False)
        return

def hover_label(event):
    label_hint.config(text="indice: " + hint)

def quit_label(event):
    label_hint.config(text=hint_message)

# bind pour la gestion des événements
label_hint.bind("<Enter>", hover_label)
label_hint.bind("<Leave>", quit_label)
entry_letter.bind("<Return>", proposal)

#######################################################################################################################
root.mainloop()
