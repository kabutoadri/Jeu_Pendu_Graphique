#Auteur : Adriano Alves Morais, Kodjo Attivon
#Date : 16.09.2025
#Présentation du programme : Programme principal du jeu du pendu

import random
import function

#Déclaration et initialisation des variables
erreur = 0
stockage = ""
lettre = ""
game = True
rejouer = ""

numero_random = random.randint(0,9)
max_erreur = function.dessiner_pendu(erreur)[0] #Récuperation de la taille du pendu
mot_visible = function.mots_aleatoires(numero_random, lettre, stockage)[0] #Récuperation du mot aléatoire

#Début du JEU
print("\nBienvenue au jeu de Pendu ! \n\nnous allons vous sélectionner un mot aléatoire\n")
print(" ".join(function.mots_aleatoires(numero_random, lettre, stockage)[1]), "\n")

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