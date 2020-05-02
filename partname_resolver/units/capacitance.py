from .unit_base import Unit
from decimal import Decimal
import re


class Capacitance(Unit):
    multiply = {'G': Decimal('1000000000'),
                'GF': Decimal('1000000000'),
                'M': Decimal('1000000'),
                'MF': Decimal('1000000'),
                'k': Decimal('1000'),
                'kF': Decimal('1000'),
                'F': Decimal('1'),
                'm': Decimal('0.001'),
                'mF': Decimal('0.001'),
                'u': Decimal('0.000001'),
                u"\u00B5": Decimal('0.000001'),
                'uF': Decimal('0.000001'),
                u"\u00B5F": Decimal('0.000001'),
                'n': Decimal('0.000000001'),
                'nF': Decimal('0.000000001'),
                'p':  Decimal('0.000000000001'),
                'pF': Decimal('0.000000000001'),
                'f': Decimal('0.000000000000001'),
                'fF': Decimal('0.000000000000001')}

    def __init__(self, capacitance):
        if isinstance(capacitance, Decimal):
            value = capacitance
        elif isinstance(capacitance, str):
            value = self.__convert_str_capacitance_to_decimal_farads(capacitance)
        else:
            print(capacitance)
            raise TypeError(capacitance)
        super().__init__("Farad", 'F', value)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == self.__convert_str_capacitance_to_decimal_farads(other)
        if isinstance(other, Capacitance):
            return self.value == other.value

    @staticmethod
    def __convert_str_capacitance_to_decimal_farads(capacitance):
        """Convert string ie: 100nF to capacitance in farads of type Decimal"""
        try:
            separatedCapacitance = re.split('(\d+)', capacitance)
            if separatedCapacitance[-1] in Capacitance.multiply:
                multiplier = Capacitance.multiply[separatedCapacitance[-1]]
                value = Decimal(capacitance.replace(separatedCapacitance[-1], ''))
                value = value * multiplier
                return value
            else:
                for i, chunk in enumerate(separatedCapacitance):
                    if chunk in Capacitance.multiply:
                        multiplier = Capacitance.multiply[chunk]
                        capacitance = Decimal(capacitance.replace(chunk, '.'))
                        capacitance = capacitance * multiplier
                        return capacitance
                return Decimal(capacitance)
        except:
            print(capacitance)
            raise


class CapacitanceRange:
    def __init__(self, min, max):
        if isinstance(min, Capacitance):
            self.min = min
        else:
            self.min = Capacitance(min)
        if isinstance(max, Capacitance):
            self.max = max
        else:
            self.max = Capacitance(max)

    def __eq__(self, other):
        return self.min == other.min and self.max == other.max

    def __str__(self):
        return str(self.min) + '...' + str(self.max)

    def __repr__(self):
        return self.__str__()

