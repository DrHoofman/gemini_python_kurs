fruechte = ["Apfel", "Birne", "Banane", "Kirsche", "Pfirsich"]

for frucht in fruechte:
    print(f"ich mag sehr gerne : {frucht}")

for zahl in range(6):
    print(f"Zahl: {zahl}")

for zahl in range(1, 6):
    print(f"Zahl: {zahl}")    

text = "\nPython\n"
for bubble in text:
    print(bubble)    

zahl = 1
while zahl <= 5:
    print(f"Aktuelle Zahl: {zahl}")
    zahl += 1

for zahl in range(10):
    if zahl == 5:
        print("Schleife bei 5 gestoppt.")
        break
    print(zahl)

for zahl in range(10):
    if zahl % 2 == 0:
        continue # Überspringt gerade Zahlen
    print(f"Ungerade Zahl: {zahl}")

for zahl in range(1,21):
    if zahl == 7:
        print("die Zahl ist", zahl)
    if zahl == 15:
        print("die Schleife wurde bei ", zahl, "gestoppt")  