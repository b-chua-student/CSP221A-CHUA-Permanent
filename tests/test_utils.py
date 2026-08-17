import unittest
import io
from contextlib import redirect_stdout 
from utils import *
from src.drone import Drone
from src.rover import Rover

class UtilsTestCase(unittest.TestCase):
    def test_fleet_report(self) -> None:
        robots = [Drone(name="Reaper"), Rover(name="Curiosity"), Rover(name="Opportunity", battery=0)]

        output_str = io.StringIO() # Instantiating StringIO class. From Python docs: A text stream using an in-memory text buffer. It inherits from TextIOBase.
        with redirect_stdout(output_str): # Redirect fleet report print output from sys.stdout to StringIO instance.
            fleet_report(robots)

        for robot in robots:
            self.assertIn( # Check if output of subclass str() method is in output_str
                str(robot), 
                output_str.getvalue() # Return string containing content of entire buffer
            )
    
    def test_run_task_safely_insufficient_battery_logs_error(self) -> None:
        drone = Drone(name="Reaper", battery=1)
        self.assertLogs(run_task_safely(drone))

    def test_run_task_safely_success(self) -> None:
        drone = Drone(name="Reaper")

        output_str = io.StringIO()
        with redirect_stdout(output_str): # capture print output into output_str
            run_task_safely(drone)

        PERFORM_TASK_RETURN_VALUE = None
        FINALLY_PRINT_OUTPUT = f"{drone.name} at {drone.battery}% battery."

        self.assertIn(str(PERFORM_TASK_RETURN_VALUE), output_str.getvalue())
        self.assertIn(FINALLY_PRINT_OUTPUT, output_str.getvalue())
