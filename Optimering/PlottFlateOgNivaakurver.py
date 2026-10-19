# -*- coding: utf-8 -*-
"""Dette skriptet plottar ei flate i rommet.
Den gjer det på tre måtar - direkte som eit flateplott, som fargekart
og som nivåkurver.

Funksjonsuttrykket og grensene for x og y er hardkoda i 
starten av skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 
#from matplotlib import cm            # Fargekart

# Funksjon som vi vil plotte
def funk(x,y):
     return -1/((x-1)**2+(y-2)**2+1) - 1/((x-4)**2+(y-3)**2+2)
       
# Grenser for x og y (hardkoda)
xMin = -4
xMax = 6
yMin = -4
yMax = 6

# Vektor - og matriser - med funksjonsverdiar (Npkt pkt i kvar retning)
Npkt = 200
x = np.linspace(xMin, xMax, Npkt)
y = np.linspace(yMin, yMax, Npkt)
xx, yy = np.meshgrid(x, y)

# Matrise med z-verdiar
zz = funk(xx, yy)

# Ny 3d-figur til å lage flateplott
fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111, projection='3d')
# Lagar flateplott i rommet
surf = ax.plot_surface(xx, yy, zz, cmap = 'magma')
# Tekst på aksane
ax.set_xlabel('x')
ax.set_ylabel('y')


# Ny figur til å lage fargekart
# Plott fargekart
plt.figure(2)
plt.clf()
plt.pcolormesh(xx, yy, zz, shading = 'auto', cmap = 'viridis')
plt.colorbar()

# Tekst på aksane
plt.xlabel('x')
plt.ylabel('y')

plt.show()

# Ny figur til å lage nivåkurver
fig2 = plt.figure(3)
plt.clf()
ax2 = fig2.subplots(1, 1)
# Lagar nivåkurver
contours = ax2.contour(xx, yy, zz)
# Skriv den aktuelle z-verdien på kvar kurve
plt.clabel(contours)
# Tekst på aksane
ax2.set_xlabel('x')
ax2.set_ylabel('y')
# Kvadratiske aksar
ax2.set_aspect('equal', adjustable='box')
ax2.set_title('Nivåkurver')

plt.show()
