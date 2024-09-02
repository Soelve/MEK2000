"""Dette skriptet reknar ut dei n foerste ledda i ei talfoelge gitt
ved ei differenslikning av første orden.
All input er hard-koda.
"""

# Maksimal n
Nmax = 4

# Startkrav
a0 = 4
# Skriv startkravet til skjerm
print('n= 0 , a_n=', a0)

# Initierar a og aOld
a = a0
aOld = a0
for n in range(1,Nmax+1):      # Det der med Nmax+1 er ganske forvirrande...
    # Oppdaterar gamle a
    aOld = a
    # Reknar ut ny a
    a = a/2
    # Skriv a til skjerm
    print('n=',n, ', a_n=', a)