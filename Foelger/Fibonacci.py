"""Dette skriptet reknar ut Fibonacci-tala. I tillegg sjekkar det
løysinga vi kjem fram til når vi løyser differenslikninga med 
startkrava. Begge svara blir skrivne til skjerm -- i tillegg til 
forholdet mellom to etterfølgande ledd. Dette siste konvergerar
rakst mot det gyldne snittet.
Merk at vi startar indekseringa på n=0 her."""

# Importerar NumPy
import numpy as np

# Maksimalt ledd
N = 20

# Tilordnar dei første ledda
a_old = 1
a_older = 1
a = a_old

# Koeffisientar i løysinga
A = (np.sqrt(5)-1)/(2*np.sqrt(5))
B = (np.sqrt(5)+1)/(2*np.sqrt(5))

for n in range(2,N+1):
    # Oppdaterar førre ledd
    a_older = a_old
    a_old = a
    # Nytt ledd
    a = a_old + a_older
    # Frå løysinga
    a_loeysing = A*(-(np.sqrt(5)-1)/2)**n + B*((np.sqrt(5)+1)/2)**n
    # Skriv til skjerm
    print('n=',n,'a_diff=',a, f'a_loeysing={a_loeysing:.4f}', 
          f'Forhold: {a/a_old:.10f}.')
    
# Til slutt: Skriv det gyldne snitt til skjerm:
phi = (np.sqrt(5)+1)/2
print(f'Det gyldne snitt: {phi:.10f}')