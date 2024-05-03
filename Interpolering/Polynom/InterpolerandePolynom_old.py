# This script constructs an interpolating
# polynomial for a set of points. 
# It does so by inverting the Vandermonde matrix.
# This set of points is hard coded initially.

# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Vectors for interpolation (hard coded)
x = [1, 1.5, 3, 7]
y = [-1.2, .2, 3, 3.4]

# Vandermonde-matrix
VanMat = np.vander(x)
# Determine coefficients by matrix inversion
InvVanMat = np.linalg.inv(VanMat)
Coeff = np.matmul(InvVanMat,np.transpose(y))

# Vector for plotting polynomial (100 points)
LL = len(x)
xx = np.linspace(x[0]-0.2,x[LL-1]+0.2,100)
yy = np.zeros(100)

# Construct the interpolating polynomaial
for n in range(0,LL,1):
    yy = yy + Coeff[n]*xx**(LL-n-1)
    
# Plot the points - with lines and polynomial
plt.plot(x,y,'r*', label = 'Points')               # Just points
plt.plot(x,y,'k-', label = 'Linear splines')       # Lines between points
plt.plot(xx,yy,'b-.', label = 'Polynomial')        # Interpolating polynomial
plt.xlabel('x')
plt.ylabel('y')
plt.legend()