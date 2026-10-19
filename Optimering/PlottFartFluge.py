"""Dette skriptet plottar ei kurve i rommet.
Koordinatane x, y og z er alle gitt ved parameteren t.

Funksjonsuttrykka og grensene for t er hardkoda i 
starten av skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 

# Grenser for t (hardkoda)
tMin = 0;
tMax = 3.5;

# Vektorar til plotting
Npkt = 500                  # Antal punkt
tVektor = np.linspace(tMin, tMax, Npkt)
vVektor = 1/2*np.sqrt(1 + np.cos(tVektor)**2 + 
          tVektor**2*np.sin(tVektor**2/2)**2)
# Plottinga
plt.figure(2)
plt.clf()
# Sjoelve plottet
plt.plot(tVektor, vVektor)
# Tekst paa aksane
plt.xlabel('Tid [s]')
plt.ylabel('Fart [m/s]')
# Rutenett
plt.grid()
# Vis plott
plt.show()
