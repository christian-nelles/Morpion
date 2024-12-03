
import random
reponse = {
    "non": 1,
    "Non": 1,
    "NON": 1,
    "oui": 2,
    "Oui": 2,
    "OUI": 2,
}

texte = input("Jouer avec un Bot ? ")

m = reponse.get(texte, "Valeur non définie")

if m == 1:
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    x = 10
    o = 11
    while True:
        print(f"""
         {a if a not in [10, 11] else ('X' if a == 10 else 'O')} | {b if b not in [10, 11] else ('X' if b == 10 else 'O')} | {c if c not in [10, 11] else ('X' if c == 10 else 'O')}
        ---|---|---
         {d if d not in [10, 11] else ('X' if d == 10 else 'O')} | {e if e not in [10, 11] else ('X' if e == 10 else 'O')} | {f if f not in [10, 11] else ('X' if f == 10 else 'O')}
        ---|---|---
         {g if g not in [10, 11] else ('X' if g == 10 else 'O')} | {h if h not in [10, 11] else ('X' if h == 10 else 'O')} | {i if i not in [10, 11] else ('X' if i == 10 else 'O')}
        """)
        
        if a == b == c or d == e == f or g == h == i or a == d == g or b == e == h or c == f == i or a == e == i or g == e == c:
            print("O à gagné")
            break
        elif a+b+c+d+e+f+g+h+i == 95:
            print("match nul")
            a = 1
            b = 2
            c = 3
            d = 4
            e = 5
            f = 6
            g = 7
            h = 8
            i = 9
            print(f"""
         {a if a not in [10, 11] else ('X' if a == 10 else 'O')} | {b if b not in [10, 11] else ('X' if b == 10 else 'O')} | {c if c not in [10, 11] else ('X' if c == 10 else 'O')}
        ---|---|---
         {d if d not in [10, 11] else ('X' if d == 10 else 'O')} | {e if e not in [10, 11] else ('X' if e == 10 else 'O')} | {f if f not in [10, 11] else ('X' if f == 10 else 'O')}
        ---|---|---
         {g if g not in [10, 11] else ('X' if g == 10 else 'O')} | {h if h not in [10, 11] else ('X' if h == 10 else 'O')} | {i if i not in [10, 11] else ('X' if i == 10 else 'O')}
        """)
        
        k = int(input("position de X entre 1 et 9 : "))
        if k == 1 and a not in [10, 11]:
            a = 10
        elif k == 2 and b not in [10, 11]:
            b = 10
        elif k == 3 and c not in [10, 11]:
            c = 10
        elif k == 4 and d not in [10, 11]:
            d = 10
        elif k == 5 and e not in [10, 11]:
            e = 10
        elif k == 6 and f not in [10, 11]:
            f = 10
        elif k == 7 and g not in [10, 11]:
            g = 10
        elif k == 8 and h not in [10, 11]:
            h = 10
        elif k == 9 and i not in [10, 11]:
            i = 10
        else:
            print("valeur invalide ou deja prise")
            k = int(input("dernière chance : "))
            if k == 1 and a not in [10, 11]:
                a = 10
            elif k == 2 and b not in [10, 11]:
                b = 10
            elif k == 3 and c not in [10, 11]:
                c = 10
            elif k == 4 and d not in [10, 11]:
                d = 10
            elif k == 5 and e not in [10, 11]:
                e = 10
            elif k == 6 and f not in [10, 11]:
                f = 10
            elif k == 7 and g not in [10, 11]:
                g = 10
            elif k == 8 and h not in [10, 11]:
                h = 10
            elif k == 9 and i not in [10, 11]:
                i = 10
            else:
                print("seul une valeur entre 1 et 9 qui n'as pas deja été prise")
            
        print(f"""
         {a if a not in [10, 11] else ('X' if a == 10 else 'O')} | {b if b not in [10, 11] else ('X' if b == 10 else 'O')} | {c if c not in [10, 11] else ('X' if c == 10 else 'O')}
        ---|---|---
         {d if d not in [10, 11] else ('X' if d == 10 else 'O')} | {e if e not in [10, 11] else ('X' if e == 10 else 'O')} | {f if f not in [10, 11] else ('X' if f == 10 else 'O')}
        ---|---|---
         {g if g not in [10, 11] else ('X' if g == 10 else 'O')} | {h if h not in [10, 11] else ('X' if h == 10 else 'O')} | {i if i not in [10, 11] else ('X' if i == 10 else 'O')}
        """)
        
        if a == b == c or d == e == f or g == h == i or a == d == g or b == e == h or c == f == i or a == e == i or g == e == c:
            print("X à gagné")
            break
        elif a+b+c+d+e+f+g+h+i == 94:
            print("match nul")
            a = 1
            b = 2
            c = 3
            d = 4
            e = 5
            f = 6
            g = 7
            h = 8
            i = 9
            print(f"""
         {a if a not in [10, 11] else ('X' if a == 10 else 'O')} | {b if b not in [10, 11] else ('X' if b == 10 else 'O')} | {c if c not in [10, 11] else ('X' if c == 10 else 'O')}
        ---|---|---
         {d if d not in [10, 11] else ('X' if d == 10 else 'O')} | {e if e not in [10, 11] else ('X' if e == 10 else 'O')} | {f if f not in [10, 11] else ('X' if f == 10 else 'O')}
        ---|---|---
         {g if g not in [10, 11] else ('X' if g == 10 else 'O')} | {h if h not in [10, 11] else ('X' if h == 10 else 'O')} | {i if i not in [10, 11] else ('X' if i == 10 else 'O')}
        """)

        k = int(input("position de O entre 1 et 9 : "))
        if k == 1 and a not in [10, 11]:
            a = 11
        elif k == 2 and b not in [10, 11]:
            b = 11
        elif k == 3 and c not in [10, 11]:
            c = 11
        elif k == 4 and d not in [10, 11]:
            d = 11
        elif k == 5 and e not in [10, 11]:
            e = 11
        elif k == 6 and f not in [10, 11]:
            f = 11
        elif k == 7 and g not in [10, 11]:
            g = 11
        elif k == 8 and h not in [10, 11]:
            h = 11
        elif k == 9 and i not in [10, 11]:
            i = 11
        else:
            print("valeur invalide ou deja prise")
            k = int(input("dernière chance : "))
            if k == 1 and a not in [10, 11]:
                a = 10
            elif k == 2 and b not in [10, 11]:
                b = 10
            elif k == 3 and c not in [10, 11]:
                c = 10
            elif k == 4 and d not in [10, 11]:
                d = 10
            elif k == 5 and e not in [10, 11]:
                e = 10
            elif k == 6 and f not in [10, 11]:
                f = 10
            elif k == 7 and g not in [10, 11]:
                g = 10
            elif k == 8 and h not in [10, 11]:
                h = 10
            elif k == 9 and i not in [10, 11]:
                i = 10
            else:
                print("seul une valeur entre 1 et 9 qui n'as pas deja été prise")

elif m == 2:
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    x = 10
    o = 11
    while True:
        print(f"""
         {a if a not in [10, 11] else ('X' if a == 10 else 'O')} | {b if b not in [10, 11] else ('X' if b == 10 else 'O')} | {c if c not in [10, 11] else ('X' if c == 10 else 'O')}
        ---|---|---
         {d if d not in [10, 11] else ('X' if d == 10 else 'O')} | {e if e not in [10, 11] else ('X' if e == 10 else 'O')} | {f if f not in [10, 11] else ('X' if f == 10 else 'O')}
        ---|---|---
         {g if g not in [10, 11] else ('X' if g == 10 else 'O')} | {h if h not in [10, 11] else ('X' if h == 10 else 'O')} | {i if i not in [10, 11] else ('X' if i == 10 else 'O')}
        """)
        
        if a == b == c or d == e == f or g == h == i or a == d == g or b == e == h or c == f == i or a == e == i or g == e == c:
            print("O à gagné")
            break
        elif a+b+c+d+e+f+g+h+i == 95:
            print("match nul")
            a = 1
            b = 2
            c = 3
            d = 4
            e = 5
            f = 6
            g = 7
            h = 8
            i = 9
            print(f"""
         {a if a not in [10, 11] else ('X' if a == 10 else 'O')} | {b if b not in [10, 11] else ('X' if b == 10 else 'O')} | {c if c not in [10, 11] else ('X' if c == 10 else 'O')}
        ---|---|---
         {d if d not in [10, 11] else ('X' if d == 10 else 'O')} | {e if e not in [10, 11] else ('X' if e == 10 else 'O')} | {f if f not in [10, 11] else ('X' if f == 10 else 'O')}
        ---|---|---
         {g if g not in [10, 11] else ('X' if g == 10 else 'O')} | {h if h not in [10, 11] else ('X' if h == 10 else 'O')} | {i if i not in [10, 11] else ('X' if i == 10 else 'O')}
        """)
        
        k = int(input("position de X entre 1 et 9 : "))
        if k == 1 and a not in [10, 11]:
            a = 10
        elif k == 2 and b not in [10, 11]:
            b = 10
        elif k == 3 and c not in [10, 11]:
            c = 10
        elif k == 4 and d not in [10, 11]:
            d = 10
        elif k == 5 and e not in [10, 11]:
            e = 10
        elif k == 6 and f not in [10, 11]:
            f = 10
        elif k == 7 and g not in [10, 11]:
            g = 10
        elif k == 8 and h not in [10, 11]:
            h = 10
        elif k == 9 and i not in [10, 11]:
            i = 10
        else:
            print("valeur invalide ou deja prise")
            k = int(input("dernière chance : "))
            if k == 1 and a not in [10, 11]:
                a = 10
            elif k == 2 and b not in [10, 11]:
                b = 10
            elif k == 3 and c not in [10, 11]:
                c = 10
            elif k == 4 and d not in [10, 11]:
                d = 10
            elif k == 5 and e not in [10, 11]:
                e = 10
            elif k == 6 and f not in [10, 11]:
                f = 10
            elif k == 7 and g not in [10, 11]:
                g = 10
            elif k == 8 and h not in [10, 11]:
                h = 10
            elif k == 9 and i not in [10, 11]:
                i = 10
            else:
                print("seul une valeur entre 1 et 9 qui n'as pas deja été prise")
            
        print(f"""
         {a if a not in [10, 11] else ('X' if a == 10 else 'O')} | {b if b not in [10, 11] else ('X' if b == 10 else 'O')} | {c if c not in [10, 11] else ('X' if c == 10 else 'O')}
        ---|---|---
         {d if d not in [10, 11] else ('X' if d == 10 else 'O')} | {e if e not in [10, 11] else ('X' if e == 10 else 'O')} | {f if f not in [10, 11] else ('X' if f == 10 else 'O')}
        ---|---|---
         {g if g not in [10, 11] else ('X' if g == 10 else 'O')} | {h if h not in [10, 11] else ('X' if h == 10 else 'O')} | {i if i not in [10, 11] else ('X' if i == 10 else 'O')}
        """)
        
        if a == b == c or d == e == f or g == h == i or a == d == g or b == e == h or c == f == i or a == e == i or g == e == c:
            print("X à gagné")
            break
        elif a+b+c+d+e+f+g+h+i == 94:
            print("match nul")
            a = 1
            b = 2
            c = 3
            d = 4
            e = 5
            f = 6
            g = 7
            h = 8
            i = 9
            print(f"""
         {a if a not in [10, 11] else ('X' if a == 10 else 'O')} | {b if b not in [10, 11] else ('X' if b == 10 else 'O')} | {c if c not in [10, 11] else ('X' if c == 10 else 'O')}
        ---|---|---
         {d if d not in [10, 11] else ('X' if d == 10 else 'O')} | {e if e not in [10, 11] else ('X' if e == 10 else 'O')} | {f if f not in [10, 11] else ('X' if f == 10 else 'O')}
        ---|---|---
         {g if g not in [10, 11] else ('X' if g == 10 else 'O')} | {h if h not in [10, 11] else ('X' if h == 10 else 'O')} | {i if i not in [10, 11] else ('X' if i == 10 else 'O')}
        """)
            
        positions_libres = [a, b, c, d, e, f, g, h, i]

        winning_combinations = [
            [a, b, c], [d, e, f], [g, h, i],  
            [a, d, g], [b, e, h], [c, f, i], 
            [a, e, i], [c, e, g]               
        ]
            
                
        blocage = None
        adversaire = 10 
        for combo in winning_combinations:
            if combo.count(adversaire) == 2 and combo.count(None) == 1:
                blocage = combo.index(None)
                break

        if blocage is not None:
            bot_move = blocage
        else:
            positions_libres = [p for p in [a, b, c, d, e, f, g, h, i] if p not in [10, 11]]
            bot_move = random.choice(positions_libres)

        if bot_move == a:
            a = 11
        elif bot_move == b:
            b = 11
        elif bot_move == c:
            c = 11
        elif bot_move == d:
            d = 11
        elif bot_move == e:
            e = 11
        elif bot_move == f:
            f = 11
        elif bot_move == g:
            g = 11
        elif bot_move == h:
            h = 11
        elif bot_move == i:
            i = 11

else:
    print("Utilisez une syntaxe valide")
    
    
    
    
    
    
    
    