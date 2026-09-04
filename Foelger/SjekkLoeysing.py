"""Dette skriptet reknar ut dei N foerste ledda i ei talfoelge gitt
ved ei differenslikning av første orden. Den samanliknar det
vi får frå differenslikninga med løysinga vi har funne frå før.
All input er hard-koda.
"""

# Maksimal n
N = 10

# Startkrav
a0 = 8

# Initierar a_diff og aOld
a_diff = a0
for n in range(0,N):      # Det der med Nmax+1 er ganske forvirrande...
    # Løysinga:
    a_loeys = 8*(1/2)**n
    # Skriv n, og a-verdiane til skjerm
    print('n=',n,', a_diff=',a_diff,', a_loeysing=', a_loeys)   
    # Oppdaterar gamle a og reknar ut ny frå differenslikninga
    aOld = a_diff
    a_diff = a_diff/2
    