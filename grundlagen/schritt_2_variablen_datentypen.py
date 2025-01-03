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
print("\nHier sind die Daten, die du eingegeben hast:")
print("Name:", name)
print("Alter:", alter)
print("Größe:", groesse, "Meter")
print("Bist du Programmierer?", ist_programmierer)  

jahre_bis_rente = 67 - alter # Berechnung der Jahre bis zur Rente, wenn das Renteneintrittsalter 67 ist
groesse_in_cm = groesse * 100 # Umrechnung der Größe in Zentimeter

#Formatierte Ausgabe
print("\nZusätzliche Informationen:")
print(f"Deine Größe in Zentimetern: {groesse_in_cm:.1f} cm") # f-string für die Formatierung

if alter >= 67:
    print("Du bist bereits im Rentenalter.")
elif jahre_bis_rente > 0:
    print(f"Du hast noch {jahre_bis_rente} Jahre bis zur Rente.")
else:
    print("Rente ist für dich noch nicht relevant.")

# Bedingung: Programmierer-Status
if ist_programmierer:
    print("Das ist großartig! Viel Spaß beim Programmieren!")
else:
    print("Vielleicht möchtest du Programmieren lernen!")

print("\nZahlen von 1 bis 5:")
for zahl in range(1,6):
    print(zahl)

geheimzahl = 7  # Geheime Zahl
benutzerzahl = 0  # Benutzereingabe

while benutzerzahl != geheimzahl:
    benutzerzahl = int(input("\nRate die geheime Zahl (1-10): "))
    if benutzerzahl < geheimzahl:
        print("Zu niedrig! Versuche es erneut.")
    elif benutzerzahl > geheimzahl:
        print("Zu hoch! Versuche es erneut.")
    else:
        print("Glückwunsch! Du hast die geheime Zahl erraten!")

def begruessung():
    print("\nHerzlich willkommen zum Gemini Python Kurs!")
    print("Wir wünschen dir viel Spaß beim Programmieren.")

begruessung()  # Aufruf der Funktion



