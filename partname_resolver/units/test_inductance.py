import unittest
from decimal import Decimal
from partname_resolver.units.inductance import Inductance


class ResistanceTestCase(unittest.TestCase):
    def test_resistance_conversion_str_to_decimal(self):
        self.assertEqual(Inductance("1MH").get_value(), Decimal('1') * Decimal('1E6'))
        self.assertEqual(Inductance("1kH").get_value(), Decimal('1') * Decimal('1E3'))
        self.assertEqual(Inductance("1H").get_value(), Decimal('1') * Decimal('1E0'))
        self.assertEqual(Inductance("1mH").get_value(), Decimal('1') * Decimal('1E-3'))

        self.assertEqual(Inductance("1M").get_value(), Decimal('1') * Decimal('1E6'))
        self.assertEqual(Inductance("1k").get_value(), Decimal('1') * Decimal('1E3'))
        self.assertEqual(Inductance("1H").get_value(), Decimal('1') * Decimal('1E0'))
        self.assertEqual(Inductance("1m").get_value(), Decimal('1') * Decimal('1E-3'))

        self.assertEqual(Inductance("1000MH").get_value(), Decimal('1000') * Decimal('1E6'))
        self.assertEqual(Inductance("1000kH").get_value(), Decimal('1000') * Decimal('1E3'))
        self.assertEqual(Inductance("1000H").get_value(), Decimal('1000') * Decimal('1E0'))
        self.assertEqual(Inductance("1000mH").get_value(), Decimal('1000') * Decimal('1E-3'))

        self.assertEqual(Inductance("1M5").get_value(), Decimal('1.5') * Decimal('1E6'))
        self.assertEqual(Inductance("1k5").get_value(), Decimal('1.5') * Decimal('1E3'))
        self.assertEqual(Inductance("1H5").get_value(), Decimal('1.5') * Decimal('1E0'))
        self.assertEqual(Inductance("1m5").get_value(), Decimal('1.5') * Decimal('1E-3'))

    def test_resistance_to_str_conversion(self):
        self.assertEqual("0H", str(Inductance(Decimal('0'))))
        self.assertEqual("2.2MH", str(Inductance(Decimal('2.2E6'))))
        self.assertEqual("4kH", str(Inductance(Decimal('4E3'))))
        self.assertEqual("100H", str(Inductance(Decimal('100'))))
        self.assertEqual("100mH", str(Inductance(Decimal('100E-3'))), "100mH")
        self.assertEqual("100uH", str(Inductance(Decimal('100E-6'))))
        self.assertEqual("100nH", str(Inductance(Decimal('100E-9'))))

    def test_equality(self):
        self.assertEqual(Inductance(Decimal('100')), Inductance(Decimal('100')))
        self.assertEqual(Inductance(Decimal('100')), '100H')
        self.assertEqual(Inductance(Decimal('100E3')), '100kH')


if __name__ == '__main__':
    unittest.main()
