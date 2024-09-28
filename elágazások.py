def elso():
    print("A program eldönti egy egész számról, hogy pozitív-e.")
    szam = int(input("Adjon meg egy számot:"))
    if szam>0:
        print("Ez egy pozitív szám.")

def masodik():
    szam = int(input("Adjon meg egy számot:"))
    if szam>=-9 and szam<=9:
        megelozo = szam-1
        kovetkezo = szam+1
        print("Az előző érték: "+str(megelozo)+" a következő érték: "+str(kovetkezo)+".")
