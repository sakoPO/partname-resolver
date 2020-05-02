import unittest
from partname_resolver.inductors import inductors_partname_decoder
from partname_resolver.components.inductor import Inductor
from partname_resolver.units.temperature import TemperatureRange
from partname_resolver.units.capacitanceTolerance import Tolerance
from partname_resolver.case.chip import Chip
from partname_resolver.units.length import Dimmension, Length, LengthTolerance


class TaiyoYudenDecoderTestCase(unittest.TestCase):
    def test_NR(self):
        part = inductors_partname_decoder.resolve('NR6028T220M')
        self.assertIsNotNone(part)
        component = Inductor(inductor_type=Inductor.Type.WireWoundInductor,
                             manufacturer="Taiyo Yuden",
                             partnumber="NR6028T220M",
                             working_temperature_range=TemperatureRange('-25', '120'),
                             series="NR",
                             inductance='22uH',
                             tolerance=Tolerance('20%'),
                             q=None,
                             dc_resistance=None,
                             rated_current=None,
                             self_resonant_frequency=None,
                             max_working_voltage=None,
                             case='6028',
                             note='SMD Power Inductors')
        self.assertEqual(component, part)


if __name__ == '__main__':
    unittest.main()
