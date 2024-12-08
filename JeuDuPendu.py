# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:01:04 2024

@author: laure
"""

import random

def jeu_pendu(limite_essais, liste_mots):
    
    # On définit les variables
    mot_a_trouver = random.choice(liste_mots)
    mot_trouve = ["_"] * len(mot_a_trouver)  
    lettres_saisies = set()  
    essais = 0  
    points = 0
    indice_utilise = False

    # Cette fonction permet d'afficher un bâton supplémentaire du pendu à chaque mauvaise lettre
    def afficher_pendu(essais):
        dessin = [
            "",
            " O ",
            " O \n | ",
            " O \n/| ",
            " O \n/|\\",
            " O \n/|\\\n | ",
            " O \n/|\\\n | \n/  ",
            " O \n/|\\\n | \n/ \\",
        ]
        print("\nProgression du pendu:")
        if essais < len(dessin):
            print(dessin[essais])
        else:
            print(dessin[-1])
    
    # Affichage des textes généraux du jeu
    def afficher_texte_explicatif():
        print("Mot à deviner : " + " ".join(mot_trouve))
        print("Lettres déjà saisies : " + ", ".join(sorted(lettres_saisies)))
        print(f"Nombre d'essais restants : {limite_essais - essais}")
        print(f"Points actuels : {points}")

    # Cette fonction permet l'affichage d'une des lettres du mot si on le demande et qu'on a un nombre de points suffisant
    def donner_indice():
        nonlocal essais, indice_utilise
        if points >= 5:
            for i, char in enumerate(mot_a_trouver):
                if mot_trouve[i] == "_":
                    mot_trouve[i] = char
                    indice_utilise = True
                    break
            print("Indice utilisé ! Une lettre a été révélée.")
        else:
            print("Vous n'avez pas assez de points pour demander un indice.")

    # Début du jeu
    print("Bienvenue au jeu du pendu !")
    while essais < limite_essais and "_" in mot_trouve:
        afficher_texte_explicatif()
        # Le joueur choisit quoi faire via le menu
        print("Menu : S -->  Saisir une lettre \n  D --> Saisir le mot \n  I --> Indice")
        choix = input("Choisissez une option : ").upper()

        if choix == "S":
            lettre = input("Proposez une lettre : ").lower()

            # On vérifie que l'inout est bien une lettre
            if not lettre.isalpha() or len(lettre) != 1:
                print("Entrée invalide. Veuillez entrer une seule lettre.")
                continue
            # On empêche de saisir deux fois la même lettre
            if lettre in lettres_saisies:
                print(f"La lettre '{lettre}' a déjà été saisie. Essayez une autre.")  
            elif lettre in mot_a_trouver:
                lettres_saisies.add(lettre)
                for i, char in enumerate(mot_a_trouver):
                    # La lettre est bien dans le mot, gain de points
                    if char == lettre:
                        mot_trouve[i] = lettre
                points += 2
                print("Bonne lettre !")
            # La lettre n'est pas dans le mot, perte de points
            else:
                lettres_saisies.add(lettre)
                essais += 1  
                points = max(0, points - 2)
                print("Mauvaise lettre...")
                # Un trait se rajoute au bonhomme
                afficher_pendu(essais)

        # Option de remplir le mot en un coup
        elif choix == "D":
            mot_propose = input("Proposez le mot : ").lower()
            if mot_propose == mot_a_trouver:
                mot_trouve = list(mot_a_trouver)
                print("Félicitations, vous avez deviné le mot !")
                break
            else:
                essais += 1
                points = max(0, points - 3)
                print("Ce n'est pas le bon mot.")
                
        # Option de demande d'un indice cf la fonction précédente
        elif choix == "I":
            donner_indice()
            points = max(0, points - 5)

        else:
            print("Choix invalide. Veuillez choisir une option valide.")

    if "_" not in mot_trouve:
        print("\nFélicitations ! Vous avez trouvé le mot : " + mot_a_trouver)
    else:
        print("\nVous avez perdu. Le mot à trouver était : " + mot_a_trouver)

    print("Menu : C --> Continuer \n  A --> Arrêter")
    rejouer = input("Voulez-vous rejouer ? ").upper()
    
    # Recommencer une partie, on relance le jeu
    if rejouer == "C":
        jeu_pendu(limite_essais, liste_mots)

if __name__ == "__main__":
    liste_mots = ["gagne", "raptor", "bouteille", "endroit", "mer", "montagne", "extraordinaire", "possible", "python",
                  "jeu", "histoire", "cerveau", "violoncelle", "xylophone", "cactus", "asticot", "vaiselle", "yeti"]
    jeu_pendu(9, liste_mots)
