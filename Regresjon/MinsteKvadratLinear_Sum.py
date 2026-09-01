"""
 Dette skriptet tar utgangspunkt i eit sett med punkt og 
 bestemmer ei regresjonslinje for dei ved minste kvadraters metode.
 Her blir koeffisientane i funksjonen rekna ut via ein furmel med summar.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Punkt
x = [1, 2.5, 3]
y = [3, 4, 4.5]

########### Slutt på input ##################

n = len(x)          				# Antal punkt

# Konvertere til array
x = np.array(x)
y = np.array(y)

# Gjennomsnitt
x_mean = 1/n*sum(x)
y_mean = 1/n*sum(y)
# Reknar ut b-koeffisienten
b = sum((x-x_mean)*(y-y_mean))/sum((x-x_mean)**2)
# Reknar ut a-koeffisientet
a = y_mean - b*x_mean

# Skriv koeffisentane til skjerm
print("Koeffisientar:")
print("a =", a)
print("b =", b)

# Plottar punkta og regresjonslinja (brukar same x-verdiar som datasettet)
plt.figure(1)
plt.clf()
plt.plot(x, y, 'rx')  
plt.plot(x, a+b*x, 'k-')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(visible = True)                           		# Legg på rutenett  
plt.show()