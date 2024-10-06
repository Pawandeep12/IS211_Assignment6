import unittest
from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)

class TestConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        print("\nTesting Celsius to Kelvin conversions...")
        test_cases = [
            (0.0, 273.15),
            (100.0, 373.15),
            (-273.15, 0.0),
            (25.0, 298.15),
            (300.0, 573.15)
        ]
        for celsius, expected_kelvin in test_cases:
            result = convertCelsiusToKelvin(celsius)
            print(f"{celsius}°C to Kelvin: {result} K (expected {expected_kelvin} K)")
            self.assertAlmostEqual(result, expected_kelvin, places=2)

    def test_convertCelsiusToFahrenheit(self):
        print("\nTesting Celsius to Fahrenheit conversions...")
        test_cases = [
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (25.0, 77.0),
            (300.0, 572.0)
        ]
        for celsius, expected_fahrenheit in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            print(f"{celsius}°C to Fahrenheit: {result} °F (expected {expected_fahrenheit} °F)")
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)

    def test_convertFahrenheitToCelsius(self):
        print("\nTesting Fahrenheit to Celsius conversions...")
        test_cases = [
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (77.0, 25.0),
            (572.0, 300.0)
        ]
        for fahrenheit, expected_celsius in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            print(f"{fahrenheit}°F to Celsius: {result} °C (expected {expected_celsius} °C)")
            self.assertAlmostEqual(result, expected_celsius, places=2)

    def test_convertFahrenheitToKelvin(self):
        print("\nTesting Fahrenheit to Kelvin conversions...")
        test_cases = [
            (32.0, 273.15),
            (212.0, 373.15),
            (-40.0, 233.15),
            (77.0, 298.15),
            (572.0, 573.15)
        ]
        for fahrenheit, expected_kelvin in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            print(f"{fahrenheit}°F to Kelvin: {result} K (expected {expected_kelvin} K)")
            self.assertAlmostEqual(result, expected_kelvin, places=2)

    def test_convertKelvinToCelsius(self):
        print("\nTesting Kelvin to Celsius conversions...")
        test_cases = [
            (273.15, 0.0),
            (373.15, 100.0),
            (0.0, -273.15),
            (298.15, 25.0),
            (573.15, 300.0)
        ]
        for kelvin, expected_celsius in test_cases:
            result = convertKelvinToCelsius(kelvin)
            print(f"{kelvin} K to Celsius: {result} °C (expected {expected_celsius} °C)")
            self.assertAlmostEqual(result, expected_celsius, places=2)

    def test_convertKelvinToFahrenheit(self):
        print("\nTesting Kelvin to Fahrenheit conversions...")
        test_cases = [
            (273.15, 32.0),
            (373.15, 212.0),
            (0.0, -459.67),
            (298.15, 77.0),
            (573.15, 572.0)
        ]
        for kelvin, expected_fahrenheit in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            print(f"{kelvin} K to Fahrenheit: {result} °F (expected {expected_fahrenheit} °F)")
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)


if __name__ == '__main__':
    unittest.main()

