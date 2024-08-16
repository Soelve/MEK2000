"""
Dette skriptet løyser ei andregradslikning.
Koeffisientane i polynomet er hard-koda inn i starten.
"""

# Importere NumPy
import numpy as np

# Gir koeffisientane
a = 1
b = -3
c = 2

# Reknar ut løysingane - dersom dei er reelle
if b**2-4*a*c >= 0:
    x_1 = (-b - np.sqrt(b**2-4*a*c)) / (2*a)
    x_2 = (-b + np.sqrt(b**2-4*a*c)) / (2*a)

    # Skriv løysingane til skjerm
    print('x1 =', x_1)
    print('x2 =', x_2)
else:
    print('Likninga har ingen reelle løysingar')
      