#Auteur : Adriano Alves Morais, Kodjo Attivon
#Date : 16.09.2025
#Présentation du programme : Fichier Fonction pour le programme du jeu du pendu


def mots_aleatoires(aleatoire,lettre, vide):
    listes = ["python", "ordinateur", "jeu", "random", "chat", "chien", "soleil", "lune", "code", "apprentissage"]

    mot_mystere = list(listes[aleatoire].upper())

    if vide == "":
        mot_affiche = ["_ "] * len(mot_mystere)
    else:
        mot_affiche = vide

    for i, char in enumerate(mot_mystere):
         if char == lettre:
            mot_affiche[i] = lettre

    return mot_mystere, mot_affiche

######################################################################################################################

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
    # erreur = 0 => on affiche la 1ère image (état initial)
    idx = min(erreur, max_erreur - 1)
    return max_erreur, etapes_pendu[idx]
