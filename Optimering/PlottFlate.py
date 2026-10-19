"""Dette skriptet plottar ei flate i rommet.
Funksjonsuttrykket og grensene for x og y er hardkoda i 
starten av skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm            # Fargekart

# Funksjon som vi vil plotte
def funk(x,y):
    return 1/(x**2-x*y+2*y**2+x+y+1)

# Grenser for x og y (hardkoda)
xMin = -1
xMax = -.5
yMin = -.5
yMax = 0

# Vektor - og matriser - med funksjonsverdiar (200 pkt i kvar retning)
x = np.linspace(xMin, xMax, 400)
y = np.linspace(yMin, yMax, 400)
xx, yy = np.meshgrid(x, y)

# Matrise med z-verdiar
zz = funk(xx, yy)

# Ny 3d-figur til å lage flateplott
fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111, projection='3d')
# Lagar flateplott i rommet
surf = ax.plot_surface(xx, yy, zz, cmap = cm.magma, 
                       alpha = 0.7)
# Tekst på aksane
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
