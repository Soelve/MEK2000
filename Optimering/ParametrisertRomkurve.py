"""Dette skriptet plottar ei kurve i rommet.
Koordinatane x, y og z er alle gitt ved parameteren t.

Funksjonsuttrykka og grensene for t er hardkoda i 
starten av skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 

# Funksjon som vi vil plotte
def funkX(t):
    return 2+t/2

def funkY(t):
    return np.sin(t)/2

def funkZ(t):
    return 1/2*np.cos(t**2/2)

# Grenser for t (hardkoda)
tMin = 0;
tMax = 3.5;

# Vektorar til plotting
Npkt = 200                  # Antal punkt
tVektor = np.linspace(tMin, tMax, Npkt)
xVektor = funkX(tVektor)
yVektor = funkY(tVektor)
zVektor = funkZ(tVektor)

# Plottinga
ax = plt.figure(1).add_subplot(projection='3d')
ax.plot(xVektor, yVektor, zVektor)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
