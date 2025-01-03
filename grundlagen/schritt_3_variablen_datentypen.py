def quadriere_zahl(zahl):
    return zahl ** 2

ergebnis = quadriere_zahl(4)
print(f"\nDas Quadrat von 4 ist: {ergebnis}")

# Eine Liste mit verschiedenen zahlen erstellen
zahlen = [1, 2, 3, 4, 5]

# Die gesamte Liste ausgeben
print("\nDie Liste der Zahlen:", zahlen)
# Zugriff auf einzelne Elemente der Liste (Index beginnt bei 0)
print("Das erste Element der Liste:", zahlen[0])
print("Das dritte Element der Liste:", zahlen[2])

# Letztes Element ausgeben (negativer Index)
print("Das letzte Element der Liste:", zahlen[-1])

# Einen Wert zur Liste hinzufügen
zahlen.append(6)
print("\nDie Liste der Zahlen nach dem Hinzufügen von 6:", zahlen)

# Die Liste mit einer Schleife durchlaufen
print("\nAlle Zahlen in der Liste:")
for zahl in zahlen:
    print(zahl)
