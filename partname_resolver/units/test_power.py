import unittest
from partname_resolver.units.power import Power
from decimal import Decimal


class PowerTestCase(unittest.TestCase):
    def test_Power_conversion_str_to_decimal(self):
        self.assertEqual(Power("1MW").get_value(), Decimal('1') * Decimal('1E6'))
        self.assertEqual(Power("1kW").get_value(), Decimal('1') * Decimal('1E3'))
        self.assertEqual(Power("1W").get_value(), Decimal('1') * Decimal('1E0'))
        self.assertEqual(Power("1mW").get_value(), Decimal('1') * Decimal('1E-3'))

        self.assertEqual(Power("1M").get_value(), Decimal('1') * Decimal('1E6'))
        self.assertEqual(Power("1k").get_value(), Decimal('1') * Decimal('1E3'))
        self.assertEqual(Power("1W").get_value(), Decimal('1') * Decimal('1E0'))
        self.assertEqual(Power("1m").get_value(), Decimal('1') * Decimal('1E-3'))

        self.assertEqual(Power("1000MW").get_value(), Decimal('1000') * Decimal('1E6'))
        self.assertEqual(Power("1000kW").get_value(), Decimal('1000') * Decimal('1E3'))
        self.assertEqual(Power("1000W").get_value(), Decimal('1000') * Decimal('1E0'))
        self.assertEqual(Power("1000mW").get_value(), Decimal('1000') * Decimal('1E-3'))

        self.assertEqual(Power("1M5").get_value(), Decimal('1.5') * Decimal('1E6'))
        self.assertEqual(Power("1k5").get_value(), Decimal('1.5') * Decimal('1E3'))
        self.assertEqual(Power("1W5").get_value(), Decimal('1.5') * Decimal('1E0'))
        self.assertEqual(Power("1m5").get_value(), Decimal('1.5') * Decimal('1E-3'))

    def test_Power_to_str_conversion(self):
        self.assertEqual("2.2MW", str(Power(Decimal('2.2E6'))))
        self.assertEqual("4kW", str(Power(Decimal('4E3'))))
        self.assertEqual("100W", str(Power(Decimal('100'))))
        self.assertEqual("100mW", str(Power(Decimal('100E-3'))))
        self.assertEqual("100uW", str(Power(Decimal('100E-6'))))
        self.assertEqual("0.1uW", str(Power(Decimal('100E-9'))))

    def test_equality(self):
        self.assertEqual(Power(Decimal('100')), Power(Decimal('100')))
        self.assertEqual(Power(Decimal('100')), '100W')
        self.assertEqual(Power(Decimal('100E3')), '100kW')


if __name__ == '__main__':
    unittest.main()
