"""
Dette skriptet estimerar eit (bestemt) integral ved hjelp av trapes-metoden.
Som input tar det integranden (funksjonen vi skal integrere), 
integrasjonsgrensene a og b og N - antal delintervall vi vil bruke i 
estimatet.
Desse er hard-koda i starten av skriptet.
"""

# importerar NumPy-biblioteket
import numpy as np

# Integranden
def funk(x):
    return np.cos(x**2)

# Integrasjonsgrenser
a = 0
b = 1

# Oppdelinga
N = 10

################################

# Bestemmer delta x
dx = (b-a)/N

# Første og siste punkt
T = dx/2*(funk(a) + funk(b))

# Resten av punkta
x = a                               # Startverdi for x
for n in range(1,N):
    x = x + dx                      # Oppdaterar x
    T = T + dx*funk(x)              # Oppdaterar summen T
    
# Skriv resultat til skjerm

print('T=', T)    
