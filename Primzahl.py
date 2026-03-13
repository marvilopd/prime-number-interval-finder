def primzahl(zahl):
    # consider only integers greater than 1 as prime
    if zahl < 2:
        return False
    if zahl == 2:
        return True
    # check divisibility up to the square root
    for i in range(2, int(zahl**0.5) + 1):
        if zahl % i == 0:
            return False
    return True
def eingabe():
    print("Ich ermittele alle Primzahlen inn einem Intervall")
    a = int(input("Untere Intervallgrenze: "))
    b = int(input("Obere Intervallgrenze: "))
    return(a, b)
def verarbeitung(Intervall):
    prim = []
    for i in range(Intervall[0], Intervall[1] + 1):
        if primzahl(i):
            prim.append(i)    # store the prime itself, not 1
    return prim
def ausgabe(primzahlen):
    print("Primzahlen: ")
    for zahl in primzahlen:
        print(zahl, end=" ")

Intervall = eingabe()
primzahlListe = verarbeitung(Intervall)
ausgabe(primzahlListe)