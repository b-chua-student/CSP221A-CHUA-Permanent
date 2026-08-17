import unittest
from src.rover import Rover
from exceptions import InsufficientBatteryError
from logger import *

ensure_log_directories("logs/tests/")
configure_logging("logs/tests/test_rover.logs", "rover")

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
        with self.assertRaises(InsufficientBatteryError):
            self.rover.use_battery(101)

    def test_unique_attr(self) -> None:
        self.assertTrue(hasattr(self.rover, "max_speed"))

    def test_wrapped_method_preserved(self) -> None:
        self.assertEqual(self.rover.perform_task.__name__, "perform_task")
