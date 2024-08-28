"""
 Dette skriptet konstruerar ein kvadratisk spline for eit sett med fire punkt.
 Dette settet er hardkoda i starten av skriptet.
 Koeffisientane i polynoma blir bestemt ved å sette opp eit lineært liknings-
 system for problemet. Dette systemet blir løyst ved at koeffisientmatrisa 
 sett opp og invertert.
"""
# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Vektorar med punkta som skal inperpolerast
x = [1, 2, 3, 5]
y = [-4, -3, 0, -2]

###### Slutt på inputs #############

#
# Set opp Koeffisient-matrisa
#
Mat = [[x[0]**2, x[0], 1, 0, 0, 0, 0, 0, 0],    # Første seks: Interpolere punkta
       [x[1]**2, x[1], 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, x[1]**2, x[1], 1, 0, 0, 0],
       [0, 0, 0, x[2]**2, x[2], 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, x[2]**2, x[2], 1],    # Neste to: glatt overgang
       [0, 0, 0, 0, 0, 0, x[3]**2, x[3], 1],
       [2*x[1], 1, 0, -2*x[1], -1, 0, 0, 0, 0],
       [0, 0, 0, 2*x[2], 1, 0, -2*x[2], -1, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0]]             # Siste: p_1''(x) = 0
# Høgresidene i likningane (blir gjort om til søylevektor)
HoegreSide = np.array([y[0], y[1], y[1], y[2], y[2], y[3], 0, 0, 0])
HoegreSide= np.transpose(HoegreSide)

# Gjer vektorane til søyle-vektorar
# Bestemmer koeffisientane ved å invertere matrisa
MatInv = np.linalg.inv(Mat)
# Finn koeffisientane ved å multiplisere den inverterte matrisa med y-vektoren
Coeff = np.matmul(MatInv, HoegreSide)

#
# Plottar splinen - saman med punkta som skal interpolerast
#
plt.plot(x, y,'kx', label = 'Punkt')            # Punkta

# Loopar over dei tre andregradsfunksjonane
for n in range(0,3):   
    # Lagar vektor for å plotte polynomet (50 punkt)
    xx = np.linspace(x[n],x[n+1], 50)    
    # Vektor med y-verdiane
    a = Coeff[0+3*n]
    b = Coeff[1+3*n]
    c = Coeff[2+3*n]
    yy = a*xx**2 + b*xx + c
    plt.plot(xx, yy, label = 'p_{}'.format(n))

# Tekst på aksane, forklaringsboks og rutenett
plt.xlabel('x')
plt.ylabel('y')
plt.grid(visible = True)
plt.legend()
plt.show()
