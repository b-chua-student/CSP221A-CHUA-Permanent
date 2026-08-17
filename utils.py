from src.robot import Robot
from src.drone import Drone
from exceptions import InsufficientBatteryError
import logging

def fleet_report(robots: list[Robot]) -> None:
    for robot in robots:
        print(str(robot))

def run_task_safely(robot: Robot, **kwargs) -> None:
    try:
        output = robot.perform_task()
    except InsufficientBatteryError as e:
        logging.error(
            f"{e.name} requires {e.required_battery}% battery for this task, but only has {e.available_battery}% battery left.",
            exc_info=True, 
            stack_info=True
        )
    else:
        print(output)
    finally:
        print(
            f"{robot.name} at {robot.battery}% battery."
        )
