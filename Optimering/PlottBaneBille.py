"""Dette skriptet plottar ei kurve i planet.
Koordinatane x og y er gitt ved parameteren t.

Funksjonsuttrykka og grensene for t er hardkoda i 
starten av skriptet.

I tillegg plottar skriptet farten som funksjon av tid, der 
tida er parameteren.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 

# Grenser for t (hardkoda)
tMin = 0;
tMax = 3;

# Funksjonsuttrykk
def x(t):
    return 1 + t - 0.5*t**2

def y(t):
    return 2 - 0.5*np.cos(t)

# Vektorar til plotting
Npkt = 500                  # Antal punkt
tVektor = np.linspace(tMin, tMax, Npkt)

# Plottinga
plt.figure(1)
plt.clf()
# Sjoelve plottet
plt.plot(x(tVektor), y(tVektor))
# Tekst paa aksane
plt.xlabel('x')
plt.ylabel('y')
# Rutenett
plt.grid()
# Vis plott
plt.show()