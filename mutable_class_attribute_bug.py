from robot import Robot

class ClassAttrRobot(Robot):
    robot_type: list[str] = []

    def __init__(self, name, type: str, battery = Robot.MAX_BATTERY_VALUE):
        super().__init__(name, battery)
        ClassAttrRobot.robot_type.append(type)

    def perform_task(self) -> None:
        pass

class InstanceAttrRobot(Robot):
    def __init__(self, name, type: str, battery = Robot.MAX_BATTERY_VALUE):
        super().__init__(name, battery)
        self.robot_type = type

    def perform_task(self) -> None:
        pass

# Create robot subclasses with shared class attribute
bugged_drone = ClassAttrRobot(name="Reaper", type="Drone")
bugged_rover = ClassAttrRobot(name="Curiosity", type="Rover")

# Create robot subclasses with unique instance attributes
correct_drone = InstanceAttrRobot(name="Reaper", type="Drone")
correct_rover = InstanceAttrRobot(name="Curiosity", type="Rover") 

def display_attr_status(robot_1, robot_2) -> None:

    print(f"{robot_1.name} has type: {robot_1.robot_type}")
    print(f"{robot_2.name} has type: {robot_2.robot_type}")

    if robot_1.robot_type is robot_2.robot_type:
        print(f"Two different robots share the same list of robot types.")
    else:
        print(f"Two different robots do not share list of robot types.")

    print()

display_attr_status(bugged_drone, bugged_rover)
display_attr_status(correct_drone, correct_rover)



