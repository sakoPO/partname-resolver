from decimal import Decimal
from .unit_base import Unit
import re


class Power(Unit):
    multiply = {u'G': Decimal('1000000000'),
                u'GW': Decimal('1000000000'),
                u'M': Decimal('1000000'),
                u'MW': Decimal('1000000'),
                u'k': Decimal('1000'),
                u'kW': Decimal('1000'),
                u'W': Decimal('1'),
                u'm': Decimal('0.001'),
                u'mW': Decimal('0.001'),
                u'u': Decimal('0.000001'),
                u'uW': Decimal('0.000001')}

    def __init__(self, power):
        if isinstance(power, Decimal):
            self.power = power
        elif isinstance(power, str):
            self.power = self.__convert_str_power_to_decimal_ohms(power)
        else:
            print(power)
            raise TypeError
        super().__init__("Watt", 'W', self.power)
        self.str_conversion_prefixes = ['u', 'm', '-', 'k', 'M', 'G']

    def __eq__(self, other):
        if isinstance(other, str):
            return self.power == self.__convert_str_power_to_decimal_ohms(other)
        if isinstance(other, Power):
            return self.power == other.power

    @staticmethod
    def __convert_str_power_to_decimal_ohms(power):
        try:
            separated = re.split('(\d+)', power)
            if separated[-1] in Power.multiply:
                multiplier = Power.multiply[separated[-1]]
                value = Decimal(power.replace(separated[-1], ''))
                value = value * multiplier
                return value
            else:
                for i, chunk in enumerate(separated):
                    if chunk in Power.multiply:
                        multiplier = Power.multiply[chunk]
                        power = Decimal(power.replace(chunk, '.'))
                        power = power * multiplier
                        return power
                return Decimal(power)
        except:
            print("Unable to convert power: " + power)
            raise
