import unittest
from decimal import Decimal
from partname_resolver.units.resistance import Resistance


class ResistanceTestCase(unittest.TestCase):
    def test_resistance_conversion_str_to_decimal(self):
        self.assertEqual(Resistance("1MΩ").get_value(), Decimal('1') * Decimal('1E6'))
        self.assertEqual(Resistance("1kΩ").get_value(), Decimal('1') * Decimal('1E3'))
        self.assertEqual(Resistance("1Ω").get_value(), Decimal('1') * Decimal('1E0'))
        self.assertEqual(Resistance("1mΩ").get_value(), Decimal('1') * Decimal('1E-3'))

        self.assertEqual(Resistance("1M").get_value(), Decimal('1') * Decimal('1E6'))
        self.assertEqual(Resistance("1k").get_value(), Decimal('1') * Decimal('1E3'))
        self.assertEqual(Resistance("1R").get_value(), Decimal('1') * Decimal('1E0'))
        self.assertEqual(Resistance("1m").get_value(), Decimal('1') * Decimal('1E-3'))

        self.assertEqual(Resistance("1000MΩ").get_value(), Decimal('1000') * Decimal('1E6'))
        self.assertEqual(Resistance("1000kΩ").get_value(), Decimal('1000') * Decimal('1E3'))
        self.assertEqual(Resistance("1000Ω").get_value(), Decimal('1000') * Decimal('1E0'))
        self.assertEqual(Resistance("1000mΩ").get_value(), Decimal('1000') * Decimal('1E-3'))

        self.assertEqual(Resistance("1M5").get_value(), Decimal('1.5') * Decimal('1E6'))
        self.assertEqual(Resistance("1k5").get_value(), Decimal('1.5') * Decimal('1E3'))
        self.assertEqual(Resistance("1R5").get_value(), Decimal('1.5') * Decimal('1E0'))
        self.assertEqual(Resistance("1m5").get_value(), Decimal('1.5') * Decimal('1E-3'))

    def test_resistance_to_str_conversion(self):
        self.assertEqual(str(Resistance(Decimal('0'))), "0Ω")
        self.assertEqual(str(Resistance(Decimal('2.2E6'))), "2.2MΩ")
        self.assertEqual(str(Resistance(Decimal('4E3'))), "4kΩ")
        self.assertEqual(str(Resistance(Decimal('100'))), "100Ω")
        self.assertEqual(str(Resistance(Decimal('100E-3'))), "100mΩ")
        self.assertEqual(str(Resistance(Decimal('100E-6'))), "100uΩ")
        self.assertEqual(str(Resistance(Decimal('100E-9'))), "0.1uΩ")

    def test_equality(self):
        self.assertEqual(Resistance(Decimal('100')), Resistance(Decimal('100')))
        self.assertEqual(Resistance(Decimal('100')), '100Ω')
        self.assertEqual(Resistance(Decimal('100E3')), '100kΩ')


if __name__ == '__main__':
    unittest.main()
