"""
Dette skriptet reknar ut dei n foerste ledda i ei talfoelge gitt
ved ei differenslikning av andre orden
All input er hard-koda
"""

# Maksimal n
Nmax = 4

# Startkrav
a0 = 2
a1 = 4
# Skriv startkravet til skjerm
print('n= 0 , a_n=', a0)
print('n= 1 , a_n=', a1)

# Initierar a og aOld
a = a1
aOld = a0
for n in range(2,Nmax+1):      # Det der med Nmax+1 er ganske forvirrande...
    # Oppdaterar gamle a
    aOlder = aOld
    aOld = a
    # Reknar ut ny a
    a = 2*aOld -2*aOlder + n
    # Skriv a til skjerm
    print('n=',n, ', a_n=', a)