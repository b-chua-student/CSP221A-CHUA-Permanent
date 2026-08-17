import unittest
import inspect
from src.rover import Rover
from src.drone import Drone

class RobotSubclassTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.drone = Drone(name="Reaper")
        self.rover = Rover(name="Curiosity")

    def test_different_perform_task_implementation(self) -> None:
        self.assertNotEqual(inspect.getsource(self.drone.perform_task), inspect.getsource(self.rover.perform_task)) # Compare raw source code text of function object as string. Demonstrates first-class functions by passing function as argument.
