import math
import numpy as np
from matplotlib import pyplot as plt
import random


obstacle1 = (2, 2, 6, 3)
obstacle2 = (8, 8, 6, 4)
obstacle3 = (15, 2, 4, 2)
obstacle4 = (8, -3, 4, 2)
obstacle5 = (23, -2, 4, 2)


obstacle_list = [obstacle1, obstacle2, obstacle3, obstacle4, obstacle5]


def is_in_wall(x, y):
    collided = False
    collisions = []
    for index, obstacle in enumerate(obstacle_list):
        if obstacle[0] <= x <= (obstacle[0] + obstacle[2]) \
                and obstacle[1] <= y <= (obstacle[1] + obstacle[3]):
            collisions.append((index, x, y))
            collided = True
    return collided, collisions


collision_list = []


def remove_nesting(nested_list):
    for i in nested_list:
        if type(i) == list:
            remove_nesting(i)
        else:
            collision_list.append(i)


x_path_end_position = []
y_path_end_position = []
collisions = 0

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
        collision = []
        # time including: time, deg
        for deg in steering_angles:
            pos_x = np.around(pos_x + math.cos(math.radians(deg)))
            pos_y = np.around(pos_y + math.sin(math.radians(deg)))
            if is_in_wall(pos_x, pos_y)[0]:
                collision.append((pos_x, pos_y))
            path.append((pos_x, pos_y))
        return path, collision

    if len(calc_path(0, 0, rand_angles_rel)[1]) == 0:
        random_relative_path = calc_path(0, 0, rand_angles_rel)[0]

        x_random_relative = list(zip(*random_relative_path))[0]
        y_random_relative = list(zip(*random_relative_path))[1]

        x_path_end_position.append(x_random_relative[-1])
        y_path_end_position.append(y_random_relative[-1])
    else:
        collisions += 1

print('num of collisions: ', collisions)
plt.hist2d(x_path_end_position, y_path_end_position, bins=(40, 40), cmap=plt.cm.jet)
plt.colorbar()
plt.xlabel("x value")
plt.ylabel("y value")
# plt.savefig('obstacles_histogram2d.png')
plt.show()
