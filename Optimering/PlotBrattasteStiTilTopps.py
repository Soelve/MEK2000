"""
Dette skriptet plottar ei flate i rommet og den brattaste vegen til den
"næraste" toppen.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm            # Fargekart

# Funksjon som vi vil plotte
def funk(x,y):
    return np.exp(-(2*x**2+x*yy**2))

# Steglengda - Parameter brukt til å estimere partielle deriverte
# og til å lage stien mot toppen
h = 1e-3
offset = .02

# Grenser for x og y (hardkoda)
xMin = -2
xMax = 2
yMin = -2
yMax = 2

# Startpunkt
x0 = -1
y0 = 2
z0 = funk(x0, y0)

# Vektor - og matriser - med funksjonsverdiar (200 pkt i kvar retning)
x = np.linspace(xMin, xMax, 200)
y = np.linspace(yMin, yMax, 200)
xx, yy = np.meshgrid(x, y)

# Matrise med z-verdiar
zz = funk(xx, yy)

# Initerar posisjon - og vektor med posisjonsdata
x = x0
y = y0
z = z0
xVektor = []
yVektor = []
zVektor = []
# Set laag verdi for zOld - for at loekka skal komme i gang
zOld = -1e5

#
while z > zOld:
    # Kopierar z til zOld
    zOld = z
    # Skriv x, y og z til vektor (utvikdar vektorane)
    xVektor = xVektor + [x] 
    yVektor = yVektor + [y] 
    zVektor = zVektor + [z + offset]    # z faar eit lite tillegg
    # Partielle deriverte
    dFdx = (funk(x+h, y) - funk(x-h, y))/(2*h)
    dFdy = (funk(x, y+h) - funk(x, y-h))/(2*h)
    # Normen til gradienten
    Norm = np.sqrt(dFdx**2 + dFdy**2)
    # Steg i retning av gradienten
    x = x + h*dFdx/Norm
    y = y + h*dFdy/Norm
    z = funk(x,y)
    
# Ny 3d-figur til å lage flateplott
fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111, projection='3d')
# Lagar flateplott i rommet
# cmap: Fargekart (gitt med pakken cm fraa MatPlotLib)
# alpha: Kor gjennomsiktig det skal vere 
surf = ax.plot_surface(xx, yy, zz, cmap = cm.cividis, 
                       alpha = .5)
# Plottar startpunkt
ax.plot(x0, y0, z0+offset, 'kx')
# Plottar banen langs gradienten
ax.plot(xVektor, yVektor, zVektor, color = 'red')

# Tekst på aksane
ax.set_xlabel('x')
ax.set_ylabel('y')

# Vis plottet
plt.show()
