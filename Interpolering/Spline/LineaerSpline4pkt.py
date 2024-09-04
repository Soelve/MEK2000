"""Dette skriptet konstruerar ein lineær spline for eit sett med fire punkt.
Dette settet er hardkoda i starten av skriptet.
Koeffisientane i polynoma blir bestemt ved å sette opp eit lineært liknings-
system for problemet. Dette systemet blir løyst ve dat koeffisientmatrisa 
sett opp og invertert.
"""
# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Vektorar med punkta som skal inperpolerast
x = [11, 11.5, 12, 12.5]
y = [27.3, 28.1, 29.0, 28.7]

###### Slutt på inputs #############

#
# Set opp Koeffisient-matrisa
#
Mat = [[x[0], 1, 0, 0, 0, 0],
       [x[1], 1, 0, 0, 0, 0],
       [0, 0, x[1], 1, 0, 0],
       [0, 0, x[2], 1, 0, 0],
       [0, 0, 0, 0, x[2], 1],
       [0, 0, 0, 0, x[3], 1]]
# Høgresidene i likningane (blir gjort om til søylevektor)
HoegreSide = np.array([y[0], y[1], y[1], y[2], y[2], y[3]])
HoegreSide= np.transpose(HoegreSide)

# Gjer vektorane til søyle-vektorar
# Bestemmer koeffisientane ved å invertere matrisa
MatInv = np.linalg.inv(Mat)
# Finn koeffisientane ved å multiplisere den inverterte matrisa med y-vektoren
Coeff = np.matmul(MatInv, HoegreSide)

# Skriv splinen til skjerm
print(f'p_0 = {Coeff[0]:.2f}x + {Coeff[1]:.2f}')
print(f'p_1 = {Coeff[2]:.2f}x + {Coeff[3]:.2f}')
print(f'p_2 = {Coeff[4]:.2f}x + {Coeff[5]:.2f}')


#
# Plottar splinen - saman med punkta som skal interpolerast
#
plt.plot(x, y,'kx', label = 'Punkt')            # Punkta

# Loopar over dei tre førstegradsfunksjonane
for n in range(0,3):   
    # Lagar vektor for å plotte polynomet (50 punkt)
    xx = np.linspace(x[n],x[n+1], 50)    
    # Vektor med y-verdiane
    a = Coeff[0+2*n]
    b = Coeff[1+2*n]
    yy = a*xx + b
    plt.plot(xx, yy, label = 'p_{}'.format(n))

# Tekst på aksane, rutenett og tekstboks med forklaring
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(visible = True)
plt.show()
