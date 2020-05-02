import unittest
from partname_resolver.capacitors import capacitors_partname_decoder
from partname_resolver.components.capacitor import Capacitor
from partname_resolver.units.temperature import TemperatureRange


class TestJBCapacitorsPartnameResolver(unittest.TestCase):
    def test_JRG(self):
        part = capacitors_partname_decoder.resolve('JRG0J331M02500630115000B')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="JB Capacitors Company",
                              partnumber="JRG0J331M02500630115000B",
                              working_temperature_range=TemperatureRange('-40', '105'),
                              series="JRG",
                              capacitance="330uF",
                              voltage="6.3V",
                              tolerance={'min': "-20%", 'max': '+20%'},
                              dielectric_type="Aluminium oxide",
                              case='6.3x11.5mm',
                              note="Radial Aluminum Electrolytic Capacitor, Pitch=2.5, Lead length=Standard, Packing: Bulk")
        self.assertEqual(component, part)


if __name__ == "__main__":
    unittest.main()
