"""
Dette skriptet plottar gradientfeltet til ei flate i rommet.
Funksjonsuttrykket og grensene for x og y er hardkoda i 
starten av skriptet.
Vi brukar midtpunktsformelen for numerisk derivasjontil å 
estimere dei partielt deriverte.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt 

# Funksjon som vi vil plotte gradientfeltet til
def funk(x,y):
    return -1/((x-1)**2+(y-2)**2+1) - 1/((x-4)**2+(y-3)**2+2)

# Grenser for x og y (hardkoda)
xMin = -2
xMax = 6
yMin = 0
yMax = 6

# Steglengda brukt til å estimere gradienten (hardkoda)
h = 1e-2

# Vektor - og matriser - med funksjonsverdiar (200 pkt i kvar retning)
Npkt = int(50)
x = np.linspace(xMin, xMax, Npkt)
y = np.linspace(yMin, yMax, Npkt)
xx, yy = np.meshgrid(x, y)

# Matrise med z-verdiar
zz = funk(xx, yy)

# Loopar over alle punkt og finn patrielt deriverte
dFdx = np.zeros((Npkt, Npkt))
dFdy = np.zeros((Npkt, Npkt))
Xindex = 0
# NB: Rekkefoelga paa indeksane for x og y er bytt om i matrisene
for xValue in x:
    Yindex = 0
    for yValue in y:
      # Den x-deriverte
      dFdx[Yindex, Xindex] = (funk(xValue+h, yValue) - 
                              funk(xValue-h, yValue))/(2*h)    
      # Den y-deriverte
      dFdy[Yindex, Xindex] = (funk(xValue, yValue+h) - 
                              funk(xValue, yValue-h))/(2*h)    
    # Oppdaterar indeksar (merk indenteringa)
      Yindex = Yindex + 1
    Xindex = Xindex + 1  

# Ny 3d-figur til å plotte gradienten - samen med eit fargeplott av funsjonen
plt.figure(1)
plt.clf()
# Fargeplott av funksjonen
plt.pcolor(xx, yy, zz, alpha = 1, shading = 'auto')
# Vektorfeltet. NB: Merk at dei deriverte kjem i ei ikkje-intuitiv rekkefølge
#plt.quiver(x, y, dFdx, dFdy)
# Tekst på aksane
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# Ny figur til å lage nivåkurver
fig2 = plt.figure(2)
plt.clf()
ax2 = fig2.subplots(1, 1)
# Lagar nivåkurver
contours = ax2.contour(xx, yy, zz)
# Skriv den aktuelle z-verdien på kvar kurve
plt.clabel(contours)
ax2.quiver(x, y, dFdx, dFdy)
# Tekst på aksane
ax2.set_xlabel('x')
ax2.set_ylabel('y')
# Kvadratiske aksar
ax2.set_aspect('equal', adjustable='box')
ax2.set_title('Nivåkurver')

plt.show()