import math
import numpy as np
from matplotlib import pyplot as plt
import random
import matplotlib.ticker as ticker

x_path_end_position = []
y_path_end_position = []
endpoint = []

for i in range(10000):
    def generate_random_angles_relative(number_of_turns):
        rel_angles = []
        angles = []
        for i in range(number_of_turns):
            angle = random.randint(-35, 35)
            angles.append(angle)
        for a in range(len(angles)):
            # first generated number is the same in both cases (absolute-relative)
            if a == 0:
                rel_angles.append(angles[0])
            else:
                rel_angles.append(angles[a])
                rel_angles[a] = angles[a] + rel_angles[a-1]
        # printing absolute random angles to check if relatives are correct
        # print('\nrandom angles: ', angles)
        return rel_angles

    # decide the number of turns in param
    rand_angles_rel = generate_random_angles_relative(30)

    # print('relative random angles: ', rand_angles_rel, '\n')


    def calc_path(pos_x, pos_y, steering_angles):
        path = []
        # time including: time, deg
        for deg in steering_angles:
            pos_x = np.around(pos_x + math.cos(math.radians(deg)))
            pos_y = np.around(pos_y + math.sin(math.radians(deg)))
            path.append((pos_x, pos_y))
        return path


    random_relative_path = calc_path(0, 0, rand_angles_rel)

    x_random_relative = list(zip(*random_relative_path))[0]
    y_random_relative = list(zip(*random_relative_path))[1]

    x_path_end_position.append(x_random_relative[-1])
    y_path_end_position.append(y_random_relative[-1])


# plt.hist(endpoint, 50, edgecolor='black', color="#2ecc71")
# plt.title("Distribution of end position y coordinates")
# plt.xlabel("end position y coordinate")
# plt.ylabel("value")
# ax_y_coord = plt.axes()
# ax_y_coord.xaxis.set_major_locator(ticker.MultipleLocator(5))
# ax_y_coord.xaxis.set_minor_locator(ticker.MultipleLocator(1))
# plt.savefig('fig2.png')
# plt.show()


plt.hist2d(x_path_end_position, y_path_end_position, bins=(40, 40), cmap=plt.cm.jet)
plt.colorbar()
plt.xlabel("x value")
plt.ylabel("y value")
# plt.savefig('no_obstacles_histogram2d.png')
plt.show()
