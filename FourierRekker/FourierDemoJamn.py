# -*- coding: utf-8 -*-
"""Skriptet plottar ein periodisk funksjon saman med trunkterte Fourier-rekker 
av stadig høgare orden.

Funksjonen er absoluttverdien av x - med periode 2.

Skriptet plottar funksjonen over tre periodar - saman med Fourier-summar 
av aukande orden til og med ein Nmax, som er hardkoda i skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Bestemme maksimal N-verdi (input)
Nmax = 20

# Periode og frekvens
T = 2
w = 2*np.pi/T

# Initierar vektor med 200 x-verdiar mellom -9 og 9
Npkt = 200
x = np.linspace(-3, 3, Npkt)


# Tilordnar a0 og initerar vektor for Fourier-summen. (Konstant lik a0.)
a = 1/2
y = a*np.ones(Npkt)
n = 0
# Itererar ved aa auke trunkeringsgrensa N
while 2*n <= Nmax: 
  # Nytt plott
  plt.figure(1)
  plt.clf()
  # Plottar sjølve funksjonen (tre periodar)
  plt.plot([-1, 0, 1], [1, 0, 1], 'k-')
  plt.plot([-3, -2, -1], [1, 0, 1], 'k-')
  plt.plot([1, 2, 3], [1, 0, 1], 'k-')
  # Plottar Fourier-summen for den aktuelle trunkeringa
  plt.plot(x, y, 'r--')
  # Set tittelen
  TitleStr = f'Fourier-sum med N = {2*n}'
  plt.title(TitleStr)
  plt.grid()                                # Rutenett
  plt.show()
  # Oppsdaterar n
  # Oppdaterar koeffisientane a og b - og sjølve Fourier-summen y
  a = -4/((2*n+1)*np.pi)**2
  y = y + a*np.cos((2*n+1)*w*x)
  n = n+1
  # Legg inn ein pause
  dummy = input('Hit enter')
