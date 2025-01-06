namen = ["Stefan", "Lisa", "Lucca", "Lea", "Trang", "Nga", "Quang"]
for name in namen:
    print(f"hallo, {name}!")

zahlen = [3, 7, 12, 15]

for i in range(len(zahlen)):
    print(f"index {i}: Wert = {zahlen[i]}")

# Aufgabe 1: Schreibe eine Schleife, die die Summe der Zahlen in der Liste zahlen berechnet und ausgibt
zahlen = [3, 7, 12, 15]
summe = 0
for zahl in zahlen:
    summe += zahl
    print(f"summe der Zahlen: {summe}")

# enumerate()  für Listen (Index und Wert kombinieren)
farben = ["rot", "grün", "blau", "gelb"]
for index, farbe in enumerate(farben):
    print(f"Farbe an Position {index}: {farbe}")
