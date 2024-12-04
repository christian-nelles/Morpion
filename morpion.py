def afficher_grille(grille):
    for ligne in grille:
        print("|".join(ligne))
        print("-" * 5)

def verifier_victoire(grille, joueur):
    # Vérifier les lignes
    for ligne in grille:
        if all(s == joueur for s in ligne):
            return True
    # Vérifier les colonnes
    for col in range(3):
        if all(grille[ligne][col] == joueur for ligne in range(3)):
            return True
    # Vérifier les diagonales
    if all(grille[i][i] == joueur for i in range(3)):
        return True
    if all(grille[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def jeu_morpion():
    # Initialiser la grille de jeu
    grille = [[" " for _ in range(3)] for _ in range(3)]
    joueur_actuel = "X"
    tours = 0

    while tours < 9:
        # Afficher la grille actuelle
        afficher_grille(grille)
        try:
            ligne = int(input(f"Joueur {joueur_actuel}, entrez la ligne (0, 1, 2) : "))
            col = int(input(f"Joueur {joueur_actuel}, entrez la colonne (0, 1, 2) : "))
            
            if 0 <= ligne < 3 and 0 <= col < 3:  # Vérifier si l'entrée est valide
                if grille[ligne][col] == " ":
                    grille[ligne][col] = joueur_actuel
                    if verifier_victoire(grille, joueur_actuel):
                        afficher_grille(grille)
                        print(f"Joueur {joueur_actuel} gagne!")
                        return
                    joueur_actuel = "O" if joueur_actuel == "X" else "X"
                    tours += 1
                else:
                    print("Case déjà occupée. Choisissez une autre case.")
            else:
                print("Entrée non valide. Choisissez des valeurs entre 0 et 2.")
        except ValueError:
            print("Entrée non valide. Veuillez entrer des nombres.")

    afficher_grille(grille)
    print("Match nul!")

# Lancer le jeu
jeu_morpion()




         