#Auteur : Adriano Alves Morais, Marc Schilter
#Date : 16.09.2025
#Présentation du programme : Fichier Fonction pour le programme du jeu du pendu

#Fonction mot aléatoire
def mots_aleatoires(aleatoire,lettre):
    listes = ["python", "ordinateur", "jeu", "random", "chat", "chien", "soleil", "lune", "code", "apprentissage"]

    mot_mystere = list(listes[aleatoire].upper())

    if lettre == "":
        mot_affiche = ["_ "] * len(mot_mystere)
        print("oui")
    else:
        mot_affiche = lettre
        print("non")

    for i, char in enumerate(mot_mystere):
         if char == lettre:
            mot_affiche[i] = lettre

    return mot_mystere, mot_affiche

######################################################################################################################

#Fonction dessin du pendu
def dessiner_pendu(erreur):
    #liste avec les etapes du pendu
    etapes_pendu =\
    [
        """
            |
            |
        ____|___""",
        """
            |
            |
            |
            |
            |
        ____|___""",
        """
             _______
            |/      |
            |
            |
            |
            |
            |
        ____|___""",
        """
             _______
            |/      |
            |      (_)
            |
            |
            |
            |
        ____|___""",
        """
             _______
            |/      |
            |      (_)
            |      \\|/
            |
            |
            |
        ____|___""",
        """
             _______
            |/      |
            |      (_)
            |      \\|/
            |       |
            |
            |
        ____|___""",
        """
             _______
            |/      |
            |      (_)
            |      \\|/
            |       |
            |      / \\
            |
        ____|___"""
    ]
    #Retourne le bon affichage et le nombre max d'erreur
    return len(etapes_pendu), etapes_pendu[erreur - 1]