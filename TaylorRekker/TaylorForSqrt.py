"""Skript som plottar Taylor-polynoma, opp til 
 ein bestemt orden, for funksjonen
 f(x) = sqrt(x) omkring x=1.
 Den maksimale ordenen til funksjonen er input."""

# Bibliotek
import numpy as np
import math
import matplotlib.pyplot as plt

# Maksimal orden
Nmax = 15

# Funksjonen
def funk(x):
    return np.sqrt(x)

# Vektor med x-verdiar
x = np.linspace(0, 3, 200)

# Initierer polynomet
P = 0*x

# Initerar tejlar og nemnar for koeffisentane
teljar = 1
nemnar = 1

# Startar plot
fig = plt.figure(1)

# Går gjennom alle N-verdiane til og med Nmax
for n in range(Nmax+1):
    # Neste ledd i Taylor-polynomet
    an = 1/math.factorial(n)
    P = P + teljar/nemnar*(x-1)**n

    plt.clf()   # Tømmer figuren

    plt.plot(x, funk(x), 'k-', linewidth=2)     # Plottar sjølve funksjonen

    # Plottar Taylor-polynomet
    plt.plot(x, P, 'r--', linewidth=2)          # Plottar tilnærminga
    
    plt.ylim(-0.1, 2)                              # Grenser for y-aksen
    plt.grid(True)                              # Set på rutenett
    plt.title(f'n = {n}')                       # Tittel på figuren

    # Ventar på tastetrykk
    plt.show(block=False)
    plt.pause(0.1)
    plt.waitforbuttonpress()
    
    # Oppdaterar teljar og nemnar
    teljar = -teljar*(2*n-1)
    nemnar = nemnar*2*(n+1)