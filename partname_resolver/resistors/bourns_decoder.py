from .common import *
from .resistor import Resistor
from .tolerance import Tolerance
import re
from decimal import Decimal

series = {'CAT16': 'Concave Terminations',
          'CAY16': 'Convex Terminations',
          'CHV': 'Thick Film High Voltage Chip Resistors'}

resistor_type = {'CAT16': Resistor.Type.ThickFilmResistorArray,
                 'CAY16': Resistor.Type.ThickFilmResistorArray,
                 'CHV': Resistor.Type.ThickFilmResistor}

tolerance = {'F': Tolerance('1%'),
             'J': Tolerance('5%')}

termination = {'LF': 'Tin-plated (RoHS compliant)'}

size_CAT16 = {'J2': '0606',
              'F4': '1206',
              'J4': '1206',
              'F8': '2406',
              'J8': '2406'}

size_CAY16 = {'J2': '0606',
              'F4': '1206',
              'J4': '1206',
              'F8': '2406',
              'J8': '1506'}

size = {'CAT16': size_CAT16, 'CAY16': size_CAY16}

tcr = {'X': '100ppm/K',
       'W': '200ppm/K'}

power = {'0603': Decimal('0.1'),
         '0805': Decimal('0.125'),
         '1206': Decimal('0.25'),
         '2010': Decimal('0.5'),
         '2512': Decimal('1')}

maximum_working_voltage = {'0603': '200V',
                           '0805': '400V',
                           '1206': '800V',
                           '2010': '2000V',
                           '2512': '3000V'}


def build_regexpr_CHV():
    series_group = '(CHV)'  # 1
    size_group = '(0603|0805|1206|2010|2512)'  # 2
    separator = '(-)'  # 3
    tolerance_group = build_group(tolerance)  # 4
    tcr_group = build_group(tcr)  # 5
    separator2 = '(-)'  # 6
    resistance_group = '(\d{3}|\d{2}R|\d{1}R\d{1}])'  # 7
    packing_group = '(E)'  # 8
    termination_group = build_group(termination)  # 9
    return series_group + size_group + separator + tolerance_group + tcr_group + separator2 + resistance_group + \
           packing_group + termination_group + '?'


def decode_match_CHV(match):
    return Resistor(resistor_type=resistor_type[match.group(1)],
                    manufacturer="Bourns",
                    partnumber=match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
                        5) + match.group(6) + match.group(7) + match.group(8) + match.group(9),
                    series=match.group(1),
                    resistance=resistance_string_to_ohm(match.group(7)),
                    power=power[match.group(2)],
                    max_working_voltage=maximum_working_voltage[match.group(2)],
                    tolerance=tolerance[match.group(4)],
                    case=match.group(2),
                    note=series[match.group(1)])


def build_regexpr():
    series_group = build_group(series)  # 1
    separator = '(-)'  # 2
    resistance_group = '(\d{3}|\d{2}R|\d{1}R\d{1}])'  # 3
    tolerance_group = build_group(tolerance)  # 4
    resistors_group = '(2|4|8)'  # 5
    termination_group = build_group(termination)  # 6
    return series_group + separator + resistance_group + tolerance_group + resistors_group + termination_group + '?'


def decode_match(match):
    return Resistor(resistor_type=resistor_type[match.group(1)],
                    manufacturer="Bourns",
                    partnumber=match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
                        5) + match.group(6),
                    series=match.group(1),
                    resistance=resistance_string_to_ohm(match.group(3)),
                    power=Decimal('0.125') if match.group(4) + match.group(5) == "J2" else Decimal('0.25'),
                    max_working_voltage='25V' if match.group(1) + match.group(4) + match.group(
                        5) == "CAY16J8" else '50V',
                    tolerance=tolerance[match.group(4)],
                    case=size[match.group(1)][match.group(4) + match.group(5)],
                    note=series[match.group(1)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)

    regexpr = build_regexpr_CHV()
    match = re.match(regexpr, partname)
    if match:
        return decode_match_CHV(match)
