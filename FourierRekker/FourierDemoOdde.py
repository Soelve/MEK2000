
"""
Skriptet plottar ein periodisk funksjon saman med trunkterte Fourier-rekker 
av stadig høgare orden.

Funksjonen er 1 mellom 0 og pi og -1 mellom -pi og 0. Perioden er 2 pi.

Skriptet plottar funksjonen over tre periodar - saman med Fourier-summar 
av aukande orden til og med ein Nmax, som er hardkoda i skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Bestemme maksimal N-verdi (input)
Nmax = 10

# Periode og frekvens
T = 2*np.pi
w = 2*np.pi/T

# Initierar vektor med 200 x-verdiar mellom -9 og 9
Npkt = 200
x = np.linspace(-3*np.pi, 3*np.pi, Npkt)


# Tilordnar a0 og initerar vektor for Fourier-summen. (Konstant lik a0.)
y = np.zeros(Npkt)
n = 0
# Itererar ved aa auke trunkeringsgrensa N
while n <= Nmax: 
  # Nytt plott
  plt.close()
  plt.figure(1)
  # Plottar sjølve funksjonen (tre periodar)
  plt.plot([0, np.pi], [1, 1], 'k-')
  plt.plot([np.pi, 2*np.pi], [-1, -1], 'k-')
  plt.plot([2*np.pi, 3*np.pi], [1, 1], 'k-')
  plt.plot([-3*np.pi, -2*np.pi], [-1, -1], 'k-')
  plt.plot([-2*np.pi, -np.pi], [1, 1], 'k-')
  plt.plot([-np.pi, 0], [-1, -1], 'k-')
  # Plottar Fourier-summen for den aktuelle trunkeringa
  plt.plot(x,y, 'r--')
  # Set tittelen
  TitleStr = f'Fourier-sum med N = {2*n+1}'
  plt.title(TitleStr)
  plt.grid()                                # Rutenett
  plt.show()
  # Oppsdaterar n
  # Oppdaterar koeffisientane a og b - og sjølve Fourier-summen y
  b = 4/(np.pi*(2*n+1))
  y = y + b*np.sin((2*n+1)*w*x)
  n = n+1
  # Legg inn ein pause
  dummy = input('Hit enter')
  
  
  