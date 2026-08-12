import unittest
import io
from contextlib import redirect_stdout 
from utils import *
from drone import Drone
from rover import Rover

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
