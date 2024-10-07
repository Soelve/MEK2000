"""Dette skriptet plottar ein funksjon.
Sjølve funksjonen og intervallet vi vil plotte i er
hard-koda inn i starten. 
Vi har også hardkoda inn antal punkt vi brukar til plottinga
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Funksjon
def funk(x):
    return np.sin(x**2)

# Intervall
x_min = -2
x_max = 3

# Antal punkt
Npkt = 200

######## Slutt på inputs #############

# Vektor med x-verdiar
x_vektor = np.linspace(x_min, x_max, Npkt)
# Vektor med y-verdiar
y_vektor = funk(x_vektor)

# Lagar plott
plt.figure(1)           # Figur 1
plt.clf()               # Fjernar evt. gamalt plott
# Plottar funksjonen
plt.plot(x_vektor, y_vektor, color = 'black')   # Svart kurve
# Namn på aksane
plt.xlabel('x')
plt.ylabel('y')
# Rutenett
plt.grid()
plt.show()
