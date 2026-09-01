"""
 Dette skriptet tar utgangspunkt i eit sett med punkt og 
 bestemmer ei regresjonslinje for dei ved minste kvadraters metode.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Punkt
x = [1, 2.5, 3]
y = [3, 4, 4.5]

########### Slutt på input ##################

N = len(x)          				# Antal punkt

x = np.transpose(x) 				# Transponerar x
y = np.transpose(y) 				# Transponerar y

# Set opp A-matrisa
A = np.array([np.ones(N), x])
A = np.transpose(A)

# Bestemmer koeffisientane i regresjonslinja
InvMat = np.matmul(np.transpose(A), A)         	# A^T A
InvMat = np.linalg.inv(InvMat)                 	# inversen  til A^T A
ATy = np.matmul(np.transpose(A), y)
Coeff = np.matmul(InvMat, ATy)

# Hentar ut koeffisientane
a = Coeff[0]
b = Coeff[1]
# Skriv koeffisentane til skjerm
print("Koeffisientar:")
print("a =", a)
print("b =", b)

# Plottar punkta og regresjonslinja
plt.figure(1)
plt.clf()
plt.plot(x, y, 'rx')  
plt.plot(x, a+b*x, 'k-')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(visible = True)                           		# Legg på rutenett  
plt.show()
