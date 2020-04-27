import unittest
from partname_resolver.units.capacitanceTolerance import Tolerance


class CapacitanceToleranceTestCase(unittest.TestCase):
    def test_tolerance(self):
        self.assertEqual(str(Tolerance('10%')), "\u00B110%")
        self.assertEqual(str(Tolerance('-10%', '+10%')), "\u00B110%")
        self.assertEqual(str(Tolerance('-10%', '+20%')), "-10%...+20%")

        self.assertEqual(str(Tolerance('1pF')), "\u00B11pF")
        self.assertEqual(str(Tolerance('-1pF', '+1pF')), "\u00B11pF")
        self.assertEqual(str(Tolerance('-1pF', '+2pF')), "-1pF...+2pF")

        with self.assertRaises(ValueError):
            Tolerance('-20%')

    def test_equality_operator(self):
        self.assertEqual(Tolerance('-20%', '20%'), Tolerance('20%'))


if __name__ == '__main__':
    unittest.main()
