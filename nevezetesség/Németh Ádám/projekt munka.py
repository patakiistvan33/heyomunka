orszagnevezetessegek = []

with open(nevezetesegek.txt)
    for line in n:
        orszag, varos, nevezetessegek = line.split(,).strip()
        orszagnevezetessegek.append(orszag, varos, nevezetessegek)

while True:
    print("\nHello üdv itt a programban, kérlek szépen válasz ki egy menü pontot.\n1. Országok nevezetességei\n2 városokban lévő nevezetességek az országokon belül.\n3. Összes nevezetesség listája")

    menupont = int(input("\Ide írja be a kapott sorszámot a kiválasztott a menüpontból"))

    if menupont == 1:
        nevezetessegeklistaja = set([x[0] for x in orszagnevezetessegek])
        for orszagnevezetesseg in nevezetessegeklistaja:
            nevezetessegek-lista = [n[0] for n in orszagnevezetessegek if n[0] == orszagnevezetesseg]
            print(nevezetessegek-lista)
    elif menupont == 2:
        kivalasztott-varos = input("\nKérem válasszon egy várost: ")
        for orszag, varos, nevezetessegek in orszagnevezetessegek:
            if varos == kivalasztott-varos:
                print(f"{nevezetessegek} - {orszag}")

    elif menupont == 3:
        orszagok = set([n[1] for n in orszagnevezetessegek])
        kivalasztott_orszag = input("\Kérem vélasszon egy országot: ")
        for orszagnevezetesseg in orszagnevezetessegek:
            if orszagnevezetesseg[1] = kivalasztott_orszag:
                print(orszagnevezetessegek[0])

    else:
        print("\nEz nem létezik,kérem válasz egy olyan menüpontot ami létezik.\n")
        
