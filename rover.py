from robot import Robot 
from logger import log_action

class Rover(Robot):

    def __init__(self, name: str, battery: int = Robot.MAX_BATTERY_VALUE, x: float = 0, y: float = 0, z: float = 0, max_speed: float = 10):
        super().__init__(name, battery)
        self.x = x
        self.y = y
        self.z = z
        self.max_speed = max_speed

    @log_action
    def perform_task(self) -> None:
        print("Testing all motors...")
        self.use_battery(3)

    def move_forward(self, distance_meter: float) -> None:
        self.y += distance_meter
        self.use_battery(10)

        print(f"Moved {distance_meter} feet away. Battery at {self.battery}")
