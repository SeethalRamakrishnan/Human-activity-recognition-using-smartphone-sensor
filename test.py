import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = [1,1,1,1,2,2,2,2,2,2,2,2,4,4,4,4,4,3,5,5,5,5,6,6]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, normed=1,facecolor='blue',rwidth=0.85)
plt.show()