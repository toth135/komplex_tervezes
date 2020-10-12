import python.path_calculation as path_calc
import matplotlib.pyplot as plt

plt.plot(path_calc.rand_angles_abs, 'r')
plt.ylabel('steering angles')
plt.xlabel('time')
plt.plot(path_calc.rand_angles_rel, 'black')
plt.ylabel('steering angles')
plt.xlabel('time')
plt.show()
