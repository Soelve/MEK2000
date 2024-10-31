"""Dette skriptet implementerar gradient-metoden for å finne (lokale) 
toppunkt for ein funksjon av to variable.
Input er
funk - funksjonen vi skal optimere
dfdx - den partialderiverte i x
dfdy - den partialderiverte i y
gamma - den såkalla læringsraten
L - minimalverdien for gradient-storleiken; stoppkriterium
h - liten verdi som blir brukt til å estimere deriverte
x0 - startverdi for x
y0 - startverdi for y
"""

# Bibliotek
import numpy as np

# Parametrar
gamma = 0.1
L = 1e-5
h = 1e-3

# Startpunkt
x0 = 2
y0 = 1

# Funksjonar
# f(x, y)
def funk(x, y):
    return np.exp(-(x**2 + y**2))

# Initiere
xNy = x0
yNy = y0
GradVal = 1e5               # Finn på ein tilfeldig, høg verdi

while GradVal > L:
    # Kopierar dei gamle verdiane
    x = xNy
    y = yNy
    # Deriverte
    dfdx = (funk(x+h, y) - funk(x-h, y))/(2*h)
    dfdy = (funk(x, y+h) - funk(x, y-h))/(2*h)
    # Oppdaterar punkt
    xNy = x + gamma*dfdx
    yNy = y + gamma*dfdy
    # Lengda av gradienten
    GradVal = np.sqrt(dfdx**2 + dfdy**2)
    
# Skriv resultat til skjerm
z = funk(x, y)
print(f'Maksimalverdi: {z:.4f}')
print(f'Maksimalpunkt: x={x:.4f} og y={y:.4f}')     
