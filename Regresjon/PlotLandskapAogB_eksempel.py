import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm

# Funksjon som vi vil plotte
def funk(x,y):
#    return x**2 + y**2
    return (3-(x+ y*1))**2 + (4-(x+y*2.5))**2 + (4.5-(x+y*3))**2

# Grenser for x og y (hardkoda)
xMin = 0;
xMax = 3;
yMin = 0;
yMax = 2;

# Vektor - og matriser - med funksjonsverdiar (200 pkt i kvar retning)
x = np.linspace(xMin, xMax, 200)
y = np.linspace(yMin, yMax, 200)
xx, yy = np.meshgrid(x, y)

# Matrise med z-verdiar
zz = funk(xx, yy)

# Ny 3d-figur til å lage flateplott
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
# Lagar flateplott i rommet
surf = ax.plot_surface(xx, yy, np.log(zz), cmap = cm.magma, alpha = .5)
Aminval = 2.25
Bminval = 0.731
Cminval = funk(Aminval, Bminval)
ax.plot(Aminval, Bminval, np.log(Cminval), 'rx')
# Tekst på aksane
ax.set_xlabel('a')
ax.set_ylabel('b')
