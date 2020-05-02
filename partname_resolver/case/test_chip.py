import unittest
from partname_resolver.case.chip import Chip
from partname_resolver.units.length import Dimmension, Length, LengthTolerance


class ChipTestCase(unittest.TestCase):
    def test_chip_name(self):
        self.assertEqual("EIA 0402, H=0.35", str(Chip('0402', L=1, W=0.5, T=0.35, t1=0.25, t2=0.2)))
        self.assertEqual("EIA 0402", str(Chip('0402')))
        self.assertEqual("EIA 0402, IEC/EN 1005, L=1mm, W=0.5mm, T=1±0.1mm", Chip('0402', T=Dimmension('1mm', LengthTolerance('0.1mm'))).get_full_str())

    def test_custom_dimmensions(self):
        tolerance = LengthTolerance('0.1mm')
        chip = Chip('0603', L=Dimmension('1.6mm', tolerance), W=Dimmension('0.8mm', tolerance),
                    T=Dimmension('0.45mm', tolerance), t1=Dimmension('0.3mm', LengthTolerance('0.2mm')),
                    t2=Dimmension('0.3mm', LengthTolerance('0.2mm')))
        self.assertEqual("EIA 0603, IEC/EN 1608, L=1.6±0.1mm, W=0.8±0.1mm, T=0.45±0.1mm, t1=0.3±0.2mm, t2=0.3±0.2mm", chip.get_full_str())



if __name__ == '__main__':
    unittest.main()
