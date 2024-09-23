"""Dette skriptet estimerar eit integral ved hjelp
av ei trunkert Maclaurin-rekke.
Det samanliknar estimatet med eit anna vi har funne
ved hjelp av trapesmetoden og svært mange punkt.
"""

# Bibliotek
import numpy as np
import math

# Les inn - frå skjerm - kor vi skal trunkere rekka
N = int(input('Kor mange ledd skal vi ta med i rekka? '))

# Initerar summen
s = 0
for n in range(0, N+1):
    s = s + (-1)**n/math.factorial(2*n)*2/(4*n+1)
    
# Skriv svaret til skjerm 
print(f'Integral-estimat via rekke: {s:.8f}, {N+1} ledd')    

# Trapes-estimat med 1000 ledd
x = np.linspace(-1, 1, 1000)
y = np.cos(x**2)
trapz_int = np.trapz(y, x)
print(f'Integral-estimat med trapesmetoden: {trapz_int:.8f}, 1000 punkt')    
