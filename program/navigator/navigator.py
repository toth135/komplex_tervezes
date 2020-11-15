import python.program.navigator.environment as env


class Navigator:
    """
    Navigator for four-wheeled vehicles in a simplified environment
    """
    
    def __init__(self):
        self.environment = []

    def add_wall(self, x1, y1, x2, y2):
        self.environment.append((x1, y1, x2, y2))

    def find_path(self, vehicle_start, vehicle_finish, environment):
        """
        Estimate a path of the vehicle from start to finish positions.
        :param vehicle_start: the starting position
        :param vehicle_finish: the finish position
        :param environment: the map
        :return: list of angles
        """

        start_position = vehicle_start
        end_position = vehicle_finish
        environment = environment

        # NOTE: The step size is matter!
        return []
