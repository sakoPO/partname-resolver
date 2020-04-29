import unittest
from partname_resolver.units.capacitance import Capacitance, CapacitanceRange
from decimal import Decimal


class CapacitanceTestCase(unittest.TestCase):
    def test_capacitance_conversion_str_to_decimal(self):
        self.assertEqual(Capacitance("1pF").get_value(), Decimal('1') * Decimal('1E-12'))
        self.assertEqual(Capacitance("1nF").get_value(), Decimal('1') * Decimal('1E-9'))
        self.assertEqual(Capacitance("1uF").get_value(), Decimal('1') * Decimal('1E-6'))
        self.assertEqual(Capacitance("1mF").get_value(), Decimal('1') * Decimal('1E-3'))
        self.assertEqual(Capacitance("1F").get_value(), Decimal('1') * Decimal('1E-0'))

        self.assertEqual(Capacitance("1p").get_value(), Decimal('1') * Decimal('1E-12'))
        self.assertEqual(Capacitance("1n").get_value(), Decimal('1') * Decimal('1E-9'))
        self.assertEqual(Capacitance("1u").get_value(), Decimal('1') * Decimal('1E-6'))
        self.assertEqual(Capacitance("1m").get_value(), Decimal('1') * Decimal('1E-3'))
        self.assertEqual(Capacitance("1").get_value(), Decimal('1') * Decimal('1E-0'))

        self.assertEqual(Capacitance("1000pF").get_value(), Decimal('1000') * Decimal('1E-12'))
        self.assertEqual(Capacitance("1000nF").get_value(), Decimal('1000') * Decimal('1E-9'))
        self.assertEqual(Capacitance("1000uF").get_value(), Decimal('1000') * Decimal('1E-6'))
        self.assertEqual(Capacitance("1000mF").get_value(), Decimal('1000') * Decimal('1E-3'))
        self.assertEqual(Capacitance("1000F").get_value(), Decimal('1000') * Decimal('1E-0'))

        self.assertEqual(Capacitance("1p5").get_value(), Decimal('1.5') * Decimal('1E-12'))
        self.assertEqual(Capacitance("1n5").get_value(), Decimal('1.5') * Decimal('1E-9'))
        self.assertEqual(Capacitance("1u5").get_value(), Decimal('1.5') * Decimal('1E-6'))
        self.assertEqual(Capacitance("1m5").get_value(), Decimal('1.5') * Decimal('1E-3'))
        self.assertEqual(Capacitance("1F5").get_value(), Decimal('1.5') * Decimal('1E-0'))

        self.assertEqual(Capacitance("1.5p").get_value(), Decimal('1.5') * Decimal('1E-12'))
        self.assertEqual(Capacitance("1.5n").get_value(), Decimal('1.5') * Decimal('1E-9'))
        self.assertEqual(Capacitance("1.5u").get_value(), Decimal('1.5') * Decimal('1E-6'))
        self.assertEqual(Capacitance("1.5m").get_value(), Decimal('1.5') * Decimal('1E-3'))
        self.assertEqual(Capacitance("1.5F").get_value(), Decimal('1.5') * Decimal('1E-0'))

        self.assertEqual(Capacitance("1.5pF").get_value(), Decimal('1.5') * Decimal('1E-12'))
        self.assertEqual(Capacitance("1.5nF").get_value(), Decimal('1.5') * Decimal('1E-9'))
        self.assertEqual(Capacitance("1.5uF").get_value(), Decimal('1.5') * Decimal('1E-6'))
        self.assertEqual(Capacitance("1.5mF").get_value(), Decimal('1.5') * Decimal('1E-3'))

    def test_capacitance_to_str_conversion(self):
        self.assertEqual(str(Capacitance(Decimal('100'))), "100F")
        self.assertEqual(str(Capacitance(Decimal('100E-3'))), "100mF")
        self.assertEqual(str(Capacitance(Decimal('100E-6'))), "100uF")
        self.assertEqual(str(Capacitance(Decimal('100E-9'))), "100nF")
        self.assertEqual(str(Capacitance(Decimal('100E-12'))), "100pF")
        self.assertEqual(str(Capacitance(Decimal('100E-15'))), "100fF")

    def test_equality(self):
        self.assertEqual(Capacitance(Decimal('100')), Capacitance(Decimal('100')))
        self.assertEqual(Capacitance(Decimal('100')), '100F')
        self.assertEqual(Capacitance(Decimal('100E-9')), '100nF')

    def test_capacitance_range(self):
        self.assertEqual("1pF...1nF", str(CapacitanceRange(Capacitance("1pF"), Capacitance("1nF"))))
        self.assertEqual("1pF...1nF", str(CapacitanceRange("1pF", "1nF")))

    def test_capacitance_range_equality(self):
        self.assertEqual(CapacitanceRange("1pF", "1nF"), CapacitanceRange("1pF", "1nF"))


if __name__ == '__main__':
    unittest.main()
