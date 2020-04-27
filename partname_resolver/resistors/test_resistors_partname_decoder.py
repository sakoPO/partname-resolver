import unittest
from partname_resolver.resistors.tolerance import Tolerance
from partname_resolver.resistors import resistors_partname_decoder
from partname_resolver.resistors.resistor import Resistor
from partname_resolver.resistors.resistance import Resistance
from partname_resolver.resistors.power import Power


class ResistorsPartnameResolverTestCase(unittest.TestCase):
    def test_royal_ohm(self):
        decoded = resistors_partname_decoder.resolve("1206S4J0100T5E")
        self.assertEqual(Resistor.Type.ThickFilmResistor, decoded.type)
        self.assertEqual('Royal Ohm', decoded.manufacturer)
        self.assertEqual('1206S4J0100T5E', decoded.partnumber)
        self.assertEqual('', decoded.series)
        self.assertEqual(Resistance('10'), decoded.resistance)
        self.assertEqual(Tolerance('5%'), decoded.tolerance)
        self.assertEqual(Power('0.25'), decoded.power)
        self.assertEqual('200V', decoded.max_working_voltage)
        self.assertEqual('1206', decoded.case)
        self.assertEqual('Lead (Pb) Free Plating Type/ RoHS compliant', decoded.note)

        decoded = resistors_partname_decoder.resolve("4D02WGJ0240T")
        self.assertEqual(Resistor.Type.ThickFilmResistorArray, decoded.type)
        self.assertEqual('Royal Ohm', decoded.manufacturer)
        self.assertEqual('4D02WGJ0240T', decoded.partnumber)
        self.assertEqual('', decoded.series)
        self.assertEqual(Resistance('24'), decoded.resistance)
        self.assertEqual(Tolerance('5%'), decoded.tolerance)
        self.assertEqual(Power('0.0625'), decoded.power)
        self.assertEqual('50V', decoded.max_working_voltage)
        self.assertEqual('4D02', decoded.case)
        self.assertEqual('', decoded.note)

    def test_yaego(self):
        decoded = resistors_partname_decoder.resolve("RC0402FR-07100RL")
        self.assertEqual(Resistor.Type.ThickFilmResistor, decoded.type)
        self.assertEqual('Yaego', decoded.manufacturer)
        self.assertEqual('RC0402FR-07100RL', decoded.partnumber)
        self.assertEqual('RC', decoded.series)
        self.assertEqual(Resistance('100'), decoded.resistance)
        self.assertEqual(Tolerance('1%'), decoded.tolerance)
        self.assertEqual(Power('0.0625'), decoded.power)
        self.assertEqual('50V', decoded.max_working_voltage)
        self.assertEqual('0402', decoded.case)
        self.assertEqual('General purpose chip resistors', decoded.note)

    def test_vishay(self):
        decoded = resistors_partname_decoder.resolve("CRCW0805562RFKTA")
        self.assertEqual(Resistor.Type.ThickFilmResistor, decoded.type)
        self.assertEqual('Vishay', decoded.manufacturer)
        self.assertEqual('CRCW0805562RFKTA', decoded.partnumber)
        self.assertEqual('CRCW', decoded.series)
        self.assertEqual(Resistance('562'), decoded.resistance)
        self.assertEqual(Tolerance('1%'), decoded.tolerance)
        self.assertEqual(Power('0.125'), decoded.power)
        self.assertEqual('150V', decoded.max_working_voltage)
        self.assertEqual('0805', decoded.case)
        self.assertEqual('Lead (Pb)-Bearing Thick Film, Rectangular Chip Resistors', decoded.note)

    def test_bourns(self):
        decoded = resistors_partname_decoder.resolve("CAT16-220J4LF")
        self.assertEqual(Resistor.Type.ThickFilmResistorArray, decoded.type)
        self.assertEqual('Bourns', decoded.manufacturer)
        self.assertEqual('CAT16-220J4LF', decoded.partnumber)
        self.assertEqual('CAT16', decoded.series)
        self.assertEqual(Resistance('22'), decoded.resistance)
        self.assertEqual(Tolerance('5%'), decoded.tolerance)
        self.assertEqual(Power('0.25'), decoded.power)
        self.assertEqual('50V', decoded.max_working_voltage)
        self.assertEqual('1206', decoded.case)
        self.assertEqual('Concave Terminations', decoded.note)


if __name__ == '__main__':
    unittest.main()
