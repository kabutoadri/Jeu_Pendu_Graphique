#Auteur : Adriano Alves Morais, Marc Schilter
#Date : 16.09.2025
#Présentation du programme : Fichier Fonction pour le programme du jeu du pendu

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