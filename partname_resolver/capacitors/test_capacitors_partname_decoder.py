import unittest
from partname_resolver.capacitors import capacitors_partname_decoder
from partname_resolver.components.capacitor import Capacitor
from partname_resolver.units.temperature import TemperatureRange


class TestCapacitorPartnameResolver(unittest.TestCase):
    def test_samsung_CL(self):
        part = capacitors_partname_decoder.resolve('CL05B222KB5NNNC')
        component = Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                              manufacturer="Samsung",
                              partnumber="CL05B222KB5NNNC",
                              working_temperature_range=TemperatureRange('-55', '125'),
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
                              working_temperature_range=TemperatureRange('-55', '125'),
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
                              working_temperature_range=TemperatureRange('-55', '105'),
                              series="KA",
                              capacitance="22uF",
                              voltage="50V",
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
                              working_temperature_range=TemperatureRange('-55', '125'),
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
                              working_temperature_range=TemperatureRange('-55', '105'),
                              series="CA",
                              capacitance="330uF",
                              voltage="25V",
                              tolerance={'min': "-20%", 'max': '+20%'},
                              dielectric_type="Aluminium oxide",
                              case="10mm",
                              note="Chip type, Long Life Series")
        self.assertEqual(component, part)

        part = capacitors_partname_decoder.resolve("SD1J475M05011BB")
        component = Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                              manufacturer="Samwha",
                              partnumber="SD1J475M05011BB",
                              working_temperature_range=TemperatureRange('-40', '85'),
                              series="SD",
                              capacitance="4.7uF",
                              voltage="63V",
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
                              working_temperature_range=TemperatureRange('-55', '125'),
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
                              working_temperature_range=TemperatureRange('-55', '125'),
                              series="M",
                              capacitance="2.2uF",
                              voltage="100V",
                              tolerance={'min': "-10%", 'max': '+10%'},
                              dielectric_type="X7R",
                              case="1210",
                              note="Multilayer ceramic capacitor")
        self.assertEqual(component, part)

    def test_aishi(self):
        part = capacitors_partname_decoder.resolve("EWH1EM221F11OT")
        self.assertIsNotNone(part)
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Aishi",
                              partnumber="EWH1EM221F11OT",
                              working_temperature_range=TemperatureRange('-40', '105'),
                              series="WH",
                              capacitance="220uF",
                              voltage="25V",
                              tolerance={'min': "-20%", 'max': '+20%'},
                              dielectric_type="Aluminium oxide",
                              case="8x11",
                              note="Miniature aluminium electrolytic capacitors")
        self.assertEqual(component, part)

        part = capacitors_partname_decoder.resolve("EWH1KM2R2D11OT")
        self.assertIsNotNone(part)
        component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                              manufacturer="Aishi",
                              partnumber="EWH1KM2R2D11OT",
                              working_temperature_range=TemperatureRange('-40', '105'),
                              series="WH",
                              capacitance="2.2uF",
                              voltage="100V",
                              tolerance={'min': "-20%", 'max': '+20%'},
                              dielectric_type="Aluminium oxide",
                              case="5x11",
                              note="Miniature aluminium electrolytic capacitors")
        self.assertEqual(component, part)

    def test_jamicon(self):
        # ---------------- TK -----------------
        with self.subTest("TKP102M1EG20M"):
            part = capacitors_partname_decoder.resolve("TKP102M1EG20M")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Jamicon",
                                  partnumber="TKP102M1EG20M",
                                  working_temperature_range=TemperatureRange('-55', '105'),
                                  series="TK",
                                  capacitance="1000uF",
                                  voltage="25V",
                                  tolerance={'min': "-20%", 'max': '+20%'},
                                  dielectric_type="Aluminium oxide",
                                  case="8x20",
                                  note="Wide temperature range")
            self.assertEqual(component, part)
        with self.subTest("TKR221M1EFBBM"):
            part = capacitors_partname_decoder.resolve("TKR221M1EFBBM")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Jamicon",
                                  partnumber="TKR221M1EFBBM",
                                  working_temperature_range=TemperatureRange('-55', '105'),
                                  series="TK",
                                  capacitance="220uF",
                                  voltage="25V",
                                  tolerance={'min': "-20%", 'max': '+20%'},
                                  dielectric_type="Aluminium oxide",
                                  case="7.3x11.5",
                                  note="Wide temperature range")
            self.assertEqual(component, part)
        with self.subTest("TKR100M2AE11M"):
            part = capacitors_partname_decoder.resolve("TKR100M2AE11M")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Jamicon",
                                  partnumber="TKR100M2AE11M",
                                  working_temperature_range=TemperatureRange('-55', '105'),
                                  series="TK",
                                  capacitance="10uF",
                                  voltage="100V",
                                  tolerance={'min': "-20%", 'max': '+20%'},
                                  dielectric_type="Aluminium oxide",
                                  case="6.3x11",
                                  note="Wide temperature range")
            self.assertEqual(component, part)
        with self.subTest("TKR330M1VD11M"):
            part = capacitors_partname_decoder.resolve("TKR330M1VD11M")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Jamicon",
                                  partnumber="TKR330M1VD11M",
                                  working_temperature_range=TemperatureRange('-55', '105'),
                                  series="TK",
                                  capacitance="33uF",
                                  voltage="35V",
                                  tolerance={'min': "-20%", 'max': '+20%'},
                                  dielectric_type="Aluminium oxide",
                                  case="5.5x11",
                                  note="Wide temperature range")
            self.assertEqual(component, part)
        # ---------------- SK -----------------
        with self.subTest("SKP471M1AE11M"):
            part = capacitors_partname_decoder.resolve("SKP471M1AE11M")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Jamicon",
                                  partnumber="SKP471M1AE11M",
                                  working_temperature_range=TemperatureRange('-40', '105'),
                                  series="SK",
                                  capacitance="470uF",
                                  voltage="10V",
                                  tolerance={'min': "-20%", 'max': '+20%'},
                                  dielectric_type="Aluminium oxide",
                                  case="6.3x11",
                                  note="General purpose")
            self.assertEqual(component, part)
        # ---------------- NS -----------------
        with self.subTest("NSP470M0JE07ME2"):
            part = capacitors_partname_decoder.resolve("NSP470M0JE07ME2")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Jamicon",
                                  partnumber="NSP470M0JE07ME2",
                                  working_temperature_range=TemperatureRange('-40', '85'),
                                  series="NS",
                                  capacitance="47uF",
                                  voltage="6.3V",
                                  tolerance={'min': "-20%", 'max': '+20%'},
                                  dielectric_type="Aluminium oxide",
                                  case="6.3x7",
                                  note="7mmL, Bi-pola")
            self.assertEqual(component, part)
        # ---------------- SS -----------------
        with self.subTest("SSP2R2M1JC07ME2"):
            part = capacitors_partname_decoder.resolve("SSP2R2M1JC07ME2")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Jamicon",
                                  partnumber="SSP2R2M1JC07ME2",
                                  working_temperature_range=TemperatureRange('-40', '85'),
                                  series="SS",
                                  capacitance="2.2uF",
                                  voltage="63V",
                                  tolerance={'min': "-20%", 'max': '+20%'},
                                  dielectric_type="Aluminium oxide",
                                  case="5x7",
                                  note="7mmL, General purpose")
            self.assertEqual(component, part)
            # ---------------- SH -----------------
            with self.subTest("SHR100M1HE07M"):
                part = capacitors_partname_decoder.resolve("SHR100M1HE07M")
                self.assertIsNotNone(part)
                component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                      manufacturer="Jamicon",
                                      partnumber="SHR100M1HE07M",
                                      working_temperature_range=TemperatureRange('-55', '105'),
                                      series="SH",
                                      capacitance="10uF",
                                      voltage="50V",
                                      tolerance={'min': "-20%", 'max': '+20%'},
                                      dielectric_type="Aluminium oxide",
                                      case="6.3x7",
                                      note="7mmL, Wide temperature range")
                self.assertEqual(component, part)

    def test_kemet(self):
        with self.subTest("C0603C393K5RAC"):
            part = capacitors_partname_decoder.resolve("C0603C393K5RAC")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Kemet",
                                  partnumber="C0603C393K5RAC",
                                  working_temperature_range=TemperatureRange('-55', '125'),
                                  series="C",
                                  capacitance="39nF",
                                  voltage="50V",
                                  tolerance={'min': "-10%", 'max': '+10%'},
                                  dielectric_type="X7R",
                                  case="0603",
                                  note="Standard")
            self.assertEqual(component, part)

    def test_yaego(self):
        # ---------------- CC -----------------
        with self.subTest("CC0402JRNPO9BN330"):
            part = capacitors_partname_decoder.resolve("CC0402JRNPO9BN330")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Yageo",
                                  partnumber="CC0402JRNPO9BN330",
                                  working_temperature_range=TemperatureRange('-55', '125'),
                                  series="CC",
                                  capacitance="33pF",
                                  voltage="50V",
                                  tolerance={'min': "-5%", 'max': '+5%'},
                                  dielectric_type="NP0",
                                  case="0402",
                                  note="Paper/PE taping reel; Reel 7 inch")
            self.assertEqual(component, part)
        with self.subTest("CC1206MKX7RDBB102"):
            part = capacitors_partname_decoder.resolve("CC1206MKX7RDBB102")
            self.assertIsNotNone(part)
            component = Capacitor(capacitor_type=Capacitor.Type.MLCC,
                                  manufacturer="Yageo",
                                  partnumber="CC1206MKX7RDBB102",
                                  working_temperature_range=TemperatureRange('-55', '125'),
                                  series="CC",
                                  capacitance="1nF",
                                  voltage="2000V",
                                  tolerance={'min': "-20%", 'max': '+20%'},
                                  dielectric_type="X7R",
                                  case="1206",
                                  note="Blister taping reel; Reel 7 inch")
            self.assertEqual(component, part)


if __name__ == "__main__":
    unittest.main()
