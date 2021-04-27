import unittest

from navigator.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    """
    Vehicle test
    """
    
    def test_zero_speed(self):
        vehicle = Vehicle((0, 0), 0)
        vehicle.speed = 0
        vehicle.steering_angle = 0
        vehicle.drive(10)
        self.assertEqual(vehicle.position, (0, 0))

    # TODO: Test negative time value for driving (with expected ValueError)!
