i=0
while i<=1:

    print("Das ist ein sehr einfacher Taschenrechner")
    print("Dieser Taschenrechner kann +,-,* oder /")
    rechenop=input("Hier eingeben ob du +.-.* oder / rechnen möchtest:  ")
    zahl1=input("Die erste Zahl: ")
    zahl2=input("Die zweite Zahl: ")
    if rechenop == "+":
        ergebnis=int(zahl1)+int(zahl2)
        print("Das Ergebnis ist:" , ergebnis)

    if rechenop == "-":
        ergebnis=int(zahl1)-int(zahl2)
        print("Das Ergebnis ist:" , ergebnis)

    if rechenop == "*":
        ergebnis=int(zahl1)*int(zahl2)
        print("Das Ergebnis ist:" , ergebnis)

    if rechenop == "/":
        ergebnis=int(zahl1)/int(zahl2)
        print("Das Ergebnis ist:" , ergebnis)
       
