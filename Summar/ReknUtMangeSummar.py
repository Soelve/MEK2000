"""Dette skriptet reknar ut mange delsummar for ei rekke.
Her er uttrykket for ledda i summen hardkoda
inni løkka. 
Delsummane blir rekna ut, ein og ein, frå og med ein
Nmin til og med ein Nmax - i steg på Nstep.
"""

# Importere
import numpy as np

# Øvre grenser
Nmin = 10
Nmax = 50
Nstep = 10

# Nedre grense
n0 = 2

# for-løkke som går over alle øvre grenser
for N in range(Nmin,Nmax+1,Nstep):
    # Initierar summen
    S = 0
    # Merk: For at for-løkka skal ta med N, må vi gå forbi i range-kallet
    for n in range(n0,N+1):
        an = 2/(n**2-1)
        S = S + an

    # Skriv svaret til skjerm:
    print(f'Øvre grense: {N:d}, Sum: {S:.5f}')