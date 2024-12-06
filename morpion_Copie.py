#Importer l'aléatoire
import random
import json

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
        if m == 2 and  difficulte == 3:
            init()
            partie("x")
        else:
            init()

#Lancer la boucle de jeu
def partie(symbole):
    if m == 2 and symbole == "o":
        victoire(symbole)
        partie_bot()
    plateau()
    jouer(symbole)
    victoire(symbole)

#Choisir la difficulté du bot 
def choix_difficulte():
    print("Choisissez un niveau de difficulté :")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    
    difficulte = input("Entrez un chiffre (1, 2 ou 3): ")
    
    if difficulte == '1':
        return 1  # Facile
    elif difficulte == '2':
        return 2  # Moyen
    else:
        return 3  # Difficile

#Choisir une case libre pour le bot selon sa difficulté
def bot(difficulte):
    global a, b, c, d, e, f, g, h, i
    positions_libres = [a, b, c, d, e, f, g, h, i]
    positions_libres = [p for p in [a, b, c, d, e, f, g, h, i] if p not in [10, 11]]
    
    if difficulte == 1:
        mouvement = random.choice(positions_libres)
    
    elif difficulte == 2:
        if a == b and c not in [10, 11]:
            mouvement = c
        elif a == c and b not in [10, 11]:
            mouvement = b
        elif b == c and a not in [10, 11]:
            mouvement = a
        elif d == e and f not in [10, 11]:
            mouvement = f
        elif d == f and e not in [10, 11]:
            mouvement = e
        elif e == f and d not in [10, 11]:
            mouvement = d
        elif g == h and i not in [10, 11]:
            mouvement = i
        elif g == i and h not in [10, 11]:
            mouvement = h
        elif h == i and g not in [10, 11]:
            mouvement = g
        elif a == d and g not in [10, 11]:
            mouvement = g
        elif a == g and d not in [10, 11]:
            mouvement = d
        elif d == g and a not in [10, 11]:
            mouvement = a
        elif b == e and h not in [10, 11]:
            mouvement = h
        elif b == h and e not in [10, 11]:
            mouvement = e
        elif e == h and b not in [10, 11]:
            mouvement = b
        elif c == f and i not in [10, 11]:
            mouvement = i
        elif c == i and f not in [10, 11]:
            mouvement = f
        elif f == i and c not in [10, 11]:
            mouvement = c
        elif a == e and i not in [10, 11]:
            mouvement = i
        elif a == i and e not in [10, 11]:
            mouvement = e
        elif e == i and a not in [10, 11]:
            mouvement = a
        elif c == e and g not in [10, 11]:
            mouvement = g
        elif c == g and e not in [10, 11]:
            mouvement = e
        elif e == g and c not in [10, 11]:
            mouvement = c
        else:
            mouvement = random.choice(positions_libres)

    elif difficulte == 3:
        if a == b and c not in [10, 11]:
            mouvement = c
        elif a == c and b not in [10, 11]:
            mouvement = b
        elif b == c and a not in [10, 11]:
            mouvement = a
        elif d == e and f not in [10, 11]:
            mouvement = f
        elif d == f and e not in [10, 11]:
            mouvement = e
        elif e == f and d not in [10, 11]:
            mouvement = d
        elif g == h and i not in [10, 11]:
            mouvement = i
        elif g == i and h not in [10, 11]:
            mouvement = h
        elif h == i and g not in [10, 11]:
            mouvement = g
        elif a == d and g not in [10, 11]:
            mouvement = g
        elif a == g and d not in [10, 11]:
            mouvement = d
        elif d == g and a not in [10, 11]:
            mouvement = a
        elif b == e and h not in [10, 11]:
            mouvement = h
        elif b == h and e not in [10, 11]:
            mouvement = e
        elif e == h and b not in [10, 11]:
            mouvement = b
        elif c == f and i not in [10, 11]:
            mouvement = i
        elif c == i and f not in [10, 11]:
            mouvement = f
        elif f == i and c not in [10, 11]:
            mouvement = c
        elif a == e and i not in [10, 11]:
            mouvement = i
        elif a == i and e not in [10, 11]:
            mouvement = e
        elif e == i and a not in [10, 11]:
            mouvement = a
        elif c == e and g not in [10, 11]:
            mouvement = g
        elif c == g and e not in [10, 11]:
            mouvement = e
        elif e == g and c not in [10, 11]:
            mouvement = c
        elif e not in [10, 11]:
            mouvement = e
        elif a not in [10, 11]:
            mouvement = a
        else:
            mouvement = random.choice(positions_libres)
    
    if mouvement == a:
        a = 11
    elif mouvement == b:
        b = 11
    elif mouvement == c:
        c = 11
    elif mouvement == d:
        d = 11
    elif mouvement == e:
        e = 11
    elif mouvement == f:
        f = 11
    elif mouvement == g:
        g = 11
    elif mouvement == h:
        h = 11
    elif mouvement == i:
        i = 11

#Lancer la boucle du bot
def partie_bot():
    partie("x")
    bot(difficulte)
    partie("o")

#LE DEBUT DU SCRIPT VISUEL

#Choisir le bot ou pas
reponse = {"non": 1, "Non": 1, "NON": 1, "oui": 2, "Oui": 2, "OUI": 2,}
texte = input("Jouer avec un Bot ? ")
m = reponse.get(texte, "Valeur non définie")

#Jouer sans le bot
if m == 1:
    while True:
        partie("x")
        partie("o")

#Jouer avec le bot
if m == 2:
    difficulte = choix_difficulte()
    partie_bot()



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