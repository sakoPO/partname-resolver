class Chip:
    class Dimensions:
        iec_en_standard_dimensions = {'0402': {'L': 0.4, "W": 0.2},
                                      '0404': {'L': 0.4, "W": 0.4},
                                      '0603': {'L': 0.6, "W": 0.3},
                                      '0505': {'L': 0.5, "W": 0.5},
                                      '0805': {'L': 0.8, "W": 0.5}
                                      }

        def __init__(self, L, W, T, t):
            self.L = L
            self.W = W
            self.T = T
            self.t = t

        @staticmethod
        def from_IEC_EN_code(iec_en_code, T=0, t=0):
            tmp_dim = Chip.Dimensions.iec_en_standard_dimensions[iec_en_code]
            return Chip.Dimensions(tmp_dim["L"], tmp_dim["W"], T, t)



    eia_to_iec_en = {'1005': '0402',
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

    def __init__(self, EIA_case_code, L=None, W=None, T=None, t=None):
        self.EIA_code = EIA_case_code
        self.IEC_EN_code = Chip.eia_to_iec_en[EIA_case_code]
        if L is None and W is None and T is None and t is None:
            self.dimensions = Chip.Dimensions.from_IEC_EN_code(self.IEC_EN_code)
        else:
            self.dimensions = Chip.Dimensions(L, W, T, t)

    def __str__(self):
        return "EIA: " + str(self.EIA_code) + " IEC/EN:" + str(self.IEC_EN_code)

    def __repr__(self):
        return "Chip case, EIA: " + str(self.EIA_code) + ", IEC/EN: " + str(self.IEC_EN_code) + ", L=" + str(self.dimensions.L) + ",W=" + str(self.dimensions.W) + ",T=" + str(self.dimensions.T) + ", t=" + str(self.dimensions.t)