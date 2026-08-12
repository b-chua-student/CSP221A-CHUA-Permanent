from robot import Robot

def fleet_report(robots: list[Robot]) -> None:
    for robot in robots:
        print(str(robot))
