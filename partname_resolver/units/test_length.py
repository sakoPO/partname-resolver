import unittest
from .length import Length, LengthTolerance, Dimmension


class LengthUnitTestCase(unittest.TestCase):
    def test_string_conversion(self):
        self.assertEqual('1mm', str(Length('1mm')))
        self.assertEqual('0.1mm', str(Length('0.1mm')))

    def test_length_tolerance_conversion(self):
        self.assertEqual("±0.1mm", str(LengthTolerance('0.1mm')))

    def test_dimmension(self):
        dim = Dimmension('1.6mm', LengthTolerance('0.1mm'))
        self.assertEqual("1.6±0.1mm", str(dim))


if __name__ == '__main__':
    unittest.main()
