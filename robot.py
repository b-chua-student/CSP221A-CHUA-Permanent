from abc import ABC, abstractmethod

class Robot(ABC):

    # Avoid 'magic constants' by naming important values
    MAX_BATTERY_VALUE: int = 100
    MIN_BATTERY_VALUE: int = 0

    _manufacturer: str = "Boston Dynamics"
    _population: int = 0

    def __init__(self, name: str, battery: int = MAX_BATTERY_VALUE):
        self.name = name
        self.__battery = battery
        self._population += 1

    @property
    def battery(self) -> int:
        return self.__battery # double leading underscore to invoke name mangling

    @battery.setter
    def battery(self, charge: int) -> None:
        if not (self.MIN_BATTERY_VALUE <= charge <= self.MAX_BATTERY_VALUE):
            raise ValueError(f"Charge must be between {self.MIN_BATTERY_VALUE} and {self.MAX_BATTERY_VALUE}, but got {charge}")

        self.__battery = charge
    
    def __str__(self):
        return f"Robot: {self.name}, {self.__battery}%.__battery"

    def __repr__(self):
        return f"Robot(name={self.name},.__battery={self.__battery}, manufacturer={self._manufacturer}, population={self._population})"

    @abstractmethod
    def perform_task(self) -> None:
        pass
