from decimal import Decimal


def capacitance_string_to_farads(string):
    if string[0] == 'R':
        return Decimal(string[1:len(string)]) / Decimal('100') * Decimal('10') ** Decimal('-12')
    if string[1] == 'R':
        return Decimal(string.replace('R', '.')) * Decimal('10') ** Decimal('-12')
    value = Decimal(string[:2])
    mul = Decimal(string[2])
    return value * Decimal('10') ** mul * Decimal('10') ** Decimal('-12')


def build_group(dictionary):
    group = '('
    for key in dictionary.keys():
        group = group + str(key) + '|'
    group = group[:-1] + ')'
    return group
