import unittest
from conversions import *

class TestTemperatureConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        test_cases = [
            (0.0, 273.15),
            (100.0, 373.15),
            (-273.15, 0.0),
            (25.0, 298.15),
            (300.0, 573.15)
        ]
        for celsius, expected in test_cases:
            result = convertCelsiusToKelvin(celsius)
            print(f"Testing {celsius} °C -> {expected} K, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        test_cases = [
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (25.0, 77.0),
            (300.0, 572.0)
        ]
        for celsius, expected in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            print(f"Testing {celsius} °C -> {expected} °F, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertFahrenheitToCelsius(self):
        test_cases = [
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (77.0, 25.0),
            (572.0, 300.0)
        ]
        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            print(f"Testing {fahrenheit} °F -> {expected} °C, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertFahrenheitToKelvin(self):
        test_cases = [
            (32.0, 273.15),
            (212.0, 373.15),
            (-40.0, 233.15),
            (77.0, 298.15),
            (572.0, 573.15)
        ]
        for fahrenheit, expected in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            print(f"Testing {fahrenheit} °F -> {expected} K, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertKelvinToCelsius(self):
        test_cases = [
            (273.15, 0.0),
            (373.15, 100.0),
            (0.0, -273.15),
            (298.15, 25.0),
            (573.15, 300.0)
        ]
        for kelvin, expected in test_cases:
            result = convertKelvinToCelsius(kelvin)
            print(f"Testing {kelvin} K -> {expected} °C, got {result}")
            self.assertAlmostEqual(result, expected, places=2)

    def test_convertKelvinToFahrenheit(self):
        test_cases = [
            (273.15, 32.0),
            (373.15, 212.0),
            (233.15, -40.0),
            (298.15, 77.0),
            (573.15, 572.0)
        ]
        for kelvin, expected in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            print(f"Testing {kelvin} K -> {expected} °F, got {result}")
            self.assertAlmostEqual(result, expected, places=2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
