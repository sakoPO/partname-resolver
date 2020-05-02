from .unit_base import Unit
from decimal import Decimal
import re


class Inductance(Unit):
    multiply = {'G': Decimal('1000000000'),
                'GH': Decimal('1000000000'),
                'M': Decimal('1000000'),
                'MH': Decimal('1000000'),
                'k': Decimal('1000'),
                'kH': Decimal('1000'),
                'H': Decimal('1'),
                'm': Decimal('0.001'),
                'mH': Decimal('0.001'),
                'u': Decimal('0.000001'),
                u"\u00B5": Decimal('0.000001'),
                'uH': Decimal('0.000001'),
                u"\u00B5H": Decimal('0.000001'),
                'n': Decimal('0.000000001'),
                'nH': Decimal('0.000000001'),
                'p':  Decimal('0.000000000001'),
                'pH': Decimal('0.000000000001'),
                'f': Decimal('0.000000000000001'),
                'fH': Decimal('0.000000000000001')}

    def __init__(self, inductance):
        if isinstance(inductance, Decimal):
            ind = inductance
        elif isinstance(inductance, str):
            ind = self.__convert_str_inductance_to_decimal_farads(inductance)
        else:
            print(inductance)
            raise TypeError(inductance)
        super().__init__("Henry",  'H', ind)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == self.__convert_str_inductance_to_decimal_farads(other)
        if isinstance(other, Inductance):
            return self.value == other.value

    @staticmethod
    def __convert_str_inductance_to_decimal_farads(inductance):
        """Convert string ie: 100nH to inductance in henry of type Decimal"""
        try:
            separatedCapacitance = re.split('(\d+)', inductance)
            if separatedCapacitance[-1] in Inductance.multiply:
                multiplier = Inductance.multiply[separatedCapacitance[-1]]
                value = Decimal(inductance.replace(separatedCapacitance[-1], ''))
                value = value * multiplier
                return value
            else:
                for i, chunk in enumerate(separatedCapacitance):
                    if chunk in Inductance.multiply:
                        multiplier = Inductance.multiply[chunk]
                        inductance = Decimal(inductance.replace(chunk, '.'))
                        inductance = inductance * multiplier
                        return inductance
                return Decimal(inductance)
        except:
            print(inductance)
            raise


