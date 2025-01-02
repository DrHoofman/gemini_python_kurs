# name = "Stefan "           # String: Text
# alter = 65                 # Integer: Ganzzahl  
# groesse = 1.87             # Float: Kommazahl
# ist_programmierer = True   # Boolean: Wahrheitswert (True/False)
# zahl_der_Datentypen = 4    # Integer: Ganzzahl
# Ausgabe der Variablen
# print("Name:", name)
# print("Alter:", alter)
# print("Größe:", groesse, "Meter")
# print("Ist Programmierer?", ist_programmierer)

# Überprüfen der Datentypen
# print("Der Datentyp von 'name' ist:", type(name))
# print("Der Datentyp von 'alter' ist:", type(alter))
# print("Der Datentyp von 'groesse' ist:", type(groesse))
# rint("Der Datentyp von 'ist_programmierer' ist:", type(ist_programmierer)) 
# print("das sind insgesamt "(zahl_der_Datentypen))# 

name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? ")) # Umwandlung in Integer
groesse = float(input("Wie groß bist du(in Metern)? ")) # Umwandlung in Float
ist_programmierer = input("Bist du Programmierer? (ja/nein) : ").lower() == "ja" # Umwandlung in Boolean
print("Hier sind die Daten, die du eingegeben hast:")
print("Name:", name)
print("Alter:", alter)
print("Größe:", groesse, "Meter")
print("Ist Programmierer?", ist_programmierer)  