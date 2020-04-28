import unittest
from partname_resolver.capacitors import capacitors_partname_decoder
from partname_resolver.capacitors.capacitor import Capacitor
from partname_resolver.units.temperature import TemperatureRange


class TestFenghuaCapacitorPartnameResolver(unittest.TestCase):
    def test_0805(self):
        part = capacitors_partname_decoder.resolve('0805B472K500NT')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Fenghua Advanced Technology",
                              partnumber="0805B472K500NT",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series=None,
                              capacitance="4.7nF",
                              voltage="50V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0805",
                              note="Termination: Nickel Barrier Termination, Packing: Taping Package")
        self.assertEqual(component, part)


if __name__ == "__main__":
    unittest.main()
