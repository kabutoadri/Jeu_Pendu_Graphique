#Auteur : Adriano Alves Morais, Marc Schilter
#Date : 15.12.2025
#Présentation du programme : Programme principal du jeu du pendu

import random
import function
import tkinter as tk

#Déclaration et initialisation des variables
erreur = 0
stockage = ""
game = True
rejouer = ""

numero_random = random.randint(0,9)
max_erreur = function.dessiner_pendu(erreur)[0] #Récuperation de la taille du pendu
#mot_visible = function.mots_aleatoires(numero_random, lettre, stockage)[0] #Récuperation du mot aléatoire

root = tk.Tk()
root.title("Pendu")

#Début du JEU
frame_User_Entry = tk.Frame(root)
frame_User_Entry.pack(side="top")
label_Instruction = tk.Label(frame_User_Entry, text="Choisis une lettre :")
label_Instruction.grid(row=0, column=0)
entry_Lettre = tk.Entry(frame_User_Entry)
entry_Lettre.grid(row=0, column=1)
label_Lettres = tk.Label(root, text=f"{" ".join(function.mots_aleatoires(numero_random, entry_Lettre.get().upper())[1])}")
label_Lettres.pack(side="top")
entry_Lettre.bind("<Return>", label_Lettres.config(text=f"{" ".join(function.mots_aleatoires(numero_random, entry_Lettre.get().upper())[1])}"))

root.mainloop()



while game:
    lettre = input("Choisis une lettre :\n").upper()
    #La lettre est bonne ?
    if lettre in str(mot_visible):
        stockage = function.mots_aleatoires(numero_random, lettre, stockage)[1] #affiche la bonne lettre
    else:
        print("Dommage, ce n'est pas la bonne lettre...\n")
        erreur += 1
        print(function.dessiner_pendu(erreur)[1])  #affiche l'erreur
    print(" ".join(stockage))

    #Fin de la partie
    if erreur == max_erreur or stockage == mot_visible:
        if erreur == max_erreur:
            print("\nGAME OVER !\n")
        else:
            print("\nWIN !\n")

        #Choix de l'utilisateur pour quitter ou rejouer
        rejouer = input("Voulez-vous rejouez ? (Y/N) : ").upper()
        while rejouer not in ["Y", "N"]:
            print("Ouupss... Mauvaise touche... Merci d'appuyer sur Y ou N.\n")
            rejouer = input("Voulez-vous rejouez ? (Y/N) : ").upper()

        #Quitter ou non ?
        if rejouer == "N":
            game = False
            print("\nMerci d'avoir joué et à la prochaine !\n")
        else:
            #Réinitialisation du jeu
            erreur = 0
            stockage = ""
            lettre = ""
            numero_random = random.randint(0, 9)
            mot_visible = function.mots_aleatoires(numero_random, lettre, stockage)[0]
            rejouer = ""
            print("\nVous rejouez ? Parfait ! \n\nnous allons vous sélectionner un nouveau mot aléatoire\n")
            print(" ".join(function.mots_aleatoires(numero_random, lettre, stockage)[1]), "\n")