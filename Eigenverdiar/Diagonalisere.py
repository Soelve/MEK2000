"""
Dette skriptet finn eigenverdiane og (normaliserte) eigenvektorar
til ei matrise. Denne matrisa, input, er hardkoda i starten.
"""

# Hente numpy
import numpy as np

# Matrisa vi skal diagonalisere
Mat = [[1, 2], 
       [0, 2]]

####### Slutt på input ##################

# Finn eigenverdiar og eigenvektorar
eval, evec = np.linalg.eig(Mat)

# Skriv eigenverdiar og -vektorar til skjerm
print(eval)
print(evec)