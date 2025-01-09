def zahl_analyse(zahl):
    if zahl > 0:
        print(f"Die Zahl {zahl} ist positiv.")
        # Schleife zum Ausgeben der Zahlen von 1 bis zur eingegebenen Zahl
        for i in range(1, zahl + 1):
            print(i)
    elif zahl < 0:
        print(f"Die Zahl {zahl} ist negativ.")

    else:
        print(f"Die Zahl {zahl} ist 0.")

zahl_analyse(7)