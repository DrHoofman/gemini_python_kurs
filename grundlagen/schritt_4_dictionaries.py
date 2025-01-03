# Ein Wörterbuch erstellen
person = {
    "name": "Stefan",
    "alter": 66,
    "groesse": 1.87,
    "ist_programmierer": True,
    "Wohnort": "Altendorf",
    "Postleitzahl": 96127,
    "Straße": "Pointstrasse",
    "Hausnummer": 2,
}

# Das gesamte Wörterbuch ausgeben
print("\nPersonendaten:", person)

# Zugriff auf einzelne Werte
print("Name der Person:", person["name"])
print("Alter der Person:", person["alter"])
print("Wohnort der Person:", person["Wohnort"])

# Schleife durch das Wörterbuch
print("\nAlle Daten der Person:")
for schluessel, wert in person.items():
    print(f"{schluessel}: {wert}")