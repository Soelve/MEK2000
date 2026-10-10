"""Skriptet plottar ein periodisk funksjon saman med trunkterte Fourier-rekker 
av stadig høgare orden.

Funksjonen er absoluttverdien av cos x - med periode pi.

Skriptet plottar funksjonen over tre periodar - saman med Fourier-summar 
av aukande orden til og med ein Nmax, som er hardkoda i skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Bestemme maksimal N-verdi (input)
Nmax = 10

# Periode og frekvens
T = np.pi
w = 2*np.pi/T

# Initierar vektor med 200 x-verdiar mellom -9 og 9
Npkt = 200
x = np.linspace(-3, 3, Npkt)


# Tilordnar a0 og initerar vektor for Fourier-summen. (Konstant lik a0.)
a = 2/np.pi
y = a*np.ones(Npkt)
n = 1
# Itererar ved aa auke trunkeringsgrensa N
while n <= Nmax: 
  # Nytt plott
  plt.figure(1)
  plt.clf()
  # Plottar sjølve funksjonen (tre periodar)
  plt.plot(x, np.abs(np.cos(x)), 'k-')
  # Plottar Fourier-summen for den aktuelle trunkeringa
  plt.plot(x, y, 'r--')
  # Set tittelen
  TitleStr = f'Fourier-sum med N = {n}'
  plt.title(TitleStr)
  plt.grid(visible=True)                                # Rutenett

  # Oppdaterar koeffisientane a og b - og sjølve Fourier-summen y
  a = -4*(-1)**n/(np.pi*(4*n**2-1))
  y = y + a*np.cos(n*w*x)
  n = n+1
  
  # Legg inn ein pause
  plt.show(block=False)
  plt.pause(0.1)
  plt.waitforbuttonpress()