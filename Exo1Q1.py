from numpy.random import binomial
import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt

n, p, size = 30, 0.2, 10000
X=np.random.binomial(n,p,size)
plt.hist(X,bins=40)
plt.title("histogramme de la loi Binomiale")
plt.show()
