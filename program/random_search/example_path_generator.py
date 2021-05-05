import numpy as np
import math
from matplotlib import pyplot as plt
import random

obstacle_coordinates = []


def store_obstacle(x1, y1, x2, y2):
    obstacles = []
    for i in range(x1, (x1 + x2 + 1)):
        for j in range(y1, (y1 + y2 + 1)):
            obstacles.append((i, j))
    return obstacles


obstacle_coordinates.append(store_obstacle(2, 2, 4, 2))
obstacle_coordinates.append(store_obstacle(8, 8, 2, 4))


print(obstacle_coordinates)

for index, obstacle in enumerate(obstacle_coordinates):
    print(index)
    for coord in obstacle:
        print(coord)


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
        if obstacle[0] <= x <= (obstacle[0] + obstacle[2])\
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


def generate_random_angles_absolute(number_of_turns):
    random_angles = []
    for i in range(number_of_turns):
        angle = random.randint(-15, 15)
        random_angles.append(angle)
    return random_angles


def generate_random_angles_relative(number_of_turns):
    rel_angles = []
    angles = []
    for i in range(number_of_turns):
        angle = random.randint(-25, 25)
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


rand_angles_rel = generate_random_angles_relative(30)


def calc_path(pos_x, pos_y, steering_angles):
    path = []
    collisions = []
    # time including: time, deg
    for deg in steering_angles:
        pos_x = pos_x + math.cos(math.radians(deg))  # *time || *(v*t)
        pos_y = pos_y + math.sin(math.radians(deg))  # *time || *(v*t)
        # collision check
        if is_in_wall(pos_x, pos_y)[0]:
            collisions.append(is_in_wall(pos_x, pos_y)[1])
        path.append((pos_x, pos_y))
    return path, collisions


random_relative_path = calc_path(0, 0, rand_angles_rel)[0]
random_relative_path_collisions = calc_path(0, 0, rand_angles_rel)[1]


x_random_relative = list(zip(*random_relative_path))[0]
y_random_relative = list(zip(*random_relative_path))[1]

obstacle_objects = []
x_random_relative_collision = []
y_random_relative_collision = []

print('\nx relative: ', x_random_relative)
print('y relative: ', y_random_relative)
print('\n path: ', random_relative_path)
remove_nesting(random_relative_path_collisions)
print('collisions: ', collision_list)
if len(collision_list) > 0:
    x_random_relative_collision = list(zip(*collision_list))[1]
    y_random_relative_collision = list(zip(*collision_list))[2]


plt.figure()
rectangle1 = plt.Rectangle((2, 2), 6, 3, fc='blue', ec='red')
plt.gca().add_patch(rectangle1)
rectangle2 = plt.Rectangle((8, 8), 6, 4, fc='blue', ec='red')
plt.gca().add_patch(rectangle2)
rectangle3 = plt.Rectangle((15, 2), 4, 2, fc='blue', ec='red')
plt.gca().add_patch(rectangle3)
rectangle4 = plt.Rectangle((8, -3), 4, 2, fc='blue', ec='red')
plt.gca().add_patch(rectangle4)
rectangle5 = plt.Rectangle((23, -2), 4, 2, fc='blue', ec='red')
plt.gca().add_patch(rectangle5)


plt.plot(x_random_relative, y_random_relative, 'black')
plt.xlabel("x coordinates")
plt.ylabel("y coordinates")
plt.legend(collision_list, loc='upper left', bbox_to_anchor=(0, 1.17), handletextpad=-0.1, handlelength=0)
#plt.savefig('fig15.png')
plt.show()
