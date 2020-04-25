import unittest
from partname_resolver.capacitors import capacitors_partname_decoder
from partname_resolver.capacitors.capacitor import Capacitor


class TestCapacitorPartnameResolver(unittest.TestCase):
    def test_murata_GRT(self):
        part = capacitors_partname_decoder.resolve('GRT0335C1E120JA02')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="GRT0335C1E120JA02",
                              series="GRT",
                              capacitance="12pF",
                              voltage="25VDC",
                              tolerance={'min': "-5%", 'max': '+5%'},
                              dielectric_type="C0G",
                              case="0201",
                              note="AEC-Q200 Compliant Chip Multilayer Ceramic Capacitors for Infotainment")
        self.assertEqual(component, part)

    def test_murata_GCM(self):
        part = capacitors_partname_decoder.resolve('GCM155R71C104KA55D')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="GCM155R71C104KA55D",
                              series="GCM",
                              capacitance="100nF",
                              voltage="16VDC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0402",
                              note="Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

        part = capacitors_partname_decoder.resolve('GCM21BR71E105KA56L')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="GCM21BR71E105KA56L",
                              series="GCM",
                              capacitance="1uF",
                              voltage="25VDC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0805",
                              note="Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_murata_GC3(self):
        part = capacitors_partname_decoder.resolve('GC331AD72W153KX01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="GC331AD72W153KX01",
                              series="GC3",
                              capacitance="15nF",
                              voltage="450VDC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7T",
                              case="1206",
                              note="High Effective Capacitance & High Ripple Current Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_murata_GCJ(self):
        part = capacitors_partname_decoder.resolve('GCJ188R92A152KA01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="GCJ188R92A152KA01",
                              series="GCJ",
                              capacitance="1.5nF",
                              voltage="100VDC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X8R",
                              case="0603",
                              note="Soft Termination Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_murata_GCD(self):
        part = capacitors_partname_decoder.resolve('GCD188R71H153KA01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="GCD188R71H153KA01",
                              series="GCD",
                              capacitance="15nF",
                              voltage="50VDC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0603",
                              note="MLSC Design Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_murata_GCE(self):
        part = capacitors_partname_decoder.resolve('GCE188R71H682KA01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="GCE188R71H682KA01",
                              series="GCE",
                              capacitance="6.8nF",
                              voltage="50VDC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0603",
                              note="Soft Termination MLSC Design Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_murata_NFM(self):
        pass

    def test_murata_KCM(self):
        part = capacitors_partname_decoder.resolve('KCM55LR71H106KH01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="KCM55LR71H106KH01",
                              series="KCM",
                              capacitance="10uF",
                              voltage="50VDC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="2220",
                              note="Metal Terminal Type Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_murata_KC3(self):
        part = capacitors_partname_decoder.resolve('KC355LD72J154KH01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="KC355LD72J154KH01",
                              series="KC3",
                              capacitance="150nF",
                              voltage="630VDC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7T",
                              case="2220",
                              note="High Effective Capacitance & High Allowable Ripple Current Metal Terminal Type Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_murata_KCA(self):
        part = capacitors_partname_decoder.resolve('KCA55L7UMF102KH01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="KCA55L7UMF102KH01",
                              series="KCA",
                              capacitance="1nF",
                              voltage="250VAC",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="U2J",
                              case="2220",
                              note="Safety Standard Certified Metal Terminal Type Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_murata_GCG(self):
        part = capacitors_partname_decoder.resolve('GCG1555G1H121JA01')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Murata",
                              partnumber="GCG1555G1H121JA01",
                              series="GCG",
                              capacitance="120pF",
                              voltage="50VDC",
                              tolerance={'min': "-5%", 'max': '+5%'},
                              dielectric_type="X8G",
                              case="0402",
                              note="AgPd Termination Conductive Glue Mounting Chip Multilayer Ceramic Capacitors for Automotive")
        self.assertEqual(component, part)

    def test_samsung_CL(self):
        part = capacitors_partname_decoder.resolve('CL05B222KB5NNNC')
        component = Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                              manufacturer="Samsung",
                              partnumber="CL05B222KB5NNNC",
                              series="CL",
                              capacitance="2.2nF",
                              voltage="50V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0402",
                              note="Normal")
        self.assertEqual(component, part)

    def test_vishay_VJ(self):
        part = capacitors_partname_decoder.resolve('VJ0603D820JXCAJ')
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Vishay",
                              partnumber="VJ0603D820JXCAJ",
                              series="VJ",
                              capacitance="82pF",
                              voltage="200V",
                              tolerance={'min': "-5%", 'max': '+5%'},
                              dielectric_type="C0G",
                              case="0603",
                              note="Ni barrier100 % tin platematte finish")
        self.assertEqual(component, part)

    def test_nichicon(self):
        part = capacitors_partname_decoder.resolve("UKA1H220MDD")
        component = Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                              manufacturer="Nichicon",
                              partnumber="UKA1H220MDD",
                              series="KA",
                              capacitance="22uF",
                              voltage="50VDC",
                              tolerance={'min': "-20%", 'max': '+20%'},
                              dielectric_type="Aluminium oxide",
                              case="5",
                              note="For High Grade Audio Equipment, Wide Temperature Range")
        self.assertEqual(component, part)

    def test_avx(self):
        part = capacitors_partname_decoder.resolve("04023C104KAT2A")
        component = Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                              manufacturer="AVX",
                              partnumber="04023C104KAT2A",
                              series="",
                              capacitance="100nF",
                              voltage="25V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0402",
                              note="Standard product")
        self.assertEqual(component, part)

    def test_samwha(self):
        part = capacitors_partname_decoder.resolve("CA1E337M10010VR")
        component = Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                              manufacturer="Samwha",
                              partnumber="CA1E337M10010VR",
                              series="CA",
                              capacitance="330uF",
                              voltage="25VDC",
                              tolerance={'min': "-20%", 'max': '+20%'},
                              dielectric_type="Aluminium oxide",
                              case="10mm",
                              note="Chip type, Long Life Series")
        self.assertEqual(component, part)

        part = capacitors_partname_decoder.resolve("SD1J475M05011BB")
        component = Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                              manufacturer="Samwha",
                              partnumber="SD1J475M05011BB",
                              series="SD",
                              capacitance="4.7uF",
                              voltage="63VDC",
                              tolerance={'min': "-20%", 'max': '+20%'},
                              dielectric_type="Aluminium oxide",
                              case="5mm",
                              note="Standard, For General Purposes Series")
        self.assertEqual(component, part)

    def test_taiyo_yuden(self):
        part = capacitors_partname_decoder.resolve("EMK212B7475KG-T")
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Taiyo Yuden",
                              partnumber="EMK212B7475KG-T",
                              series="M",
                              capacitance="4.7uF",
                              voltage="16V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="0805",
                              note="Multilayer ceramic capacitor")
        self.assertEqual(component, part)

        part = capacitors_partname_decoder.resolve("HMK325B7225KM-T")
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Taiyo Yuden",
                              partnumber="HMK325B7225KM-T",
                              series="M",
                              capacitance="2.2uF",
                              voltage="100V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="1210",
                              note="Multilayer ceramic capacitor")
        self.assertEqual(component, part)


if __name__ == "__main__":
    unittest.main()
