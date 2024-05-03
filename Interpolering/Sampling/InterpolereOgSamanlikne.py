 """
 Dette skriptet plottar ein funksjon - saman med eit sett med punkt.
 Punkta tilsvarar jamfordelte x-verdiar.
 Meininga med skriptet er å vise at interpolerande polynom ikkje alltid er
 vegen å gå ...
 
 Alle inputs, inkludert funksjonen sjølv, er hardkoda i starten av skriptet
"""

# Importere numpy-biblioteket og matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Funksjonen vi skal fosøke å interpolere
def funk(x):
    return 1/(1+25*x**2)

# Det aktuelle intervallet
xMin = -1
xMax = 1

# Antal punkt i samplinga
N = 5

###### Slutt på inputs #############

# Punkt for å plotte funksjonen (200 punkt)
xDense = np.linspace(xMin, xMax, 200)
yDense = funk(xDense)

# Samplepunkta
x = np.linspace(xMin, xMax, N)
y = funk(x)

#
# Set opp Vandermonde-matrisa
#
LL = len(x)                 # Antal punkt
# Gjer vektorane til søyle-vektorar
y = np.transpose(y)         
x = np.transpose(x)
# Allokerar Vandermonde-matrisa (berre null-verdiar)
VanMat = np.zeros((LL, LL), dtype = float)
for n in range(0,LL):
    VanMat[:,n] = np.power(x,LL-n-1)    # Tilordnar søyle for sløye

# Bestemmer koeffisientane ved å invertere matrisa
InvVanMat = np.linalg.inv(VanMat)
# Finn koeffisientane ved å multiplisere den inverterte matrisa med y-vektoren
Coeff = np.matmul(InvVanMat, y)

# Allokerar vektor for y-verdiane til polynomet
yPoly = np.zeros(200)
# Reknar ut y-verdiane frå det interpolerande polynomet
for n in range(0,LL,1):
    yPoly = yPoly + Coeff[n]*xDense**(LL-n-1)
    
# Plottar punkta - saman med det linterpolerande polynomet
plt.plot(xDense, yDense, 'b-', label = 'Funksjon')      # Funksjonen
plt.plot(x, y, 'rx', label = 'Samplepunkt')             # Punkta
plt.plot(x, y, 'k--', label = 'Samplepunkt')             # Punkta
plt.plot(xDense, yPoly, 'g--', label = 'Polynom')       # Interpolerande polynom
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.ylim(-.5, 1.5)
