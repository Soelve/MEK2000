"""
 Dette skripte konstruerar eit interpolerande polynom for eit sett med punkt.
 Dette settet er hardkoda i starten av skriptet.
 Koeffisientane i polynomet blir bestemt ved å sette opp Vandermonde-
 matrisa, invertere denne og gange ho med søyelvektoren beståande av dei
 aktuelle y-verdiane.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Vektorar med punkta som skal inperpolerast
x = [0, 1, 3]
y = [1, 3, 4]

###### Slutt på inputs #############

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

# Lagar vektor for å plotte polynomet (100 punkt)
xx = np.linspace(x[0]-0.2,x[-1]+0.2,100)    # x[-1] is the last point in x
# Allokerar vektor for y-verdiane
yy = np.zeros(100)

# Reknar ut y-verdiane frå det interpolerande polynomet
for n in range(0,LL,1):
    yy = yy + Coeff[n]*xx**(LL-n-1)
    
# Plottar punkta - saman med det linterpolerande polynomet
plt.figure(5)
plt.clf()
# Punkta
plt.plot(x, y,'rx', label = 'Punkt', markeredgewidth = 2, markersize= 10)
# Interpolerande polynom
plt.plot(xx, yy,'b-.', label = 'Polynom', linewidth = 2)       
# Regresjonslinje
a = 10/7
b = 13/14
plt.plot(xx, a + b*xx, 'g--', label = 'Regresjonslinje', linewidth = 2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.show()