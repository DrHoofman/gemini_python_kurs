namen = ["Stefan", "Lisa", "Lucca", "Lea", "Trang", "Nga", "Quang"]
for name in namen:
    print(f"hallo, {name}!")
print("\n")

zahlen = [3, 7, 12, 15]

for i in range(len(zahlen)):
    print(f"index {i}: Wert = {zahlen[i]}")
print("\n")

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

#Schleifen mit dictionaries
#Beispiel: Ein Wörterbuch ausgeben
person = {
    "Name": "Stefan",
    "Alter": 65,
    "Wohnort": "Altendorf"
}

for schluessel, wert in person.items():
    print(f"{schluessel}: {wert}")  # Ausgabe: Name: Stefan, Alter: 65, Wohnort: Altendorf

# Nur die Schlüssel ausgeben
for schluessel in person:
    print(f"Schlüssel: {schluessel}")

# Nur die Werte ausgeben
for wert in person.values():
    print(f"Wert: {wert}")

#  Übung 
# 1.	Erstelle eine Liste mit fünf Zahlen.
#	2.	Berechne die Summe aller Zahlen mit einer for-Schleife.
#	3.	Gib die Summe aus.
zahlen = [7, 8, 9, 23, 45]
summe = 0

for zahl in zahlen:
    summe += zahl

print(f"Summe der Zahlen: {summe}")