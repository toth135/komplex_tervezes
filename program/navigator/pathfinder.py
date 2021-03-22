import matplotlib.pyplot as plt
import numpy as np
import math


class AStarPathFinder(object):
    def __init__(self):
        self.obstacles = []
        self.obstacles.append(self.store_obstacle(2, 2, 6, 3))
        self.obstacles.append(self.store_obstacle(8, 8, 6, 4))
        self.obstacles.append(self.store_obstacle(15, 2, 4, 2))
        self.obstacles.append(self.store_obstacle(8, -3, 4, 2))
        self.obstacles.append(self.store_obstacle(23, -2, 4, 2))

    def heuristic(self, start, goal):
        """
        :param start: start position
        :param goal: goal position
        :return: distance between the start and goal positions
        """
        return math.sqrt(((start[0]) - goal[0]) ** 2 +
                         ((start[1]) - goal[1]) ** 2)

    def get_neighbours(self, position):
        """
        Returns the next step chosen from the neighbours
        :param position: actual position
        :return: next step
        """
        neighbour = []
        # Moves allowed in 8 direction from current position
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),
                       (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            x2 = position[0] + dx
            y2 = position[1] + dy
            neighbour.append((x2, y2))
        return neighbour  # returns the next step

    def calc_cost(self, current, next):
        """
        Calculates cost of step
        :param current: giving the current position
        :param next: next step
        :return:
        """
        for obstacle in self.obstacles:
            if next in obstacle:
                return 100  # Will not choose collided coordinate because of high cost
        return 1  # Every movement's cost except obstacle coordinates

    def check_points(self, start, end):
        """
        Exits with runtime error if user gives invalid parameters
        :param start: start position
        :param end: goal position
        :return: exits with error if user gives start or end
        coordinates in an obstacle
        """
        for obstacle in self.obstacles:
            for obs in obstacle:
                if start == obs:
                    raise RuntimeError('Start coordinate is inside an obstacle!')
                elif end == obs:
                    raise RuntimeError('End coordinate is inside an obstacle!')

    def store_obstacle(self, x1, y1, x2, y2):
        """
        Collects every coordinate that is inside an obstacle
        and stores it in a list of tuples
        :param x1: x left bottom
        :param y1: y left bottom
        :param x2: width
        :param y2: height
        :return: list of obstacle coordinates
        """
        obstacles = []
        for i in range(x1, (x1 + x2 + 1)):
            for j in range(y1, (y1 + y2 + 1)):
                obstacles.append((i, j))
        return obstacles


def a_star_search(start, end, map):
    """
    :param start: start position
    :param end: goal position
    :param map: list of obstacles
    :return: shortest path, cost of the steps
    """

    map.check_points(start, end)

    g = {}  # Actual movement cost to each position from the start position
    f = {}  # Estimated movement cost of start to end

    # Initialize starting values
    g[start] = 0
    f[start] = map.heuristic(start, end)

    closed_nodes = set()
    opened_nodes = {start}
    came_from = {}

    while len(opened_nodes) > 0:
        # Get the vertex in the open list with the lowest f score
        current = None
        current_f_score = None
        for pos in opened_nodes:
            if current is None or f[pos] < current_f_score:
                current_f_score = f[pos]
                current = pos

        # Check if we have reached the goal
        if current == end:
            # Retrace our path backward
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, f[end]  # done

        # Mark the current node as closed
        opened_nodes.remove(current)
        closed_nodes.add(current)

        # Update scores for nodes near the current position
        for neighbour in map.get_neighbours(current):
            if neighbour in closed_nodes:
                continue  # We have already processed this node
            candidate_g = g[current] + map.calc_cost(current, neighbour)

            if neighbour not in opened_nodes:
                opened_nodes.add(neighbour)  # Discovered a new node
            elif candidate_g >= g[neighbour]:
                continue  # This g score is worse than previously found

            # Adopt this g score
            came_from[neighbour] = current
            g[neighbour] = candidate_g
            h = map.heuristic(neighbour, end)
            f[neighbour] = g[neighbour] + h

    raise RuntimeError("A* failed to find a solution")


if __name__ == "__main__":
    map = AStarPathFinder()

    start = (0, 0)
    goal = (21, 3)

    path, cost = a_star_search(start, goal, map)
    print("path: ", path)
    print("cost: ", cost)

    x_coords = list(zip(*path))[0]
    y_coords = list(zip(*path))[1]

    # Drawing the rectangles based on the initialization of obstacles list
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

    # Actual A* path plot:
    # plt.plot(x_coords, y_coords, 'black')

    # Scatter A* path plot
    plt.scatter(x_coords, y_coords)

    # Mark start and end positions with red and green dots
    plt.plot(start[0], start[1], 'ro')
    plt.plot(goal[0], goal[1], 'go')

    # Polynomial curve fitting
    degree = round(cost / 3)
    f = np.poly1d(np.polyfit(x_coords, y_coords, degree))
    x_values = np.linspace(min(x_coords), max(x_coords), 100)
    plt.plot(x_values, f(x_values))
    print('\nf:')
    print(f)

    # 1st and 2nd derivative of f polynomial
    f_der1 = np.polyder(f, m=1)
    f_der2 = np.polyder(f, m=2)
    print('\nf_der1:')
    print(f_der1)
    print('\nf_der2:')
    print(f_der2)

    plt.plot(x_values, f_der1(x_values), 'black')
    plt.plot(x_values, f_der2(x_values), 'red')

    # plt.savefig('astar.png')
    plt.show()
