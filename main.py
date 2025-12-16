#Auteur : Adriano Alves Morais, Marc Schilter
#Date : 15.12.2025
#Présentation du programme : Programme principal du jeu du pendu

#importation de librairie
import random
import tkinter as tk

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

#initialisation des variables
erreur = 0
lettre_choisi = ""
numero_random = random.randint(0,9)
stockage = mots_aleatoires(numero_random, "", "")[1]

#max_erreur = function.dessiner_pendu(erreur)[0] #Récuperation de la taille du pendu
mot_visible = mots_aleatoires(numero_random, lettre_choisi, stockage)[0] #Récuperation du mot aléatoire

root = tk.Tk()
root.title("Pendu")

#Début du JEU
frame_User_Entry = tk.Frame(root)
frame_User_Entry.pack(side="top")

label_Instruction = tk.Label(frame_User_Entry, text="Choisis une lettre :")
label_Instruction.grid(row=0, column=0)

entry_Lettre = tk.Entry(frame_User_Entry)
entry_Lettre.grid(row=0, column=1)
entry_Lettre.focus()

label_Lettres = tk.Label(root, text=f"{" ".join(stockage)}")
label_Lettres.pack(side="top")

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

    #stocke et affiche les traits avec la bonne lettre si besoin
    stockage = mots_aleatoires(numero_random, lettre_choisi, stockage)[1]
    label_Lettres.config(text=" ".join(stockage))

entry_Lettre.bind("<Return>", proposition)

root.mainloop()