"""Dette skriptet plottar ein modell for flo og fjøre.
"""

# Bibliotek
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 24, 200)
V = 0.67*np.sin(0.51*t+0.7)

# Plottar
plt.figure(1)
plt.clf()
# Plottar modellen
plt.plot(t, V, 'b-')
# Plottar tidspunkta då vass-standen er 0.5 m
plt.hlines(0.5, 0, 24, colors = 'black', linestyles = 'dashed')
plt.plot([0.28, 3.14, 12.60, 15.46], 0.5*np.ones(4), 'ro')
plt.xlabel('Tid [timar]')
plt.ylabel('Vannstand [meter]')
plt.grid(visible=True)
plt.show()
