import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, sqrt, atan2, pi
from python.program.navigator import parking_lot


k_distance = 2
k_alpha = 6
k_beta = -4
dt = 0.01

draw = parking_lot.ParkingLot()

# Corners of rectangle like vehicle when pointing to the right (0 radians)
p1_init = np.array([1, -0.5, 1])
p2_init = np.array([1, 0.5, 1])
p3_init = np.array([-1, 0.5, 1])
p4_init = np.array([-1, -0.5, 1])


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
    distance_init = sqrt(x_diff**2 + y_diff**2)
    distance = sqrt(x_diff**2 + y_diff**2)

    x_path = []
    y_path = []

    while distance > 0.01:
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
        # steering the car towards the goal while k_beta*beta rotates the line
        steering = k_alpha*alpha + k_beta*beta

        if distance > distance_init - 1:
            v = v/3
        elif distance > distance_init - 2:
            v = v/2

        # reversing the vehicle when the goal is behind the robot
        if alpha > pi/2 or alpha < -pi/2:
            v = -9

        heading_angle = heading_angle + steering*dt

        x = x + v*cos(heading_angle)*dt
        y = y + v*sin(heading_angle)*dt
        x_path.append(x)
        y_path.append(y)

        plt.cla()
        plt.arrow(x_start, y_start, cos(start_heading_angle),
                  sin(start_heading_angle), color='r', width=0.1)
        plt.arrow(x_goal, y_goal, cos(goal_heading_angle),
                  sin(goal_heading_angle), color='g', width=0.1)
        plot_vehicle(x, y, heading_angle, x_path, y_path, len(x_path))
    print("finished")
    print(len(x_path))


def plot_vehicle(x, y, heading_angle, x_path, y_path, steps):
    """
    Plotting the vehicle and it's path using the rotation matrix for visualize.
    Plotting the parking lot as well.
    :param x: actual x position of the vehicle
    :param y: actual y position of the vehicle
    :param heading_angle: heading angle
    :param x_path: x trajectory
    :param y_path: y trajectory
    :param steps: number of steps in the motion, using for generating images with numbered names
    :return: none
    """

    r = rotation_matrix(x, y, heading_angle)
    # using the rotation matrix to make the vehicle follow the path
    p1 = np.matmul(r, p1_init)
    p2 = np.matmul(r, p2_init)
    p3 = np.matmul(r, p3_init)
    p4 = np.matmul(r, p4_init)

    # plotting a little * to the middle of the vehicle front: (x1 + x2) / 2
    # represents the car and it's direction
    plt.plot([(p1[0] + p2[0]) / 2], p1[1], 'k*')
    # draw the lines between the 4 corners of the vehicle
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-')
    plt.plot([p2[0], p3[0]], [p2[1], p3[1]], 'k-')
    plt.plot([p3[0], p4[0]], [p3[1], p4[1]], 'k-')
    plt.plot([p4[0], p1[0]], [p4[1], p1[1]], 'k-')

    draw.plot_parking_lot()

    # plotting the path of vehicle
    plt.plot(x_path, y_path, 'b--')
    plt.savefig('pictures/'f'fig-0{steps}.png')
    # plt.show()


# use it to rotate the vehicle
def rotation_matrix(x, y, heading_angle):
    return np.array([
        [cos(heading_angle), -sin(heading_angle), x],
        [sin(heading_angle), cos(heading_angle), y],
        [0, 0, 1]
    ])


if __name__ == '__main__':
    x_start = 6.5
    y_start = 8
    start_heading_angle = pi/2
    x_goal = 18.5
    y_goal = 9
    goal_heading_angle = -pi/2

    print("Start x: %.2f m\nStart y: %.2f m\nStart heading angle: %.2f rad\n" % (x_start, y_start, start_heading_angle))
    print("Start x: %.2f m\nGoal y: %.2f m\nGoal heading angle: %.2f rad\n" % (x_goal, y_goal, goal_heading_angle))
    moving_vehicle(x_start, y_start, start_heading_angle, x_goal, y_goal, goal_heading_angle)
