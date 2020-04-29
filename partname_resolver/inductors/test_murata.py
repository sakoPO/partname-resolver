import unittest
from partname_resolver.inductors import inductors_partname_decoder
from partname_resolver.components.inductor import Inductor
from partname_resolver.units.temperature import TemperatureRange
from partname_resolver.units.capacitanceTolerance import Tolerance
from partname_resolver.case.chip import Chip
from partname_resolver.units.length import Dimmension, Length, LengthTolerance

class TestMurataInductorPartnameResolver(unittest.TestCase):
    def test_LQG(self):
        part = inductors_partname_decoder.resolve('LQG18HNR10J00D')
        self.assertIsNotNone(part)
        component = Inductor(inductor_type=Inductor.Type.MultilayerInductor,
                             manufacturer="Murata Manufacturing",
                             partnumber="LQG18HNR10J00D",
                             working_temperature_range=TemperatureRange('-55', '125'),
                             series="LQG",
                             inductance='100nH',
                             tolerance=Tolerance('5%'),
                             q='8',
                             dc_resistance=None,
                             rated_current=None,
                             self_resonant_frequency=None,
                             max_working_voltage=None,
                             case=Chip('0603', T=Dimmension('0.8mm', LengthTolerance('0.15mm'))),
                             note=None)
        self.assertEqual(component, part)
