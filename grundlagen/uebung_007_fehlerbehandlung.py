# Start
print("Programmstart")
# Funktion zur Addition von zwei Zahlen und Eingabeaufforderung für den Benutzer
def benutzer_addition():
    try :
        zahl1 = int(input("Bitte gib die erste Zahl ein:"))
        zahl2 = int(input("Bitte gib die zweite Zahl ein:"))
        summe = zahl1 + zahl2
        print(f"Die Summe von {zahl1} und {zahl2} ist {summe}")
    except ValueError:
        print("Du hast keine Zahl eingegeben.")

benutzer_addition()
