"""Dette skriptet finn, determinant, eigenverdiane og (normaliserte) 
eigenvektorar til ei kvadratisk matrise. Denne matrisa er hardkoda i starten.
"""

# Hente numpy
import numpy as np

# Matrisa vi skal diagonalisere
Mat = [[1, 2], 
       [0, 2]]


# Finn determinanten
determinant = np.linalg.det(Mat)

# Finn eigenverdiar og eigenvektorar
eval, evec = np.linalg.eig(Mat)

# Skriv determinanten til skjerm
print('Determinant:')
print(determinant)


# Skriv eigenverdiar og -vektorar til skjerm
print('Vektor med eigenverdiar:')
print(eval)
print('Matrise med tilsvarande normaliserte eigenvektorar som søyler:')
print(evec)
