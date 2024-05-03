"""
Dette skriptet plottar ei flate i rommet og 
ein sti på denne flat. Stien er gitt ved ei 
parametrisert kurve i xy-planet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm            # Fargekart

# Funksjon som vi vil plotte
def funk(x,y):
    return np.greater_equal(4 - x**2- y**2, 0)*\
        (4 - x**2 - y**2)

# Grenser for x, y og t (hardkoda)
xMin = -2
xMax = 2
yMin = -2
yMax = 2
tMin = 0
tMax = 2

# Vektor - og matriser - med funksjonsverdiar (200 pkt i kvar retning)
Npkt = 200
x = np.linspace(xMin, xMax, Npkt)
y = np.linspace(yMin, yMax, Npkt)
xx, yy = np.meshgrid(x, y)

# Matrise med z-verdiar
zz = funk(xx, yy)

# Vektorar for tid og posisjon
tVektor = np.linspace(tMin, tMax, Npkt)
xVektor = (2-tVektor)*np.cos(np.pi*tVektor)
yVektor = (2-tVektor)*np.sin(np.pi*tVektor)
zVektor = funk(xVektor, yVektor)

# Ny 3d-figur til å lage flateplott
offset = 0.1                        # Hevar sjølve stien litt
fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111, projection='3d')
# Lagar flateplott i rommet
# cmap: Fargekart (gitt med pakken cm fraa MatPlotLib)
# alpha: Kor gjennomsiktig det skal vere 
surf = ax.plot_surface(xx, yy, zz, cmap = cm.cividis, alpha = 0.35)
# Plottar banen langs gradienten
ax.plot(xVektor, yVektor, zVektor+offset, color = 'red')

# Tekst på aksane
ax.set_xlabel('x')
ax.set_ylabel('y')
# Justere z-aksen
ax.set_zlim(0, 4)

# Vis plottet
plt.show()