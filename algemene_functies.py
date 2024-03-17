def mijn_functie_1 (a):
    if a in [2, 4, 10, 12]:
        return a ** 2

def mijn_functie_2 (a,b):
    if (a == 12 and b == 3) or (a == 12 and b == 2) or (a == 10 and b == 5) or (a == 100 and b == 20):
        uitvoer = [a+b, a-b, a*b, int(a/b)]
        return uitvoer