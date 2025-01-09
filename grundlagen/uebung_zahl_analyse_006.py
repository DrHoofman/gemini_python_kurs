def zahl_analyse():
  # Benutzeraufforderung zur Eingabe einer Zahl
    zahl = int(input("Bitte gib eine Zahl ein: "))

    if zahl > 0:
        print(f"Die Zahl {zahl} ist positiv.")
        # Schleife zum Ausgeben der Zahlen von 1 bis zur eingegebenen Zahl
        for i in range(1, zahl + 1):
            print(i)
    elif zahl < 0:
        print(f"Die Zahl {zahl} ist negativ.")

    else:
        print(f"Die Zahl {zahl} ist 0.")

zahl_analyse()