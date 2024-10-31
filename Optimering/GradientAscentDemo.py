"""
Dette skriptet implementerar metoden gradient descent for å finne minimalpunkt
til ein funksjon. 
Startpunkt, (x_0, y_0), funksjonen vi skal minimere og såkalla learning rate,
gamma, er hardkoda i starten. I tillegg har vi fiksert parameteren h, som
blir brukt til å estimere dei partielle deriverte.

Skriptet lener seg tunkt på skriptet PlotBrattasteStiTilTopps.py
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm            # Fargekart

# Funksjon som vi vil plotte
def funk(x,y):
    return 1/((x-1)**2+(y-2)**2+1) + 1/((x-4)**2+(y-3)**2+2)

# Steglengda - Parameter brukt til å estimere partielle deriverte
# og til å lage stien mot toppen
h = 1e-3
gamma = 0.1                     # Learning rate

# Grenser for x og y (hardkoda)
xMin = -4
xMax = 6
yMin = -4
yMax = 6

# Startpunkt
x0 = 0
y0 = 0
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
zOld = z - 1e5

#
while z > zOld:
    # Kopierar z til zOld
    zOld = z
    # Skriv x, y og z til vektor (utvikdar vektorane)
    xVektor = xVektor + [x] 
    yVektor = yVektor + [y] 
    zVektor = zVektor + [z]    
    # Partielle deriverte
    dFdx = (funk(x+h, y) - funk(x-h, y))/(2*h)
    dFdy = (funk(x, y+h) - funk(x, y-h))/(2*h)
    # Steg i retning av gradienten
    x = x + gamma*dFdx
    y = y + gamma*dFdy
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
ax.plot(x0, y0, z0, 'kx')
# Plottar banen langs gradienten
ax.plot(xVektor, yVektor, zVektor, color = 'red')

# Tekst på aksane
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Vis plottet
plt.show()
