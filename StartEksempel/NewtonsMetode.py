"""
Dette er ei implementering av Newtons metode. Metoden tar følgande input:
* Funksjonen vi skal finne nullpunktet til
* Den deriverte av denne funksjonen
* Ei start-gjetning på løysinga
* Talet på iterasjonar
Alle desse er hard-koda i starten av skriptet.
"""

# Bibilotek
import numpy as np

# Funksjonen
def funk(x):
    return np.cos(x)-x

# Den deriverte
def funkDeriv(x):
    return -np.sin(x)-1

# Start-verdi
x0 = 0.5

# Talet på iterasjonar
Niter = 5

###################################

# Initerar x
x = x0    

# Iterasjons-skjema (Newtons metode)
for n in range(1,Niter+1):
    x = x - funk(x)/funkDeriv(x)
    
# Skriv svar til skjerm
print('x=', x, n)
    
    