import unittest
from decimal import Decimal
from .temperature import Temperature, TemperatureRange


class TemperatureTestCase(unittest.TestCase):
    def test_temperature_to_string_conversion(self):
        self.assertEqual("100℃", str(Temperature(Decimal(100))))
        self.assertEqual("-100℃", str(Temperature(Decimal(-100))))

    def test_temperature_eq_operator(self):
        self.assertEqual(Temperature(Decimal(100)), Temperature(Decimal(100)))

    def test_temperature_range_to_string_conversion(self):
        self.assertEqual("-100℃...200℃", str(TemperatureRange(Decimal(-100), Decimal(200))))
        self.assertEqual("10℃...200℃", str(TemperatureRange(Decimal(10), Decimal(200))))

        self.assertEqual("0℃...200℃", str(TemperatureRange(Temperature(Decimal(0)), Decimal(200))))




if __name__ == '__main__':
    unittest.main()
