"""Dette skriptet less inn eit (fiktivt) datasett der fiskebestanden
i eit relativt lite vatn har blitt logga årvis gjennom 40 år. Det plottar
tidsserien - i tillegg til å plotte estimat av farten bestanden veks med 
som funksjon av bestanden sjølv. Den interpolerar og gjer kvadratisk regresjon
på sistnemnde.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Les inn data
data = np.loadtxt("Fiskebestand.dat", delimiter=",", skiprows=1)

# Vektorar med argument
Tid = data[:, 0]
Bestand = data[:, 1]

# Tel elementa
n = len(Tid)

# Plottar bestand, tidsserien
plt.figure(1)
plt.clf()
plt.plot(Tid, Bestand, 'k--')
plt.plot(Tid, Bestand, 'rx')
plt.grid(visible=True)
plt.xlabel('År')
plt.ylabel('Bestand')
plt.show()

# Estimerar vekstfart ved hjelp av midtpunktsfprmelen for derivasjon
# Allokerar
Bestand_mean = np.zeros(n-1)
Vekstfart = np.zeros(n-1)
for i in range(n-1):
    Bestand_mean[i] = (Bestand[i]+Bestand[i+1])/2
    # Midtpunktsformelen
    Vekstfart[i] = (Bestand[i+1]-Bestand[i])/(Tid[i+1]-Tid[i])    

# Plottar rådata
plt.figure(2)
plt.clf()
plt.plot(Bestand_mean,Vekstfart,'rx', label='Data')
plt.grid(visible=True)
plt.xlabel('Bestand')
plt.ylabel('Vekstfart')
plt.show()    

# Plottar vekstfart - med rådata, interpolerande spline og kvadratisk regresjon
# Vektor til plotting
bestand_plott = np.linspace(np.min(Bestand), np.max(Bestand), 500)
# Bestemmer kvadratisk pline
spline = make_interp_spline(Bestand_mean, Vekstfart)
# Kvadratisk regresjon
koeff = np.polyfit(Bestand_mean, Vekstfart, 2)
regresjon_plott = koeff[0]*bestand_plott**2 + koeff[1]*bestand_plott + koeff[2]
# Sjølve plottet
plt.figure(3)
plt.clf()
# Plottar rådata
plt.plot(Bestand_mean,Vekstfart,'rx', label='Data')
# Plottar interpoleringa
plt.plot(bestand_plott,spline(bestand_plott),'b--', label='Kvadratisk spline')
# Plottar regresjonen
plt.plot(bestand_plott,regresjon_plott,'k-', label = 'Kvadratisk regresjon')
plt.grid(visible=True)
plt.xlabel('Bestand')
plt.ylabel('Vekstfart')
plt.legend()
plt.show()