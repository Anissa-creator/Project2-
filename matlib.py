#Anissa Champiom
#project 2 

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
y = np.array([20,98,87,86,112,77,103,88,92,79,78,84,89])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='spring')

plt.colorbar()

plt.show()
