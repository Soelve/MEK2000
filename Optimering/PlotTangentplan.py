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
    return 1/(x**2-x*y+0.5*y**2-x+1)

# Punktet vi tar utgangspunkt i
x0 = 0
y0 = 1

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

# Partielle deriverte (numerisk)
h = 1e-3
z0 = funk(x0, y0)
# Midtpunkts-formel
dFdx = (funk(x0+h, y0)- funk(x0-h, y0))/(2*h)
dFdy = (funk(x0, y0+h)- funk(x0, y0-h))/(2*h)
ax.plot(x0, y0, z0, 'rx')
# Tangent parallell med x-aksen
Xline = [z0 + dFdx*(xMin-x0), z0 + dFdx*(xMax-x0)]
ax.plot([xMin, xMax], [y0, y0], 
        Xline, 'b-')
# Tangent parallell med y-aksen
Yline = [z0 + dFdy*(yMin-y0), z0 + dFdy*(yMax-y0)]
ax.plot([x0, x0], [yMin, yMax], 
        Yline, 'b-')

# Tangentplan
# Funksjon
def Ztangent(x, y):
    return z0 + dFdx*(x-x0) + dFdy*(y-y0)
# Matrise med z-verdiar
ZZplane = Ztangent(xx, yy)
surf2 = ax.plot_surface(xx, yy, ZZplane, color = 'green', 
                       alpha = 0.5)

plt.show()
