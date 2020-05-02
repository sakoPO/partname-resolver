import unittest
from partname_resolver.inductors import inductors_partname_decoder
from partname_resolver.components.inductor import Inductor
from partname_resolver.units.temperature import TemperatureRange
from partname_resolver.units.capacitanceTolerance import Tolerance
from partname_resolver.case.chip import Chip
from partname_resolver.units.length import Dimmension, Length, LengthTolerance


class VishayDecoderTestCase(unittest.TestCase):
    def test_IHLP(self):
        part = inductors_partname_decoder.resolve('IHLP2525AEER1R0M01')
        self.assertIsNotNone(part)
        component = Inductor(inductor_type=Inductor.Type.WireWoundInductor,
                             manufacturer="Vishay",
                             partnumber="IHLP2525AEER1R0M01",
                             working_temperature_range=TemperatureRange('-55', '125'),
                             series="IHLP",
                             inductance='1uH',
                             tolerance=Tolerance('20%'),
                             q=None,
                             dc_resistance=None,
                             rated_current=None,
                             self_resonant_frequency=None,
                             max_working_voltage='40V',
                             case='2525',
                             note='Commercial / High Saturation')
        self.assertEqual(component, part)


if __name__ == '__main__':
    unittest.main()
