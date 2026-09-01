import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm

# Funksjon som vi vil plotte
def funk(a,b):
#    return x**2 + y**2
    return (3-(a+b*1))**2 + (4-(a+b*2.5))**2 + (4.5-(a+b*3))**2

# Grenser for x og y (hardkoda)
aMin = -2;
aMax = 5;
bMin = -2;
bMax = 4;

# Vektor - og matriser - med funksjonsverdiar (200 pkt i kvar retning)
a = np.linspace(aMin, aMax, 200)
b = np.linspace(bMin, bMax, 200)
aa, bb = np.meshgrid(a, b)

# Matrise med z-verdiar
S_mat = funk(aa, bb)

# Ny 3d-figur til å lage flateplott
fig = plt.figure(1)
plt.clf()
ax = fig.add_subplot(111, projection='3d')
# Lagar flateplott i rommet
surf = ax.plot_surface(aa, bb, S_mat, cmap = cm.magma, alpha = .5)
Aminval = 2.25
Bminval = 0.731
Sminval = funk(Aminval, Bminval)
ax.plot(Aminval, Bminval, Sminval, 'rx')
# Tekst på aksane
ax.set_xlabel('a')
ax.set_ylabel('b')
plt.show()

plt.figure(2)
plt.clf()
plt.pcolor(aa, bb, S_mat)
plt.show()
