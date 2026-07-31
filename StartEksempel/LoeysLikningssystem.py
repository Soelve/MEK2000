"""
Dette skriptet løyser eit lineært likningssystem. Systemet er formulert
som Ax = b, der A er ei kvadtisk, inverterbar matrise, x er ein søylevektor
med dei ukjende variablane og b er ein gitt søylevektor med like mange element
som x."""

# importerar NumPy-biblioteket
import numpy as np

# Koeffisientmatrisa
A = [[1, 2, 1], [2, 1, 1], [1, 1, 2]]
# Høgresida
b = [1, 2, 3]

######################################

# Bestemmer invers-matrisa
Ainv = np.linalg.inv(A)
# Reknar ut løysinga
x = np.matmul(Ainv,b)

# Skriv svaret til skjerm
print(x)