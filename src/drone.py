from src.robot import Robot 

class Drone(Robot):

    def __init__(self, name: str, battery: int = Robot.MAX_BATTERY_VALUE, current_altitude_feet: int = 0):
        super().__init__(name, battery)
        self.current_altitude_feet = current_altitude_feet

    def perform_task(self) -> None:
        print("Testing all rotors...")
        self.use_battery(3)

    def fly(self, height_feet: int) -> None:
        print(f"Flying {height_feet} feet upwards...")

        self.current_altitude_feet += height_feet 
        print(f"Hovering at {self.current_altitude_feet}...")

        self.use_battery(height_feet)
