"""
 Dette skriptet plottar ein funksjon - saman med eit sett med punkt.
 Punkta tilsvarar jamfordelte x-verdiar.
 Meininga med skriptet er å undersøke kor tett desse x-verdiane må
 ligge for at punkta på ein meiningsfull måte skal kunne sample/interpoere
 den aktuelle funksjonen. 
 Alle inputs, inkludert funksjonen sjølv, er hardkoda i starten av skriptet
"""

# Importere numpy-biblioteket
import numpy as np
import matplotlib.pyplot as plt

# Funksjonen vi skal fosøke å interpolere
def funk(x):
    return np.sin(np.pi*x)

# Det aktuelle intervallet
x_min = -2.0
x_max = 2.0

# Antal punkt i samplinga
N = 15

###### Slutt på inputs #############

# Punkt for å plotte funksjonen (200 punkt)
x_dense = np.linspace(x_min, x_max, 200)
y_dense = funk(x_dense)

# Samplepunkta
x = np.linspace(x_min, x_max, N)
y = funk(x)

# Plottar
plt.figure(1)
plt.clf()
plt.plot(x_dense, y_dense, 'b-')
plt.plot(x, y, 'rx')
plt.plot(x, y, 'y--')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
