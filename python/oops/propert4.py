#!/usr/bin/python3

"""Any code that retrieves the value of temperature will automatically call get_temperature() instead of a dictionary (__dict__) look-up. 
Similarly, any code that assigns a value to temperature will automatically call set_temperature(). This is one cool feature in Python."""

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

c=Celsius()
c.temperature=37
c.to_fahrenheit()
#print (c.to_fahrenheit())
