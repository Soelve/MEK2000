"""
Dette skriptet plottar tre punkt saman med tre ulike måtar å interpolere dei
på:
    1) Interpolerande polynom
    2) Lineær spline
    3) Kvadratisk spline
Punkta som skal interpolerast er hard-koda i starten av skriptet
"""
# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Vektorar med punkta som skal inperpolerast
x = [1, 2, 3]
y = [-4, -3, 0]

###### Slutt på inputs #############

# Gjer vektorane til søyle-vektorar
y = np.transpose(y)         
x = np.transpose(x)

########## Interpolerande polynom ######################
#
# Set opp Vandermonde-matrisa
LL = len(x)                 # Antal punkt
# Allokerar Vandermonde-matrisa (berre null-verdiar)
VanMat = np.zeros((LL, LL), dtype = float)
for n in range(0,LL):
    VanMat[:,n] = np.power(x,LL-n-1)    # Tilordnar søyle for sløye

# Bestemmer koeffisientane ved å invertere matrisa
InvVanMat = np.linalg.inv(VanMat)
# Finn koeffisientane ved å multiplisere den inverterte matrisa med y-vektoren
CoeffPoly = np.matmul(InvVanMat, y)

# Lagar vektor for å plotte polynomet (100 punkt)
xPoly = np.linspace(x[0]-0.2,x[-1]+0.2,100)    # x[-1] er siste pkt. i x-vektor
# Allokerar vektor for y-verdiane
yPoly = np.zeros(100)

# Reknar ut y-verdiane frå det interpolerande polynomet
for n in range(0,LL):
    yPoly = yPoly + CoeffPoly[n]*xPoly**(LL-n-1)

########## Kvadratisk spline ######################
#
# Set opp Koeffisient-matrisa
Mat = [[x[0]**2, x[0], 1, 0, 0, 0],    
       [x[1]**2, x[1], 1, 0, 0, 0],
       [0, 0, 0, x[1]**2, x[1], 1],
       [0, 0, 0, x[2]**2, x[2], 1],
       [2*x[1], 1, 0, -2*x[1], -1, 0],
       [1, 0, 0, 0, 0, 0]]            
# Høgresidene i likningane (blir gjort om til søylevektor)
HoegreSide = np.array([y[0], y[1], y[1], y[2], 0, 0])
HoegreSide= np.transpose(HoegreSide)

# Bestemmer koeffisientane ved å invertere matrisa
MatInv = np.linalg.inv(Mat)
# Finn koeffisientane ved å multiplisere den inverterte matrisa med y-vektoren
CoeffSpline = np.matmul(MatInv, HoegreSide)


########## Plottar punkta og interpoleringa ######################

plt.plot(x, y, 'kx', label = 'Punkt')
plt.plot(xPoly, yPoly,'b-.', label = 'Polynom')       # Interpolerande polynom
plt.plot(x, y, 'r-', label = 'Lineær spline')

# Loopar over dei tre andregradsfunksjonane
for n in range(0,2):   
    # Lagar vektor for å plotte polynomet (50 punkt)
    xx = np.linspace(x[n],x[n+1], 50)    
    # Allokerar vektor for y-verdiane
    a = CoeffSpline[0+3*n]
    b = CoeffSpline[1+3*n]
    c = CoeffSpline[2+3*n]
    yy = a*xx**2 + b*xx + c
    plt.plot(xx, yy, '--', label = 'p_{}, kvadratisk spline'.format(n))
    
# Tekst på aksane - og rutenett
plt.xlabel('x')
plt.ylabel('y')
plt.legend(visible = True)
plt.show()
