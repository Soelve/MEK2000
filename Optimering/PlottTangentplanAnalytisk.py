"""
Dette skriptet plottar ei flate i rommet.
I tillegg plottar den, for eit gitt punkt, tangentlinjer
langs x og y-aksen og tangentplanet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm               # Fargekart

# Funksjon som vi vil plotte
def funk(x,y):
    return x*np.exp(-x**2-y**2/2)


# Punktet vi tar utgangspunkt i
x0 = 1
y0 = 2

# Tangentplanet
def Tang(x,y):
    return np.exp(-3)*(1-(x-1)-2*(y-2))

# Grenser for x og y (hardkoda)
xMin = -3
xMax = 3
yMin = -3
yMax = 3

# Vektor - og matriser - med funksjonsverdiar (200 pkt i kvar retning)
x = np.linspace(xMin, xMax, 200)
y = np.linspace(yMin, yMax, 200)
xx, yy = np.meshgrid(x, y)

# Matrise med z-verdiar
zz = funk(xx, yy)

# Ny 3d-figur til å lage flateplott
fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111, projection='3d')
# Lagar flateplott i rommet
surf = ax.plot_surface(xx, yy, zz, cmap = cm.magma, 
                       alpha = 0.75)
# Tekst på aksane
ax.set_xlabel('x')
ax.set_ylabel('y')

# Matrise med z-verdiar
ZZplane = Tang(xx, yy)
surf2 = ax.plot_surface(xx, yy, ZZplane, color = 'green', 
                       alpha = 0.5)

plt.show()