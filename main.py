grille = {   #C'est la liste qui va permettre de print la grille
    "ligne1": [" ", " ", " "],
    "ligne2": [" ", " ", " "], 
    "ligne3": [" ", " ", " "]
}

def printer_jeu():   #c'est ce qui permet de print toute la grille de jeu avec une fonction
    print(grille["ligne1"])
    print(grille["ligne2"])
    print(grille["ligne3"])

def verifier_victoire(grille): #C'est le code qui vérifie la victoire de quelqu'un 
    for i in range(1, 4):
        ligne = grille[f"ligne{i}"]
        if ligne[0] == ligne[1] == ligne[2] != " ":
            return True
    for col in range(3):
        if (grille["ligne1"][col] == grille["ligne2"][col] == grille["ligne3"][col] != " "):
            return True
    if grille["ligne1"][0] == grille["ligne2"][1] == grille["ligne3"][2] != " ":
        return True
    if grille["ligne1"][2] == grille["ligne2"][1] == grille["ligne3"][0] != " ":
        return True
    return False
def est_case_vide(grille, ligne, colonne):
    return grille[f"ligne{ligne}"][colonne] == " "
def coup_robot(grille):
    for ligne in range(1, 4): #Le code check toute les cases libre
        for colonne in range(3):
            if est_case_vide(grille, ligne, colonne): #Ce code permet a O de vérifié si il O peux gagné
                grille[f"ligne{ligne}"][colonne] = "O"
                if verifier_victoire(grille):
                    grille[f"ligne{ligne}"][colonne] = " "
                    return ligne, colonne
                grille[f"ligne{ligne}"][colonne] = " "
    for ligne in range(1, 4): #Ce code permet de vérifié si X va gagné (Genre si y'a 2 case X a côté ça va bloqué directe)
        for colonne in range(3):
            if est_case_vide(grille, ligne, colonne):
                grille[f"ligne{ligne}"][colonne] = "X"
                if verifier_victoire(grille):
                    grille[f"ligne{ligne}"][colonne] = " "
                    return ligne, colonne
                grille[f"ligne{ligne}"][colonne] = " "

    if est_case_vide(grille, 2, 1): # Ce code c'est pour qu'il prenne directe le centre si le robot peux
        return 2, 1
    coins = [(1, 0), (1, 2), (3, 0), (3, 2)] #ce code c'est pour que le bot prend les coins si il sont vide
    for ligne, colonne in coins:
        if est_case_vide(grille, ligne, colonne):
            return ligne, colonne
    for ligne in range(1, 4):   #C'est ce qui permet au robot de prendre une case aléatoire
        for colonne in range(3):
            if est_case_vide(grille, ligne, colonne):
                return ligne, colonne

while True: #Cette boucle sert a choisir si on joue contre un autre joueur ou le robot
    mode = input("Choisissez votre mode de jeu:\n1 - Joueur contre Joueur\n2 - Joueur contre Robot\nVotre choix (1 ou 2): ")
    if mode in ["1", "2"]:
        break
    print("Choix invalide! Veuillez entrer 1 ou 2.")
mode_robot = (mode == "2")
if mode_robot:
    print("\nVous allez jouer contre le robot!")
else:
    print("\nMode 2 joueurs sélectionné!")
print("\nGrille initiale:")
printer_jeu()
isEnded = False
joueur_actuel = "X"
nombre_coups = 0
while isEnded == False:
    print(f"\nC'est au tour du joueur {joueur_actuel}")
    if mode_robot and joueur_actuel == "O":
        print("Tour du robot")
        ligne, colonne = coup_robot(grille)
        grille[f"ligne{ligne}"][colonne] = "O"
        nombre_coups += 1
        if verifier_victoire(grille):
            print("\nLe robot a gagné!")
            isEnded = True
        else:
            joueur_actuel = "X"
    else:
        ligne = int(input("Entrez le numéro de la ligne (1, 2 ou 3): "))
        colonne = int(input("Entrez le numéro de la colonne (0, 1 ou 2): "))
        if ligne >= 1 and ligne <= 3 and colonne >= 0 and colonne <= 2:
            if est_case_vide(grille, ligne, colonne):
                grille[f"ligne{ligne}"][colonne] = joueur_actuel
                nombre_coups += 1
                if verifier_victoire(grille):
                    print(f"\nFélicitations! Le joueur {joueur_actuel} a gagné!")
                    isEnded = True
                else:
                    joueur_actuel = "O" if joueur_actuel == "X" else "X"
            else:
                print("Cette case est déjà occupée! Choisissez une autre case.")
        else:
            print("Coordonnées invalides! Réessayez.")
    
    if nombre_coups == 9 and not isEnded:
        print("\nMatch nul!")
        isEnded = True

    print("\nGrille mise à jour:")
    printer_jeu()