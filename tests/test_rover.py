import unittest
from rover import Rover
from robot import Robot

class RoverTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.rover = Rover(name="Curiosity")

    def test_super_init(self) -> None:
        self.assertEqual(self.rover.name, "Curiosity")

    def test_battery_usage(self) -> None:
        initial_battery_percentage = self.rover.battery
        self.rover.perform_task()
        self.assertNotEqual(initial_battery_percentage, self.rover.battery)

    def test_insufficient_battery_usage(self) -> None:
        with self.assertRaises(ValueError):
            self.rover.use_battery(101)

    def test_unique_attr(self) -> None:
        self.assertTrue(hasattr(self.rover, "max_speed"))
