from decimal import Decimal
from math import log10
import re

class Unit:
    multiply = {'T': Decimal('1000000000000'),
                'G': Decimal('1000000000'),
                'M': Decimal('1000000'),
                'k': Decimal('1000'),
                '-': Decimal('1'),
                'unitSymbol': Decimal('1'),
                'm': Decimal('0.001'),
                'u': Decimal('0.000001'),
                u"\u00B5": Decimal('0.000001'),
                'n': Decimal('0.000000001'),
                'p':  Decimal('0.000000000001'),
                'f': Decimal('0.000000000000001')}

    prefix_full_name = {'-': None,
                        'm': 'milli',
                        'u': 'micro',
                        'n': 'nano',
                        'p': 'pico',
                        'f': 'femto'}

    prefix_full_name_to_symbol = {'milli': 'm',
                                  'micro': 'u',
                                  'nano': 'n',
                                  'pico': 'p',
                                  'femto': 'f'}

    def __init__(self, name, symbol, value):
        self.str_conversion_prefixes = ['f', 'p', 'n', 'u', 'm', 'unitSymbol', 'k', 'M', 'G']
        self.name = name
        self.symbol = symbol
        self.value = value

    def get_value(self):
        return self.value

    def get_value_as(self, prefix):
        """prefix can be:
         - None: the function is equivalent to self.get_value()
         - full name: milli, micro, etc.
         - short name: n, p, f, M etc.
         - short name and unit symbol: nF, uH, pV
         """
        if prefix is None:
            return self.get_value()
        if not isinstance(prefix, str):
            raise TypeError('prefix parameter have to be string')
        if prefix in Unit.prefix_full_name_to_symbol:
            return self.value / Unit.multiply[Unit.prefix_full_name_to_symbol[prefix]]
        else:
            if prefix == self.symbol:
                return self.value / Unit.multiply['unitSymbol']
            else:
                return self.value / Unit.multiply[prefix.replace(self.symbol, '')]

    def get_closest_prefix(self, prefix_list):
        if abs(self.value) == Decimal('0'):
            return "-"

        unified_prefix_list = []
        for prefix in prefix_list:
            if prefix in self.prefix_full_name_to_symbol:
                unified_prefix_list.append(self.prefix_full_name_to_symbol[prefix])
            elif prefix == self.symbol or prefix == '°C':
                unified_prefix_list.append('-')
            else:
                unified_prefix_list.append(prefix.replace(self.symbol, ''))

        smallest_diff = 100000
        prefix = None
        for key in unified_prefix_list:
            diff = log10(Unit.multiply[key]) - (log10(abs(self.value)) if self.value != Decimal(0) else 0)
            if abs(diff) < abs(smallest_diff):
                smallest_diff = diff
                prefix = key
        return self.prefix_full_name[prefix]

    def __str__(self):
        return self.__convert_value_to_string()

    def __repr__(self):
        return self.__convert_value_to_string()

    def __eq__(self, other):
        return self.value == other.value

    def __convert_value_to_string(self):
        if self.value == Decimal(0):
            return "0" + self.symbol
        for key in self.str_conversion_prefixes:
            value = self.value / Unit.multiply[key]
            if Decimal('1000.0') > abs(value) >= Decimal('0.0'):
                value = value.quantize(Decimal('.01'))
                if key != 'unitSymbol' and str(key) != '-':
                    unit_symbol = key + self.symbol
                else:
                    unit_symbol = self.symbol
                return str(value).rstrip('0').rstrip('.') + unit_symbol

    @staticmethod
    def __convert_str_to_decimal_value(str_value, unit_symbol):
        """Convert string ie: 100nH to value in henry of type Decimal"""
        str_value = str_value.replace(unit_symbol, '')
        try:
            separated_value = re.split('(\d+)', str_value)
            if separated_value[-1] in Unit.multiply:
                multiplier = Unit.multiply[separated_value[-1]]
                value = Decimal(str_value.replace(separated_value[-1], ''))
                value = value * multiplier
                return value
            else:
                for i, chunk in enumerate(separated_value):
                    if chunk in Unit.multiply:
                        multiplier = Unit.multiply[chunk]
                        str_value = Decimal(str_value.replace(chunk, '.'))
                        str_value = str_value * multiplier
                        return str_value
                return Decimal(str_value)
        except:
            print(str_value)
            raise
