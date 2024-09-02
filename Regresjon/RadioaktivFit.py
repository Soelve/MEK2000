"""Dette skriptet tar utgangspunkt i eit gitt sett med data for 
radioaktivitet og brukar dette til å estimere ein eksponentiell
samanheng mellom tid og radioaktivitet. Denne kan, i sin tur, brukast
til å estimere halveringstida for den radioaktive isotopen.
Vi gjer dette ved å bruke lineær regresjon med minste kvadraters metode
på logaritmen (den naturlege logaritmen) på dei sampla data. 
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt


# Les inn data
data =  np.loadtxt("RadioaktivData.dat", delimiter=",")
tid = data[:, 0]              # Data for tida (dagar)
Aktiv = data[:, 1]              # Data for aktivetet (kilo-Bequerel)

########### Slutt på input ##################

# For regresjonen: Logaritmen av A, ikkje A
AktivLog = np.log(Aktiv)

N = len(tid)          				# Antal punkt

# Set opp A-matrisa
A = np.array([np.ones(N),tid])
A = np.transpose(A)

# Bestemmer koeffisientane i regresjonslinja
InvMat = np.matmul(np.transpose(A),A)          	# A^T A
InvMat = np.linalg.inv(InvMat)                 	# inversen  til A^T A
ATy = np.matmul(np.transpose(A),AktivLog)
Coeff = np.matmul(InvMat,ATy)

# Hentar ut koeffisientane
a = Coeff[0]
b = Coeff[1]
# Skriv koeffisentane til skjerm
print("Koeffisientar:")
print("a =", a)
print("b =", b)

# Plottar punkta og regresjonslinja - for den lineære samanhengen
plt.figure(1)
plt.clf()
plt.plot(tid,AktivLog,'rx', label = 'Logaritmen av A-data')  
plt.plot(tid,a+b*tid,'k-', label = 'Lineær tilnærming')
plt.legend()
plt.xlabel('Tid')
plt.ylabel('log(A)')
plt.grid(visible = True)                           		# Legg på rutenett  
plt.show()
 
# Plottar tilsvarande figur for den eksponentielle samanhengen
plt.figure(2)
plt.clf()
plt.plot(tid,Aktiv,'rx', label = 'Datapunkt, A')  
plt.plot(tid,np.exp(a+b*tid),'k-', label = 'Eksponentiell tilnærming')
plt.legend()
plt.xlabel('Tid')
plt.ylabel('A(t)')
plt.grid(visible = True)                           		# Legg på rutenett  
plt.show()
