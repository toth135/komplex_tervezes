import math
from matplotlib import pyplot as plt

path = [(1, 2), (3, 3), (5, 9), (6, 12)]
path_x = [1, 3, 5, 2]
path_y = [2, 3, 9, 6]

plt.figure()
plt.plot(path_x, path_y, 'r*')
plt.show()

path_x = [0] * 100
path_y = [0] * 100

for i in range(100):
    t = i / 100
    path_x[i] = t
    path_y[i] = math.sin(t)