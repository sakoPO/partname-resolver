from decimal import Decimal
import re


def build_group(dictionary):
    group = '('
    for key in dictionary.keys():
        group = group + str(key) + '|'
    group = group[:-1] + ')'
    return group


def resistance_string_to_ohm(string):
    multiply = {'R': Decimal(1), 'K': Decimal(1000), 'M': Decimal(1000000)}
    if string == '0000':
        return 0
    match = re.match(r'(\d+)(R|M|K)(\d+)?', string)
    if match:
        number = Decimal(match.group(1))
        mul = multiply[match.group(2)]
        value = number * mul
        if match.group(3) is not None:
            decimal = Decimal(match.group(3)) / (10 ** len(match.group(3)))
            value += decimal * mul
        return value
    else:
        value = Decimal(string[0:-1])
        mul = Decimal("1E" + string[-1])
        return value * mul