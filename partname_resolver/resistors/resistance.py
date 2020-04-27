from decimal import Decimal
import re


class Resistance:
    multiply = {u'G': Decimal('1000000000'),
                u'G\u03a9': Decimal('1000000000'),
                u'GR': Decimal('1000000000'),
                u'M': Decimal('1000000'),
                u'M\u03a9': Decimal('1000000'),
                u'MR': Decimal('1000000'),
                u'k': Decimal('1000'),
                u'k\u03a9': Decimal('1000'),
                u'kR': Decimal('1000'),
                u'R': Decimal('1'),
                u'\u03a9': Decimal('1'),
                u'm': Decimal('0.001'),
                u'm\u03a9': Decimal('0.001'),
                u'mR': Decimal('0.001'),
                u'u': Decimal('0.000001'),
                u'u\u03a9': Decimal('0.000001'),
                u'uR': Decimal('0.000001')}

    def __init__(self, resistance):
        if isinstance(resistance, Decimal):
            self.resistance = resistance
        elif isinstance(resistance, str):
            self.resistance = self.__convert_str_resistance_to_decimal_ohms(resistance)
        else:
            print(resistance)
            raise TypeError

    def get_value(self):
        return self.resistance

    def __str__(self):
        return self.__convert_decimal_ohm_to_string()

    def __repr__(self):
        return self.__convert_decimal_ohm_to_string()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.resistance == self.__convert_str_resistance_to_decimal_ohms(other)
        if isinstance(other, Resistance):
            return self.resistance == other.resistance

    @staticmethod
    def __convert_str_resistance_to_decimal_ohms(resistance):
        resistance = resistance.replace("Ohms", "\u03a9")
        resistance = resistance.replace("Ohm", "\u03a9")
        try:
            separated = re.split('(\d+)', resistance)
            if separated[-1] in Resistance.multiply:
                multiplier = Resistance.multiply[separated[-1]]
                value = Decimal(resistance.replace(separated[-1], ''))
                value = value * multiplier
                return value
            else:
                for i, chunk in enumerate(separated):
                    if chunk in Resistance.multiply:
                        multiplier = Resistance.multiply[chunk]
                        resistance = Decimal(resistance.replace(chunk, '.'))
                        resistance = resistance * multiplier
                        return resistance
                return Decimal(resistance)
        except:
            print("Unable to convert resistance: " + resistance)
            raise

    def __convert_decimal_ohm_to_string(self):
        if self.resistance == Decimal('0'):
            return u'0\u03a9'
        for key in ['u\u03a9', 'm\u03a9', '\u03a9', 'k\u03a9', 'M\u03a9', 'G\u03a9']:
            value = self.resistance / Resistance.multiply[key]
            if value < Decimal('1000.0') and value >= Decimal('0.0'):
                value = value.quantize(Decimal('.01'))
                return str(value).rstrip('0').rstrip('.') + str(key)
