def summe_gerade_ungerade(a, b):
    summe = a + b
    if summe % 2 == 0:
        return f"Die Summe von {a} und {b} ist {summe} und gerade."
    else:
        return f"Die Summe von {a} und {b} ist {summe} und ungerade."


# Beispielaufruf der Funktion
zahl1 = 7
zahl2 = 5
ergebnis = summe_gerade_ungerade(zahl1, zahl2)

# Ergebnis ausgeben
print(ergebnis)
