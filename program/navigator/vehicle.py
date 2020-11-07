class Vehicle:
    """
    Vehicle with four wheels
    """

    def __init__(self, position, direction):
        # TODO: Use the dimensions of the vehicle!
        self._position = position
        self._direction = direction
        self._speed = 0
        self._steering_angle = 0

    # TODO: Add getters and setters for position, direction, speed and steering angle!

    def steer(self, angle):
        """
        Rotate the steering wheel by the given steering angle.
        :param angle: difference in steering in degree
        :return: None
        """
        self._steering_angle += angle

    def drive(self, time):
        """
        Drive the vehicle according to the actual speed and steering angle.
        :param time: the duration of the driving in seconds.
        :return: None
        """
        # TODO: Calculate the position of the car after the given time of driving!
        pass
