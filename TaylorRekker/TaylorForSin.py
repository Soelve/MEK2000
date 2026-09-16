"""Skript som plottar Taylor-polynoma, opp til 
 ein bestemt orden, for funksjonen
 f(x) = sin x omkring x=0.
 Den maksimale ordenen til funksjonen er input."""

# Bibliotek
import numpy as np
import math
import matplotlib.pyplot as plt

# Maksimalt antal ledd
Mmax = 4

# Funksjonen
def funk(x):
    return np.sin(x)

# Vektor med x-verdiar
x = np.linspace(-3*np.pi, 3*np.pi, 200)

# Initierer polynomet
P = 0*x

# Startar plot
fig = plt.figure(1)

# Går gjennom alle N-verdiane til og med Nmax
for m in range(Mmax+1):
    # Tilordnar graden
    n = 2*m+1
    # Neste ledd i Taylor-polynomet
    an = (-1)**m/math.factorial(n)
    P = P + an*x**n

    plt.clf()   # Tømmer figuren

    plt.plot(x, funk(x), 'k-', linewidth=2)     # Plottar sjølve funksjonen

    # Plottar Taylor-polynomet
    plt.plot(x, P, 'r--', linewidth=2)          # Plottar tilnærminga
    
    plt.ylim(-2,2)                              # Grenser for y-aksen
    plt.grid(True)                              # Set på rutenett
    plt.title(f'n = {n}')                       # Tittel på figuren

    # Ventar på tastetrykk
    plt.show(block=False)
    plt.pause(0.1)
    plt.waitforbuttonpress()