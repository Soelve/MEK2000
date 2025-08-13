"""
Dette skriptet estimerar den deriverte av ein gitt funksjon ved hjelp
av midpunktsformelen for numerisk derivasjon. Den samanliknar estimatet
med den eksakte verdien. I tillegg til sjølve funksjonen, den deriverte og 
den aktuelle x-verdien, er h input. Denne parameteren skal vere liten.
"""

# Bibliotek
import numpy as np

# Funksjon
def funk(x):
    return np.exp(-x**2)

# Den deriverte
def funkDeriv(x):
    return -2*x*np.exp(-x**2)

# Argumentverdi
x = 1

# Steglengda vi brukar
h=0.1

# Bestemmer deriverte (numerisk og eksakt)
Estimat = (funk(x+h)-funk(x-h))/(2*h)
Eksakt = funkDeriv(x)

# Skriv resultat til skjerm
print('Estimat for den deriverte:', Estimat)
print('Feil:', np.abs(Estimat-Eksakt))
