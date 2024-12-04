#Importer l'aléatoire
import random

#Initialiser les valeurs des cases du plateau 
def init():
    global a, b, c, d, e, f, g, h, i
    a, b, c, d, e, f, g, h, i = 1, 2, 3, 4, 5, 6, 7, 8, 9

init()

#Afficher le plateau
def plateau():
    print(f"""\033[1m
     {a if a not in [10, 11] else ('\033[1;31mX\033[0m' if a == 10 else '\033[1;34mO\033[0m')} | {b if b not in [10, 11] else ('\033[1;31mX\033[0m' if b == 10 else '\033[1;34mO\033[0m')} | {c if c not in [10, 11] else ('\033[1;31mX\033[0m' if c == 10 else '\033[1;34mO\033[0m')}
    ---|---|---
     {d if d not in [10, 11] else ('\033[1;31mX\033[0m' if d == 10 else '\033[1;34mO\033[0m')} | {e if e not in [10, 11] else ('\033[1;31mX\033[0m' if e == 10 else '\033[1;34mO\033[0m')} | {f if f not in [10, 11] else ('\033[1;31mX\033[0m' if f == 10 else '\033[1;34mO\033[0m')}
    ---|---|---
     {g if g not in [10, 11] else ('\033[1;31mX\033[0m' if g == 10 else '\033[1;34mO\033[0m')} | {h if h not in [10, 11] else ('\033[1;31mX\033[0m' if h == 10 else '\033[1;34mO\033[0m')} | {i if i not in [10, 11] else ('\033[1;31mX\033[0m' if i == 10 else '\033[1;34mO\033[0m')}
    """)

#Attribuer X ou O a une case
def jouer(symbole):
    global a, b, c, d, e, f, g, h, i
    k = int(input(f"Position de {symbole} entre 1 et 9 : "))
    z = [a, b, c, d, e, f, g, h, i]

    if z[k - 1] not in [10, 11]:
        z[k - 1] = 10 if symbole == "x" else 11
        a, b, c, d, e, f, g, h, i = z
    else:
        print("Position invalide ou déjà occupée.")
        jouer(symbole)

#vérifier si il y a une victoire ou un match nul
def victoire(symbole):
    if (
        a == b == c or d == e == f or g == h == i or
        a == d == g or b == e == h or c == f == i or
        a == e == i or g == e == c
    ):
        plateau()
        print(f"{symbole} à gagné")
        init()
    elif a + b + c + d + e + f + g + h + i >= 94:
        plateau()
        print("match nul")
        init()

#Lancer la boucle de jeu
def partie(symbole):
    plateau()
    jouer(symbole)
    victoire(symbole)


while True:
    partie("x")
    partie("o")



#a : 1ère case = 1
#b : 2ème case = 2
#c : 3ème case = 3
#d : 4ème case = 4
#e : 5ème case = 5
#f : 6ème case = 6
#g : 7ème case = 7
#h : 8ème case = 8
#i : 9ème case = 9
#x : joueur x = 10
#o : joueur o = 11
#k : input position du pions 
#m : input jouer avec un bot
#z : liste