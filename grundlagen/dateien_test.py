# Eine Datei erstellen und Text hineinschreiben
with open("meine_datei.txt", "w") as datei:
    datei.write("Hallo Stefan!\n")
    datei.write("Dies ist eine Textdatei.\n")
print("Die Datei wurde erstellt.")

# Text an bestehende Datei anhängen
with open("meine_datei.txt", "a") as datei:
     datei.write("Hier ist eine weitere neue geile Zeile!\n")
print("Text wurde erfolgreich hinzugefügt.")
     