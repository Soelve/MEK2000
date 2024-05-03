"""
Dette skriptet plottar ein modell for flo og fjoere
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 24, 200)
V = 0.67*np.sin(0.51*t+0.7)

# Plottar
plt.close()
plt.plot(t, V, 'b-')

# Plottar tidspunkta då vannstanden er 0.5 m
plt.hlines(0.5, 0, 24, colors = 'black', linestyles = 'dashed')
"""
plt.plot([0.28, 3.09, 12.60, 15.41], 0.5*np.ones(4), 'ro')
plt.xlabel('Tid [timar]')
plt.ylabel('Vannstand [meter]')
"""