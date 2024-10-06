import unittest
from conversions_refactored import convert, ConversionNotPossible

class TestRefactoredConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        self.assertAlmostEqual(convert('celsius', 'kelvin', 0.0), 273.15)
        self.assertAlmostEqual(convert('celsius', 'fahrenheit', 100.0), 212.0)
        self.assertAlmostEqual(convert('fahrenheit', 'celsius', 32.0), 0.0)

    def test_distance_conversions(self):
        self.assertAlmostEqual(convert('miles', 'yards', 1.0), 1760)
        self.assertAlmostEqual(convert('yards', 'meters', 1.0), 0.9144)

    def test_invalid_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            convert('celsius', 'miles', 100)

if __name__ == '__main__':
    unittest.main()
