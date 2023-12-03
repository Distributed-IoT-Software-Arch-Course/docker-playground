import random


class TemperatureSensor:

    def __init__(self):
        self.measure_temperature()

    # Another instance method with a parameter
    def measure_temperature(self):
        self.temperature_value = random.uniform(20.0, 40.0)
