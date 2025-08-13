"""
Dette skriptet reknar ut ein sum. Det tar eit algebraisk uttrykk for kvart
ledd som input (linje 15). I tillegg tar det start- og sluttverdi for indeksen 
n som input.
"""

# Initerarsummen
S = 0

# Gir start- og sluttverdi for indeksen
n_start = 0
n_max = 100

for n in range(n_start, n_max+1):     # Dette med "+1" er ganske forvirrande
    S = S + n**2 
    
print('S = ', S)    
