"""Dette skriptet implementerar gradient-metoden for å finne (lokale) 
toppunkt for ein funksjon av to variable.
Input er
funk - funksjonen vi skal optimere
funk_x, funk_y - dei partielle deriverte av funksjonen
dfdx - den partialderiverte i x
dfdy - den partialderiverte i y
gamma - den såkalla læringsraten
L - minimalverdien for gradient-storleiken; stoppkriterium
x0 - startverdi for x
y0 - startverdi for y
"""

# Bibliotek
import numpy as np

# Parametrar
gamma = 0.1
L = 1e-5

# Startpunkt
x0 = 2
y0 = 1

# Funksjonar
# f(x, y)
def funk(x, y):
    return np.exp(-(x**2 + y**2))

# Dei partielt deriverte
def funk_x(x, y):
    return -2*x*np.exp(-(x**2 + y**2))

def funk_y(x, y):
    return -2*y*np.exp(-(x**2 + y**2))

# Initiere
xNy = x0
yNy = y0
GradVal = 1e5               # Finn på ein tilfeldig, høg verdi

# Telle-variabel
n = 0
while GradVal > L:
    # Kopierar dei gamle verdiane
    x = xNy
    y = yNy
    # Deriverte
    dfdx = funk_x(x,y)
    dfdy = funk_y(x,y)
    # Oppdaterar punkt
    xNy = x + gamma*dfdx
    yNy = y + gamma*dfdy
    # Lengda av gradienten
    GradVal = np.sqrt(dfdx**2 + dfdy**2)

    # Oppdaterar telle-variabel og skriv svar kvar 10. iterasjon til skjerm
    n = n+1
    if np.mod(n,10) == 0:
        print(f'n={n}, x={x:.5f}, y={y:.5f}')    
    
# Skriv resultat til skjerm
z = funk(x, y)
print(f'Maksimalverdi: {z:.4f}')
print(f'Maksimalpunkt: x={x:.4f} og y={y:.4f}')     