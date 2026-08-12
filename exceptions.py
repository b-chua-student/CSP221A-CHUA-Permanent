class InsufficientBatteryError(Exception):
    def __init__(self, name: str, required_battery: int, available_battery: int, message: str | None = None): # Optional message param to allow for custom messages
        self.name = name
        self.required_battery = required_battery
        self.available_battery = available_battery
        self.message = message or f"{self.name} requires {required_battery}% battery for this task, but only has {available_battery}% battery left."

        super().__init__(self.message)
