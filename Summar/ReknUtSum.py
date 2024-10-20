"""Dette skriptet reknar ut ein sum.
Her er uttrykket for ledda i summen hardkoda
inni løkka. 
Øvre grense for summen er gitt som input i 
starten - hardkoda det også.
"""

# Importere
import numpy as np

# Øvre grense
N = 1000
# Nedre grense
n0 = 1

# Initierar summen
S = 0
# Merk: For at for-løkka skal ta med N, må vi gå forbi i range-kallet
for n in range(n0,N+1):
  an = 1/n**2
  S = S + an

# Skriv svaret til skjerm:
print(f'Sum: {S:.5f}')

# Samanliknar med eventuell fasit
Fasit = np.pi**2/6
print(f'Feil: {np.abs(Fasit-S):.5f}')
