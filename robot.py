from abc import ABC, abstractmethod

class Robot(ABC):

    # Avoid 'magic constants' by naming important values
    MAX_BATTERY_VALUE: int = 100
    MIN_BATTERY_VALUE: int = 0

    manufacturer: str = "Boston Dynamics"
    _population: int = 0

    def __init__(self, name: str, battery: int = MAX_BATTERY_VALUE):
        self.name = name
        self._battery = battery # _single_leading_underscore to signal protected instance attribute and for internal use only
        self._population += 1

    @property
    def battery(self) -> int:
        return self._battery # 

    @battery.setter
    def battery(self, charge: int) -> None:
        if not (self.MIN_BATTERY_VALUE <= charge <= self.MAX_BATTERY_VALUE):
            raise ValueError(f"Charge must be between {self.MIN_BATTERY_VALUE} and {self.MAX_BATTERY_VALUE}, but got {charge}")

        self._battery = charge

    @property 
    # setting population as property was not in the instructions but population should be read-only and NOT accessible outside this class to ensure it is the source of truth for the instance count.
    def population(self) -> int:
        return self._population
    
    def __str__(self):
        return f"Robot: {self.name}, {self._battery}%.__battery"

    def __repr__(self):
        return f"Robot(name={self.name},.__battery={self._battery}, manufacturer={self.manufacturer}, population={self._population})"

    @abstractmethod
    def perform_task(self) -> None:
        pass
