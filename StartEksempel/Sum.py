"""
Dette skriptet reknar ut ein sum. Det tar eit algebraisk uttrykk for kvart
ledd som input (linje 15). I tillegg tar det start- og sluttverdi for indeksen 
n som input.
"""

# Importerar numpy - i fall vi treng det
import numpy as np

# Gir start- og sluttverdi for indeksen
n_start = 1
n_max = 5

# Gir uttrykk for ledda
def a(n):
    return 1/(n**2+1)

##############################################

# Initerarsummen
S = 0

# Summerar alle ledda
for n in range(n_start, n_max+1):     # Dette med "+1" er ganske forvirrande
    S = S + a(n)
    
# Skriv svar til skjerm    
print('S = ', S)    
