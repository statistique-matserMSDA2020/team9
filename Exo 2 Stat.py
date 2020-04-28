import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
data = np.loadtxt("donnees.txt")
xi=data[::1,0]
yi=data[::1,1]
a, b = np.polyfit(xi, yi, 1)
a, b, r, p_value, std_err = linregress(xi, yi)

plt.plot(xi, yi, "o") # les points (x, y) representes par des points
plt.plot( # droite de regression
    [min(xi), max(xi)],                  # valeurs de x
    [a * min(xi) + b, a * max(xi) + b],  # valeurs de y
    "y",                           # couleur rouge avec un trait continu
    label="regression")             # legende

plt.title("Regression Lineaire") # titre de graphique
plt.show()
