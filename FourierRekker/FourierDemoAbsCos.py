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
Nmax = 5

# Periode og frekvens
T = np.pi
w = 2*np.pi/T

# Initierar vektor med 200 x-verdiar over 4 periodar
Npkt = 200
x = np.linspace(-2*T, 2*T, Npkt)


# Allokerar vektor for Fourier-koeffisientane
Avector = np.zeros(Nmax+1)
# Tilordnar a0 og initerar vektor for Fourier-summen. (Konstant lik a0.)
a = 2/np.pi
y = a*np.ones(Npkt)
n = 1
Avector[0] = a

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
  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid(visible=True)                                # Rutenett

  # Oppdaterar koeffisientane a og b - og sjølve Fourier-summen y
  a = -4*(-1)**n/(np.pi*(4*n**2-1))
  Avector[n] = a
  y = y + a*np.cos(n*w*x)
  n = n+1
  
  # Legg inn ein pause
  plt.show(block=False)
  plt.pause(0.1)
  plt.waitforbuttonpress()
  
# Plottar histogram over Fourier-koeffisientane
plt.figure(2)
plt.clf()  
plt.bar(np.arange(Nmax+1), Avector)
plt.title('Fourier-koeffisientar')
plt.xlabel('n')
plt.ylabel(r'$a_n$')
plt.grid(visible=True)
plt.show()
