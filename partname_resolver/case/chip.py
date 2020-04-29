# Vishay H - height
from partname_resolver.units.length import Dimmension, Length, LengthTolerance


class Chip:
    class Dimensions:
        iec_en_standard_dimensions = {'0402': {'L': Length('0.4mm'), "W": Length('0.2mm')},
                                      '0404': {'L': Length('0.4mm'), "W": Length('0.4mm')},
                                      '0603': {'L': Length('0.6mm'), "W": Length('0.3mm')},
                                      '0505': {'L': Length('0.5mm'), "W": Length('0.5mm')},
                                      '0805': {'L': Length('0.8mm'), "W": Length('0.5mm')},
                                      '1005': {'L': Length('1.0mm'), "W": Length('0.5mm')},
                                      '1608': {'L': Length('1.6mm'), "W": Length('1.8mm')},
                                      '2520': {'L': Length('2.5mm'), "W": Length('2mm')},
                                      '3216': {'L': Length('3.2mm'), "W": Length('1.6mm')}
                                      }

        def __init__(self, L, W, T, t1, t2):
            self.L = L
            self.W = W
            self.T = T
            self.t1 = t1
            if t1 is not None and t2 is None:
                self.t2 = t1
            else:
                self.t2 = t2

        def __str__(self):
            t1 = ", t1=" + str(self.t1) if self.t1 is not None else ""
            t2 = ", t2=" + str(self.t2) if self.t2 is not None else ""
            return "L=" + str(self.L) + ", W=" + str(self.W) + ", T=" + str(self.T) + t1 + t2

        def __eq__(self, other):
            return self.L == other.L and self.W == other.W and self.T == other.T and self.t1 == other.t1 and \
                   self.t2 == other.t2

        @staticmethod
        def from_IEC_EN_code(iec_en_code, T=0, t1=0, t2=0):
            tmp_dim = Chip.Dimensions.iec_en_standard_dimensions[iec_en_code]
            return Chip.Dimensions(tmp_dim["L"], tmp_dim["W"], T, t1, t2)

    eia_to_iec_en = {'01005': '0402',
                     '1005': '0402',
                     '15015': '0404',
                     '0201': '0603',
                     '0202': '0505',
                     '0302': '0805',
                     '0504': '1310',
                     '0402': '1005',
                     '0603': '1608',
                     '0805': '2012',
                     '1008': '2520',
                     '1111': '2828',
                     '1206': '3216',
                     '1210': '3225',
                     '1410': '3625',
                     '1515': '3838',
                     '1806': '4516'
                     }

    def __init__(self, EIA_case_code, L=None, W=None, T=None, t1=None, t2=None):
        self.EIA_code = EIA_case_code
        self.IEC_EN_code = Chip.eia_to_iec_en[EIA_case_code]
        if L is None and W is None:
            self.dimensions = Chip.Dimensions.from_IEC_EN_code(self.IEC_EN_code, T=T, t1=t1, t2=t2)
        else:
            self.dimensions = Chip.Dimensions(L, W, T, t1, t2)

    def get_full_str(self):
        return "EIA " + str(self.EIA_code) + ", IEC/EN " + self.IEC_EN_code + ", " + str(self.dimensions)

    def __eq__(self, other):
        return self.EIA_code == other.EIA_code and self.IEC_EN_code == other.IEC_EN_code and \
               self.dimensions == other.dimensions

    def __str__(self):
        height = ", H=" + str(self.dimensions.T) if self.dimensions.T is not None else ''
        return "EIA " + str(self.EIA_code) + height

    def __repr__(self):
        return "Chip case, EIA: " + str(self.EIA_code) + ", IEC/EN: " + str(self.IEC_EN_code) + ", L=" + str(
            self.dimensions.L) + ",W=" + str(self.dimensions.W) + ",T=" + str(self.dimensions.T) + ", t=" + str(
            self.dimensions.t)
