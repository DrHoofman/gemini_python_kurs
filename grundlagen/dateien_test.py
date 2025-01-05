# Eine Datei erstellen und Text hineinschreiben
# with open("meine_datei.txt", "w") as datei:
#     datei.write("Hallo Stefan!\n")
#     datei.write("Dies ist eine Textdatei.\n")
# print("Die Datei wurde erstellt.")
# 
# # Text an bestehende Datei anhängen
# with open("meine_datei.txt", "a") as datei:
#      datei.write("Hier ist eine weitere neue geile Zeile!\n")
# print("Text wurde erfolgreich hinzugefügt.")
#      
with open("uebung_001.txt", "w") as datei:
    datei.write("Programmieren macht Spaß! Ich möchte gerne noch viel mehr programmieren.\n")
    datei.write("ich freue mich auf den nächsten Kursabschnitt.\n")
print("Die Datei wurde erstellt.")

with open("uebung_001.txt", "a") as datei:
    datei.write("Hier ist eine weitere neue geile Zeile!\n")

# Datei lesen und Inhalt ausgeben
with open("uebung_001.txt", "r") as datei:
    inhalt = datei.read()
    print("\nInhalt der Datei:")
    print(inhalt)

