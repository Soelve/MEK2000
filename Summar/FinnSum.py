"""
Vi reknar ut ein sum. All input er hardkoda.
"""

# bibliotek
#import numpy as np

# Øvre og nedre indieks
n0 = 0
N = 10000000

# Initerar summen S
S = 0

# Itererar
for n in range(n0, N+1):
    an = 3*(-1/4)**n
    S = S + an
    
# skrive svar til skjerm
print('Summen er', S,'.')   
