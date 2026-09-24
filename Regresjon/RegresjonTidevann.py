"""Dette skriptet less inn eit (fiktivt) datasett der fiskebestanden
i eit relativt lite vatn har blitt logga årvis gjennom 40 år. Det plottar
tidsserien - i tillegg til å plotte estimat av farten bestanden veks med 
som funksjon av bestanden sjølv. Den interpolerar og gjer kvadratisk regresjon
på sistnemnde.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Les inn data
data = np.loadtxt("Tidevann.dat", delimiter=",", skiprows=1)

# Vektorar med argument
Tid = data[:, 0]
Vannstand = data[:, 1]

# Tel elementa
n = len(Tid)

# Plottar vasstanden, tidsserien
plt.figure(1)
plt.clf()
plt.plot(Tid, Vannstand, 'b--')
plt.plot(Tid, Vannstand, 'rx')
plt.grid(visible=True)
plt.xlabel('Timar etter flo')
plt.ylabel('Vannstand')
plt.show()

# Plottar vasstand mot cos(pi/6*t)
plt.figure(2)
plt.clf()
plt.plot(np.cos(np.pi/6*Tid), Vannstand, 'rx')
plt.grid(visible=True)
plt.xlabel('Timar etter flo')
plt.ylabel('Vannstand')
plt.show()

# Gjennomfører regresjon
x = np.cos(np.pi/6*Tid)
y = Vannstand
x_mean = 1/n*sum(x)
y_mean = 1/n*sum(y)
b = sum((x-x_mean)*(y-y_mean))/sum((x-x_mean)**2)
a = y_mean - b*x_mean
plt.figure(2)
plt.plot(x,a+b*x,'k-')
plt.show()

# Plottar regresjonsresultat mot tid
plt.figure(3)
plt.clf()
Tid_plott = np.linspace(Tid[0], Tid[-1])
plt.plot(Tid_plott,a+b*np.cos(np.pi/6*Tid_plott),'k-')
plt.plot(Tid, Vannstand, 'b--')
plt.plot(Tid, Vannstand, 'rx')
plt.grid(visible=True)
plt.xlabel('Timar etter flo')
plt.ylabel('Vannstand')
plt.show()