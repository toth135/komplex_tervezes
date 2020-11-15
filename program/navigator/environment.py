class Environment:
    """
    World representation
    """

    def __init__(self):
        self._walls = []

    @property
    def walls(self):
        return self._walls

    @walls.setter
    def walls(self, walls):
        self._walls = walls

    # def add_wall(self, x1, y1, x2, y2):
    #     self._walls.append((x1, y1, x2, y2))

    def is_in_wall(self, position):
        """
        Check that the given point is in wall.
        :param position: tuple of (x, y) coordinates
        :return: True, when the point is in the wall, else False
        """
        x, y = position

        for wall in self.walls:
            if wall[0] <= x <= wall[2] and wall[1] <= y <= wall[3]:
                return True
        return False
