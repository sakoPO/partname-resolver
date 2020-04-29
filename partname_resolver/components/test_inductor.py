import unittest
from partname_resolver.components.inductor import Inductor
from partname_resolver.units.temperature import TemperatureRange


class InductorTestCase(unittest.TestCase):
    def test_equality(self):
        A = Inductor(inductor_type=Inductor.Type.MultilayerInductor,
                     manufacturer="Murata Manufacturing",
                     partnumber="LQG18HNR10J00D",
                     working_temperature_range=TemperatureRange('-55', '125'),
                     series="LQG",
                     inductance='100nH',
                     tolerance=None,
                     q='8',
                     dc_resistance=None,
                     rated_current=None,
                     self_resonant_frequency=None,
                     max_working_voltage=None,
                     case=None,
                     note=None)
        B = Inductor(inductor_type=Inductor.Type.MultilayerInductor,
                     manufacturer="Murata Manufacturing",
                     partnumber="LQG18HNR10J00D",
                     working_temperature_range=TemperatureRange('-55', '125'),
                     series="LQG",
                     inductance='100nH',
                     tolerance=None,
                     q='8',
                     dc_resistance=None,
                     rated_current=None,
                     self_resonant_frequency=None,
                     max_working_voltage=None,
                     case=None,
                     note=None)
        self.assertEqual(B, A)
