"""Dette skriptet plottar loeysinga av eit startverdiproblem saman med 
tilnaermingar funne ved aa trunkere Maclauring-rekka for loeysinga.

Startverdiproblemet er dette:
    y'- 2y = e^(-x), y(0) = -1/2.
    
Det kan loeysast ekstakt: y(x) =-1/6 e^(2x) - 1/3 e^(-x).

Loeysinga kan ogsaa tilnaermast med ei trunkert potens-rekke - altsaa eit 
Taylor-polynom:    
y(x) = \sum_{n=0}^\infty c_n x^n \approx \sum_{n=0}^N c_n (x-a)^n.

Her er det naturleg aa velge a som x_0 - den x-verdien som startkravet er 
gitt for. Her er det 0.

Skriptet plottar tilnaerminga for ulike verdiar av N. Maksimal N-verdi er
(hardkoda) input.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Bestemme maksimal N-verdi (input)
Nmax = int(input('Kor skal vi trunkere rekka? '))

# Startkrav - y_0
y0 = -1/2
# Vektorar med x- og y-verdiar
x = np.linspace(0, 2, 200)
y_exact = (1/3+y0)*np.exp(2*x)-1/3*np.exp(-x)

# Initierar c-koeffisienten og tilnærma løysing
c = y0
yTrunk = c*np.ones_like(x)
n = 0
# Itererar ved aa auke trunkeringsgrensa N
while n < Nmax: 
  plt.show()
  # Oppdaterar c, n og yTrunk
  c = (2*c + (-1)**n/np.math.factorial(n))/(n+1)
  n = n+1
  yTrunk = yTrunk + c*x**n

# Plottar resultatet
plt.figure(1)
plt.clf()
plt.plot(x, y_exact, 'k-', label = 'Eksakt loeysing')
LegendEntry = f'Tilnærming med N = {n-1}'
plt.plot(x,yTrunk, 'r--', label = LegendEntry)
plt.grid(visible = True)
plt.legend(loc = 'lower left')
