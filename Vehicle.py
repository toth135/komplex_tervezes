import numpy as np
from matplotlib import pyplot as plt
import random


"""
    testing
"""


class Vehicle:
    def __init__(self, x, y, angles):
        self.position = [x, y]
        self.angles = angles


vehicle = Vehicle(0, 0, [10, 25, 6])
"""
    testing
"""
# print(vehicle.angles)


"""
problem: how to store the angles by time?
         later: angles will get two values: inside and outside wheel angle? 
         I had to use 2 simple arrays than concat them with numpy.array(). I have problems to access
         array content if I assign angle to time (like [(0, 6), (1, 12), ..., (n, n)]) to calculate with it..
calculation : xn (actual position) = x0 + integral(cos(angle(t))dt)
              yn ..                = y0 + integral(sin(angle(t))dt)
question: how to automate integration from t0 to t0, t1 to t2, ..., tn-1 to tn ??       
"""


# Constant (time, angle) values... to calc_path2 arguments

# a = np.array(steer_angles2)
# x = 0
# y = 0
# for t, d in steer_angles2:
    # print(f'{t} -> {d}')
    # x = x + math.cos(math.radians(d))
    # y = y + math.sin(math.radians(d))
    # print(x, y)












