import unittest
from src.drone import Drone
from exceptions import InsufficientBatteryError

class DroneTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.drone = Drone(name="Reaper")

    def test_super_init(self) -> None:
        self.assertEqual(self.drone.name, "Reaper")

    def test_battery_usage(self) -> None:
        initial_battery_percentage = self.drone.battery
        self.drone.perform_task()
        self.assertNotEqual(initial_battery_percentage, self.drone.battery)

    def test_insufficient_battery_usage(self) -> None:
        with self.assertRaises(InsufficientBatteryError):
            self.drone.use_battery(101)

    def test_unique_attr(self) -> None:
        self.assertTrue(hasattr(self.drone, "current_altitude_feet"))
