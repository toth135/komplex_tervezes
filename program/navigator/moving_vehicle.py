import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, sqrt, atan2, pi


k_distance = 2
k_alpha = 6
k_beta = -2
dt = 0.01

parking_spaces_1 = [
    # vertical lines
    (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
    (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10),
    (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10),
    (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10),
    (17, 4), (17, 5), (17, 6), (17, 7), (17, 8), (17, 9), (17, 10),
    (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (20, 9), (20, 10),
    (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (23, 10),
    # horizontal lines
    (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7),
    (13, 7), (14, 7), (15, 7), (16, 7), (17, 7), (18, 7), (19, 7), (20, 7),
    (21, 7), (22, 7), (23, 7)
]

parking_spaces_2 = [
    # vertical lines
    (5, 17), (5, 18), (5, 19), (5, 20), (5, 21), (5, 22), (5, 23),
    (8, 17), (8, 18), (8, 19), (8, 20), (8, 21), (8, 22), (8, 23),
    (11, 17), (11, 18), (11, 19), (11, 20), (11, 21), (11, 22), (11, 23),
    (14, 17), (14, 18), (14, 19), (14, 20), (14, 21), (14, 22), (14, 23),
    (17, 17), (17, 18), (17, 19), (17, 20), (17, 21), (17, 22), (17, 23),
    (20, 17), (20, 18), (20, 19), (20, 20), (20, 21), (20, 22), (20, 23),
    (23, 17), (23, 18), (23, 19), (23, 20), (23, 21), (23, 22), (23, 23),
    # horizontal lines
    (5, 20), (6, 20), (7, 20), (8, 20), (9, 20), (10, 20), (11, 20), (12, 20),
    (13, 20), (14, 20), (15, 20), (16, 20), (17, 20), (18, 20), (19, 20), (20, 20),
    (21, 20), (22, 20), (23, 20)
]

# storing parking lot coordinates for obstacle detection later if needed..
parking_lot = [parking_spaces_1, parking_spaces_2]
parkinglot_list = []


# Corners of rectangle like vehicle when pointing to the right (0 radians)
p1_i = np.array([0.5, -0.25, 1])
p2_i = np.array([0.5, 0.25, 1])
p3_i = np.array([-0.5, 0.25, 1])
p4_i = np.array([-0.5, -0.25, 1])

x_path = []
y_path = []


# in case of list correction
def remove_nesting(nested_list):
    for i in nested_list:
        if type(i) == list:
            remove_nesting(i)
        else:
            parkinglot_list.append(i)


def moving_vehicle(x_start, y_start, start_heading_angle, x_goal, y_goal, goal_heading_angle):
    """
    Calculates the trajectory and calls vehicle plotting function to visualize it
    :param x_start: x start coordinate of vehicle
    :param y_start: y start coordinate of vehicle
    :param start_heading_angle: vehicle's heading angle at the start
    :param x_goal: x goal coordinate of vehicle
    :param y_goal: y goal coordinate of vehicle
    :param goal_heading_angle: vehicle's target heading angle at the goal position
    :return: none
    """
    x = x_start
    y = y_start
    heading_angle = start_heading_angle

    x_diff = x_goal - x
    y_diff = y_goal - y
    distance = sqrt(x_diff**2 + y_diff**2)

    # remove_nesting(parking_lot)
    # obstacle_x = list(zip(*parkinglot_list))[0]
    # obstacle_y = list(zip(*parkinglot_list))[0]

    while distance > 0.001:
        x_diff = x_goal - x
        y_diff = y_goal - y

        # variables for setting vehicle orientation

        # distance between start and goal
        distance = sqrt(x_diff**2 + y_diff**2)
        # alpha is the angle of the goal vector with respect to the vehicle's current "pose"
        alpha = atan2(y_diff, x_diff) - heading_angle
        # beta is the angle between the car's position and the goal position plus the goal angle
        beta = goal_heading_angle - heading_angle - alpha

        # control the velocity proportionally to the distance from goal
        v = k_distance*distance
        # driving the car towards the goal while k_beta*beta rotates the line
        w = k_alpha*alpha + k_beta*beta

        # reversing the vehicle when the goal is behind the robot
        if alpha > pi/2 or alpha < -pi/2:
            v = -v

        heading_angle = heading_angle + w*dt
        x = x + v*cos(heading_angle)*dt
        y = y + v*sin(heading_angle)*dt
        x_path.append(x)
        y_path.append(y)

        # # obstacle avoidance
        # for obst_x in obstacle_x:
        #     for obst_y in obstacle_y:
        #         if obst_x - x < 0.25 and obst_y - y < 0.25:
        #             print('collided at: ', (x, y))
        #             v = -v

        # print(alpha)

    plt.cla()
    plt.arrow(x_start, y_start, np.cos(start_heading_angle),
              np.sin(start_heading_angle), color='r', width=0.1)
    plt.arrow(x_goal, y_goal, np.cos(goal_heading_angle),
              np.sin(goal_heading_angle), color='g', width=0.1)
    plot_vehicle(x, y, heading_angle, x_path, y_path)
    # print(x_path, y_path)
    print("finished")


def plot_vehicle(x, y, heading_angle, x_path, y_path):
    """
    Plotting the vehicle and it's path using the rotation matrix for visualize.
    Plotting the parking lot as well.
    :param x: actual x pos of vehicle
    :param y: actual y pos of vehicle
    :param heading_angle: heading angle
    :param x_path: x trajectory
    :param y_path: y trajectory
    :return: none
    """
    r = rotation_matrix(x, y, heading_angle)

    # using the rotation matrix to make the vehicle follow the path
    p1 = np.matmul(r, p1_i)
    p2 = np.matmul(r, p2_i)
    p3 = np.matmul(r, p3_i)
    p4 = np.matmul(r, p4_i)

    # print(p1)
    # print(p2)

    # plotting a little * to the middle of the vehicle front: (x1 + x2) / 2
    # represents the car and it's direction
    plt.plot([(p1[0] + p2[0]) / 2], p1[1], 'k*')
    # draw the lines between the 4 corners of the vehicle
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-')
    plt.plot([p2[0], p3[0]], [p2[1], p3[1]], 'k-')
    plt.plot([p3[0], p4[0]], [p3[1], p4[1]], 'k-')
    plt.plot([p4[0], p1[0]], [p4[1], p1[1]], 'k-')

    # line points for parking lot plotting
    plt_verticals_1 = [[(5, 4), (5, 10)]]
    plt_verticals_2 = [[(8, 4), (8, 10)]]
    plt_verticals_3 = [[(11, 4), (11, 10)]]
    plt_verticals_4 = [[(14, 4), (14, 10)]]
    plt_verticals_5 = [[(17, 4), (17, 10)]]
    plt_verticals_6 = [[(20, 4), (20, 10)]]
    plt_verticals_7 = [[(23, 4), (23, 10)]]

    plt_verticals_8 = [[(5, 17), (5, 23)]]
    plt_verticals_9 = [[(8, 17), (8, 23)]]
    plt_verticals_10 = [[(11, 17), (11, 23)]]
    plt_verticals_11 = [[(14, 17), (14, 23)]]
    plt_verticals_12 = [[(17, 17), (17, 23)]]
    plt_verticals_13 = [[(20, 17), (20, 23)]]
    plt_verticals_14 = [[(23, 17), (23, 23)]]

    plt_horizontals_1 = [[(5, 7), (23, 7)]]
    plt_horizontals_2 = [[(5, 20), (23, 20)]]

    # plot all the lines one by one to avoid connecting the lines by their endpoints
    for p in plt_verticals_1:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_2:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_3:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_4:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_5:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_6:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_7:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_8:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_9:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_10:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_11:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_12:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_13:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_verticals_14:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_horizontals_1:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    for p in plt_horizontals_2:
        plt.plot([v[0] for v in p], [v[1] for v in p], 'k-')

    # plotting the path of vehicle
    plt.plot(x_path, y_path, 'b--')
    plt.show()


# use it to rotate the vehicle
def rotation_matrix(x, y, heading_angle):
    return np.array([
        [cos(heading_angle), -sin(heading_angle), x],
        [sin(heading_angle), cos(heading_angle), y],
        [0, 0, 1]
    ])


if __name__ == '__main__':
    x_start = 12
    y_start = 17
    start_heading_angle = pi/2
    x_goal = 18
    y_goal = 9
    goal_heading_angle = -pi/2
    print("Start x: %.2f m\nStart y: %.2f m\nStart heading angle: %.2f rad\n" % (x_start, y_start, start_heading_angle))
    print("Start x: %.2f m\nGoal y: %.2f m\nGoal heading angle: %.2f rad\n" % (x_goal, y_goal, goal_heading_angle))
    moving_vehicle(x_start, y_start, start_heading_angle, x_goal, y_goal, goal_heading_angle)
