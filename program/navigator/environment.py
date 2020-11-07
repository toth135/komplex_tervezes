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

    def is_in_wall(self, position):
        """
        Check that the given point is in wall.
        :param position: tuple of (x, y) coordinates
        :return: True, when the point is in the wall, else False
        """
        pass
