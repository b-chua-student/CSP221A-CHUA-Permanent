import unittest
from src.robot import Robot

class DummyRobot(Robot):
    def perform_task(self) -> None: # perform_task() implementation should handle the battery cost 
        self.use_battery(10)

class MockRobot(Robot):
    def perform_task(self) -> None:
        self.use_battery(10)

class RobotTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy_robot = DummyRobot("R2D2")

    def test_population_increment_on_instantiation(self) -> None:
        self.assertEqual(self.dummy_robot.population, 1)

    def test_population_decrement_on_deletion(self) -> None:
        initial_population = self.dummy_robot.population

        temp_robot = DummyRobot("BB-8")
        self.assertEqual(self.dummy_robot.population, initial_population + 1)

        del temp_robot
        self.assertEqual(self.dummy_robot.population, initial_population)

    def test_shared_population(self) -> None:
        self.assertEqual(self.dummy_robot.population, 1)

        mock_robot = MockRobot("C3PO")
        self.assertEqual(self.dummy_robot.population, 2)

    def test_initialization(self) -> None:
        self.assertEqual(self.dummy_robot.name, "R2D2")
        self.assertEqual(self.dummy_robot.battery, 100)

    def test_battery_getter(self) -> None:
        self.assertEqual(self.dummy_robot.battery, 100)

    def test_battery_setter(self) -> None:
        self.dummy_robot.battery = 50
        self.assertEqual(self.dummy_robot.battery, 50)

    def test_battery_setter_clamped(self) -> None:
        self.dummy_robot.battery = -100
        self.assertEqual(self.dummy_robot.battery, 0)
        self.dummy_robot.battery = 200
        self.assertEqual(self.dummy_robot.battery, 100)

    def test_shared_manufacturer(self) -> None:
        mock_robot = MockRobot("C3PO")
        self.assertEqual(self.dummy_robot.manufacturer, mock_robot.manufacturer)


