"""Skriptet plottar ein periodisk funksjon saman med trunkterte Fourier-rekker 
av stadig høgare orden.

Mellom -3 og 0 er funksjonen lik -x, mellom 0 og 3 er den konstant lik 0.
Den er periodisk med periode T = 6.

Skriptet plottar funksjonen over tre periodar - saman med Fourier-summar 
av aukande orden til og med ein Nmax, som er hardkoda i skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Bestemme maksimal N-verdi (input)
Nmax = 20

# Periode og frekvens
T = 6
w = 2*np.pi/T

# Initierar vektor med 200 x-verdiar mellom -9 og 9
Npkt = 500
x = np.linspace(-9, 9, Npkt)


# Tilordnar a0 og initerar vektor for Fourier-summen (konstant lik a0).
a = 3/4
y = a*np.ones(Npkt)
n = 0
plt.figure(1)

# Itererar ved aa auke trunkeringsgrensa N
while n <= Nmax: 
  # Nytt plott
  plt.clf()
  # Plottar sjølve funksjonen (tre periodar)
  plt.plot([-3, 0, 3], [3, 0, 0], 'k-')
  plt.plot([3, 6, 9], [3, 0, 0], 'k-')
  plt.plot([-9, -6, -3], [3, 0, 0], 'k-')
  
  # Plottar Fourier-summen for den aktuelle trunkeringa
  plt.plot(x, y, 'r--')
  
  # Pyntar på plottet
  TitleStr = f'Fourier-sum med N = {n}'
  plt.title(TitleStr)
  plt.grid(visible = True)          # Rutenett
  plt.ylim(-0.5,3.5)
  
  # Oppsdaterar n
  n = n+1
  # Oppdaterar koeffisientane a og b - og sjølve Fourier-summen y
  b = 3/(n*np.pi)*(-1)**n
  y = y + b*np.sin(n*w*x)
  if np.mod(n,2) == 1:              # a-koeffisentane er null for partals-n
      a = -6/(n*np.pi)**2
      y = y + a*np.cos(n*w*x)
  
    # Legg inn ein pause
  plt.show(block=False)
  plt.pause(0.1)
  plt.waitforbuttonpress()
