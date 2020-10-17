import numpy as np
import math
from matplotlib import pyplot as plt
import random
from matplotlib.cbook import flatten

'''
(time,angle) pairs
'''
# steer_angles2 = [(0, 6), (1, 12), (2, 32), (3, 22), (4, 15), (5, 6)]

# static steering angles for testing path calculation
steer_angles = [-5, 12, 13, 8, 4, 0, -4, -6, -8, -10, -12, -10, -8, -6,
                -4, -2, 0, 0, 0, 2, 4, 6, 8, 10, 12, 14, 18, 22, 16,
                10, 4, 0, -4, -8, -14, -18, -22, -14, -7, 0, 6, 7, 15,
                13, 12, 66, 66, 66, 66, 66, 66, 20, 20, 10, 10, 5,
                ]

# steer_angles3 = [(2, -5), (3, 0), (3, 6), (4, 12), (3, 9), (4, 18),
#                  (2, 22), (3, 13), (8, 3), (6, -12)]


def generate_random_angles_absolute(number_of_turns):
    random_angles = []
    for i in range(number_of_turns):
        # time = random.randint(1, 8)
        # angle = np.random.normal(-15, 15)
        angle = random.randint(-15, 15)
        random_angles.append(angle)
    return random_angles


def generate_random_angles_relative(number_of_turns):
    rel_angles = []
    angles = []
    for i in range(number_of_turns):
        angle = random.randint(-15, 15)
        angles.append(angle)
    for a in range(len(angles)):
        # first generated number is the same in both cases (absolute-relative)
        if a == 0:
            rel_angles.append(angles[0])
        else:
            rel_angles.append(angles[a])
            rel_angles[a] = angles[a] + rel_angles[a-1]
    # printing absolute random angles to check if relatives are correct
    print('\nrandom angles: ', angles)
    return rel_angles


def generate_evenly_spaced_randnums(number_of_turns):
    random_angles = []
    for i in range(number_of_turns):
        angle = random.randint(-15, 15)
        random_angles.append(angle)
    print('random_for_evenly:', random_angles)
    spaced_random_angles = []
    for i in range(len(random_angles)):
        if i > 0:
            # random_angles.append(np.arange(random_angles[0], random_angles[i]))
            # linspace skips some values between every item in list
            difference = abs(random_angles[i] - random_angles[i-1])
            spaced_random_angles.append(np.linspace(random_angles[i-1], random_angles[i], difference, dtype=int))
    return list(flatten(spaced_random_angles))


def generate_random_angles_gauss(number_of_turns):
    random_angles = []
    for i in range(number_of_turns):
        angle = np.random.normal(10, 1)
        random_angles.append(angle)
    return random_angles


even_list = generate_evenly_spaced_randnums(10)
print('random_evenly_linspace:', even_list)
# print('gauss: ', generate_random_angles_gauss(10))


# calling the angle generating functions, parameter: number of turns
rand_angles_abs = generate_random_angles_absolute(30)
rand_angles_rel = generate_random_angles_relative(30)

# printing relative angles under absolute
print('relative random angles: ', rand_angles_rel, '\n')

'''
# b = []
# print(type(b))
def evenly_spaced_numbers(angles):
    arr = []
    for i in range(len(angles)):
        arr.append(np.linspace(angles[i], angles[i-1], num=5))
    return arr
'''

# print(evenly_spaced_numbers(rand_angles_abs))


def calc_path(pos_x, pos_y, steering_angles):
    path = []
    # time including: time, deg
    for deg in steering_angles:
        pos_x = pos_x + math.cos(math.radians(deg))  # *time || *(v*t)
        pos_y = pos_y + math.sin(math.radians(deg))  # *time || *(v*t)
        path.append((pos_x, pos_y))
    return path


random_absolute_path = calc_path(10, 0, rand_angles_abs)
random_relative_path = calc_path(10, 0, rand_angles_rel)
evenly_path = calc_path(0, 0, even_list)


# printing the generated path under each other for better visibility
# using zip to get x and y values from the generated list
print('x_absolute: ', list(zip(*random_absolute_path))[0])
print('y absolute: ', list(zip(*random_absolute_path))[1])
print('\nx relative: ', list(zip(*random_relative_path))[0])
print('y relative: ', list(zip(*random_relative_path))[1])
print('\nx evenly_speced_path:', list(zip(*evenly_path))[0])
print('y evenly_speced_path:', list(zip(*evenly_path))[1])

# Test print out
# print(x_path[:, 0])
# print(y_path[:, 1])

# Draw rectangles
plt.figure()
rectangle1 = plt.Rectangle((20, 1), 5, 0.5, fc='blue', ec='red')
plt.gca().add_patch(rectangle1)
rectangle2 = plt.Rectangle((30, 0.3), 3, 1, fc='blue', ec='red')
plt.gca().add_patch(rectangle2)
rectangle3 = plt.Rectangle((36.5, 0.7), 6, 0.5, fc='blue', ec='red')
plt.gca().add_patch(rectangle3)

# coordinates
x_random = list(zip(*random_absolute_path))[0]
y_random = list(zip(*random_absolute_path))[1]
x_random_relative = list(zip(*random_relative_path))[0]
y_random_relative = list(zip(*random_relative_path))[1]
x_evenly_spaced = list(zip(*evenly_path))[0]
y_evenly_spaced = list(zip(*evenly_path))[1]

# Plot the path
plt.plot(x_random, y_random, 'r')
plt.plot(x_random_relative, y_random_relative, 'black')
plt.plot(x_evenly_spaced, y_evenly_spaced, 'green')
plt.show()


# unfinished path calculation based on the documentation
def calc_path2(start_position, steer_angles2):
    new_x_position = [0]
    new_y_position = [0]

    # convert incoming list to array
    array = np.array(steer_angles2)
    times = array[:, 0]
    angles = array[:, 1]

    for i in range(len(times)):
        # Test print out
        # print(times[i], angles[i])
        new_x_position = start_position[0]  # + integral goes here...


'''
    calling methods for testing..
'''
# calc_path(start_position, steer_angles, time)
# calc_path2(start_position, steer_angles2)

"""
    - How to position barriers?
    - Function that decides if there was collision
        => Re-coordinate the barriers in separate class or function
    - New function or class for optimization process? 

    - how to include speed and time to path calculation
    - how will the trajectory change by that
    - creating barriers (by rectangles)
"""