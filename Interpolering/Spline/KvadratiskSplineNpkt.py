"""Dette skriptet konstruerar ein kvadratisk spline for eit sett med punkt.
Dette settet er hardkoda som input i starten av skriptet.
Koeffisientane i polynoma blir bestemt ved rekursjonsformlar som gjer oss
i stand til å finne koeffisientane for neste polynom i splinen ved hjelp
av koeffisientane til det førre.
"""
# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Vektorar med punkta som skal inperpolerast
x = [1, 2, 4, 5, 8, 10]
y = [2, 5, 3, 3, 7, 6]

###### Slutt på inputs #############

# Bestemmer antal punkt
n = len(x)

# Allokerar
a_vektor = np.zeros(n-1)
b_vektor = np.zeros(n-1)
c_vektor = np.zeros(n-1)

# Koeffisientane for p_0
a_vektor[0] = 0
b_vektor[0] = (y[1]-y[0])/(x[1]-x[0])
c_vektor[0] = y[0]

# For alle andre polynom
for k in range(1,n-1):
    c_vektor[k] = y[k]
    b_vektor[k] = b_vektor[k-1] + 2*a_vektor[k-1]*(x[k]-x[k-1])
    a_vektor[k] = (y[k+1]-y[k]-b_vektor[k]*(x[k+1]-x[k]))/(x[k+1]-x[k])**2
    

# Skriv splinen til skjerm
for k in range(n-1):
    print(f'p_{k}(x)={a_vektor[k]:.2f} (x-{x[k]})**2 + {b_vektor[k]:.2f} (x-{x[k]}) + {c_vektor[k]:.2f}')

#
# Plottar splinen - saman med punkta som skal interpolerast
#
plt.figure(1)
plt.clf()
plt.plot(x, y,'kx', label = 'Punkt')            # Punkta
# Loopar over andregradsfunksjonane
for k in range(n-1):   
    # Lagar vektor for å plotte polynomet (50 punkt)
    xx = np.linspace(x[k],x[k+1], 50)    
    # Vektor med y-verdiane
    yy = a_vektor[k]*(xx-x[k])**2 + b_vektor[k]*(xx-x[k]) + c_vektor[k]
    plt.plot(xx, yy, label = 'p_{}'.format(k))


# Tekst på aksane, forklaringsboks og rutenett
plt.xlabel('x')
plt.ylabel('y')
plt.grid(visible = True)
plt.legend()
plt.show()