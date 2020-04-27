import unittest
from .tolerance import Tolerance


class ResistanceToleranceTestCase(unittest.TestCase):
    def test_tolerance(self):
        self.assertEqual("\u00B110%", str(Tolerance('10%')))
        self.assertEqual("\u00B110%", str(Tolerance('-10%', '+10%')))
        self.assertEqual("-10%...+20%", str(Tolerance('-10%', '+20%')))

        self.assertEqual("\u00B11mΩ", str(Tolerance('1mR')))
        self.assertEqual("\u00B11kΩ", str(Tolerance('-1k', '+1k')))
        self.assertEqual("-1kΩ...+2kΩ", str(Tolerance('-1k', '+2k')))

        with self.assertRaises(ValueError):
            Tolerance('-20%')

    def test_equality_operator(self):
        self.assertEqual(Tolerance('-20%', '20%'), Tolerance('20%'))


if __name__ == '__main__':
    unittest.main()
