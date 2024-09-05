"""Dette skriptet reknar brukar vi for aa finne ut kor mange ringar vi kan
ha i Hanoi-taarna foer antal flytt bikkar ein million.
Skriptet brukar ei while-løkke
"""


# Startkrav
a1 = 1

# Initierar a og indeksen n
a = a1
n = 1

# Skriv til skjerm
print(n, a)

# Gjentar saa lenge talet på flytt er mindre enn ein million
while a < 1000000:              
    # Oppdaterar gamal a
    aOld = a
    # Reknar ut ny a
    a = 2*aOld + 1
    # Oppdaterar talet på ringar
    n = n + 1
    print(n, a)
    
print(f'Antal ringar når vi bikkar ein million flytt: {n}')
