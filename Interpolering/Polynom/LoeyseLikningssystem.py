"""
 Dette skriptet løyser eit lineært likningssystem.
 Koeffisientmatrisa og tala på høgresidene i likningane er 
 hardkoda i starten.
 Skriptet løyser likningssystemet ved å invertere koeffisient-
 matrisa og gange denne med vektoren med verdiane på høgresida
"""
# Importenre numpy
import numpy as np

# Tilordne koeffisientmatrisa
A = [[1, 1, 1, 0, 0, 0],
     [4, 2, 1, 0, 0, 0],
     [0, 0, 0, 4, 2, 1],
     [0, 0, 0, 9, 3, 1],
     [4, 1, 0, -4, -1, 0],
     [1, 0, 0, 0, 0, 0]]
# Vektor med høgresider
b = [-4, -3, -3, 0, 0, 0]

###### Slutt på inputs #############

# Inverterar
Ainv = np.linalg.inv(A)
# Gjer b til ein søylevektor
b = np.transpose(b)
# Multipliserar
Svar = np.matmul(Ainv, b)

# Skriv svaret til skjerm
print('Svaret er', Svar)

# Reknar ut temp:
t=11+47/60
p = Svar[0]*t**3 + Svar[1]*t**2 + Svar[2]*t + Svar[3]
print(p) 