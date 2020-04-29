import unittest
from partname_resolver.capacitors import capacitors_partname_decoder
from partname_resolver.capacitors.capacitor import Capacitor
from partname_resolver.units.temperature import TemperatureRange


class TestMurataCapacitorPartnameResolver(unittest.TestCase):
    def test_GRT(self):
        part = capacitors_partname_decoder.resolve('GRT0335C1E120JA02')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="GRT0335C1E120JA02",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="GRT",
                              capacitance="12pF",
                              voltage="25V",
                              tolerance={'min': "-5%", 'max': '+5%'},
                              dielectric_type="C0G",
                              case="0201",
                              note="AEC-Q200 Compliant Chip Multilayer Ceramic Capacitors for Infotainment")
        self.assertEqual(component, part)

    def test_GCM(self):
        part = capacitors_partname_decoder.resolve('GCM155R71C104KA55D')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="GCM155R71C104KA55D",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="GCM",
                              capacitance="100nF",
                              voltage="16V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0402",
                              note="Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

        part = capacitors_partname_decoder.resolve('GCM21BR71E105KA56L')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="GCM21BR71E105KA56L",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="GCM",
                              capacitance="1uF",
                              voltage="25V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0805",
                              note="Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_GC3(self):
        part = capacitors_partname_decoder.resolve('GC331AD72W153KX01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="GC331AD72W153KX01",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="GC3",
                              capacitance="15nF",
                              voltage="450V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7T",
                              case="1206",
                              note="High Effective Capacitance & High Ripple Current Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_GCJ(self):
        part = capacitors_partname_decoder.resolve('GCJ188R92A152KA01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="GCJ188R92A152KA01",
                              working_temperature_range=TemperatureRange('-55', '150'),
                              series="GCJ",
                              capacitance="1.5nF",
                              voltage="100V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X8R",
                              case="0603",
                              note="Soft Termination Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_GCD(self):
        part = capacitors_partname_decoder.resolve('GCD188R71H153KA01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="GCD188R71H153KA01",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="GCD",
                              capacitance="15nF",
                              voltage="50V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0603",
                              note="MLSC Design Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_GCE(self):
        part = capacitors_partname_decoder.resolve('GCE188R71H682KA01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="GCE188R71H682KA01",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="GCE",
                              capacitance="6.8nF",
                              voltage="50V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0603",
                              note="Soft Termination MLSC Design Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_NFM(self):
        pass

    def test_KCM(self):
        part = capacitors_partname_decoder.resolve('KCM55LR71H106KH01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="KCM55LR71H106KH01",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="KCM",
                              capacitance="10uF",
                              voltage="50V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="2220",
                              note="Metal Terminal Type Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_KC3(self):
        part = capacitors_partname_decoder.resolve('KC355LD72J154KH01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="KC355LD72J154KH01",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="KC3",
                              capacitance="150nF",
                              voltage="630V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7T",
                              case="2220",
                              note="High Effective Capacitance & High Allowable Ripple Current Metal Terminal Type Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_KCA(self):
        part = capacitors_partname_decoder.resolve('KCA55L7UMF102KH01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="KCA55L7UMF102KH01",
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="KCA",
                              capacitance="1nF",
                              voltage="250VAC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="U2J",
                              case="2220",
                              note="Safety Standard Certified Metal Terminal Type Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_GCG(self):
        part = capacitors_partname_decoder.resolve('GCG1555G1H121JA01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata Manufacturing",
                              partnumber="GCG1555G1H121JA01",
                              working_temperature_range=TemperatureRange('-55', '150'),
                              series="GCG",
                              capacitance="120pF",
                              voltage="50V",
                              tolerance={'min': "-5%", 'max': '+5%'},
                              dielectric_type="X8G",
                              case="0402",
                              note="AgPd Termination Conductive Glue Mounting Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)
