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
xMin = -2.0
xMax = 2.0

# Antal punkt i samplinga
N = 15

###### Slutt på inputs #############

# Punkt for å plotte funksjonen (200 punkt)
xDense = np.linspace(xMin, xMax, 200)
yDense = funk(xDense)

# Samplepunkta
x = np.linspace(xMin, xMax, N)
y = funk(x)

# Plottar
plt.plot(xDense, yDense, 'b-')
plt.plot(x, y, 'rx')
plt.plot(x, y, 'y--')
plt.xlabel('x')
plt.ylabel('y')
