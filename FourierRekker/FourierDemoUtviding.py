
"""Skriptet plottar ein funksjon saman med trunkterte Fourier-rekker 
av stadig høgare orden for dei halvperiodiske utvidingane - både 
den jamne og den odde utviginda.

Den oprinnelege funksjonen, som berre er definert for x mellom 0 og 1, er
f(x) = x(1-x).

Skriptet plottar funksjonen over fem periodar - saman med Fourier-summar 
av aukande orden til og med ein Nmax, som er hardkoda i skriptet.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Bestemme maksimal N-verdi (input)
# Merk at orden for trunkerinange er 2N for den jamne og 2N-1 for den 
# odde utvidinga
Nmax = 7

# Periode og frekvens
T = 2
w = 2*np.pi/T

# Vektor for éin periode
NpktPeriod = 100
xPeriod = np.linspace(0, T/2, NpktPeriod)
yPeriod = xPeriod*(1-xPeriod)

# Initierar vektor med 200 x-verdiar over fem periodar
Npkt = 200
x = np.linspace(-2*T, 3*T, Npkt)


# Tilordnar a0 og initerar vektor for Fourier-summane.
a = 1/6
yJ = a*np.ones(Npkt)    # Jamn utviding
yO = np.zeros(Npkt)     # Odde utviding
n = 0
# Itererar ved aa auke trunkeringsgrensa N
while n <= Nmax: 
  # Nytt plott
  plt.close()
  plt.figure(1)
  # Plottar sjølve funksjonen (ein halv periode)
  plt.plot(xPeriod, yPeriod, 'k-', linewidth = 2)
  # Plottar Fourier-summen for den aktuelle trunkeringa
  plt.plot(x , yJ, 'r--', linewidth = 1)
  plt.plot(x , yO, 'b-.', linewidth = 1)
  plt.grid()                                # Rutenett
  plt.axis([-2*T, 3*T, -.3, .3])
  plt.show()
  # Oppsdaterar n
  n = n+1
  # Oppdaterar koeffisientane a og b - og sjølve Fourier-summen y
  a = -1/np.pi**2/n**2
  b = 8/np.pi**3/(2*n-1)**3
  yJ = yJ + a*np.cos(2*n*w*x)
  yO = yO + b*np.sin((2*n-1)*w*x)
  # Legg inn ein pause
  dummy = input('Hit enter')
  
