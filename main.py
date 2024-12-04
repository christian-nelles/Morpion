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