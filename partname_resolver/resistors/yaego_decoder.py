from .common import *
from .resistor import Resistor
from .tolerance import Tolerance
import re
from decimal import Decimal

series = {'AC': 'THICK FILM CHIP RESISTORSAUTOMOTIVE GRADE',
          'RC': 'General purpose chip resistors'}

resistor_type = {'AC': Resistor.Type.ThickFilmResistor,
                 'RC': Resistor.Type.ThickFilmResistor}

size = {'0201': '0201',
        '0402': '0402',
        '0603': '0603',
        '0805': '0805',
        '1206': '1206',
        '1210': '1210',
        '1812': '1812'}

tolerance = {'F': Tolerance('1%'),
             'J': Tolerance('5%')}

packing_type = {'R': 'Paper/PE taping reel',
                'K': 'Embossed taping reel'}

temperature_coefficient = {'-': 'Baseon spec'}

taping_reel = {'07': '7 inch diameter Reel',
               '10': '10 inch diameter Reel',
               '13': '13 inch diameter Reel',
               '7W': '7 inch dia. Reel & 2 x standard power',
               '3W': '13 inch dia. Reel & 2 x standard power'}

optional_code = {'L': ''}

max_working_voltage = {'0201': '25V',
                       '0402': '50V',
                       '0603': '75V',
                       '0805': '150V',
                       '0508': '150V',
                       '1206': '200V',
                       '0612': '200V',
                       '1210': '200V',
                       '1812': '200V',
                       '1218': '200V',
                       '2010': '200V',
                       '1020': '200V',
                       '2512': '200V',
                       '1225': '200V'}

power = {'WH': Decimal('0.03125'),
         'WM': Decimal('0.05'),
         '0402': Decimal('0.0625'),  # 1/16W
         'WA': Decimal('0.1'),
         'W8': Decimal('0.125'),
         'W4': Decimal('0.25'),
         'W2': Decimal('0.5'),
         '1W': Decimal('1'),
         'SA': Decimal('0.1'),
         'S8': Decimal('0.125'),
         'S4': Decimal('0.25'),
         'S3': Decimal('0.333'),
         '07': Decimal('0.75'),
         'U2': Decimal('0.5')}


def build_regexpr():
    series_group = build_group(series)  # 1
    size_group = build_group(size)  # 2
    tolerance_group = build_group(tolerance)  # 3
    packing_type_group = build_group(packing_type)  # 4
    temperature_coefficient_group = build_group(temperature_coefficient)  # 5
    taping_reel_group = build_group(taping_reel)  # 6
    resistance_group = '(\d{2}[RKM]\d{1}|\d{1}[RKM]\d{1,2}|\d{1,3}[RKM])'  # 7
    optional_code_group = build_group(optional_code)  # 8

    return series_group + size_group + tolerance_group + packing_type_group + temperature_coefficient_group + \
           taping_reel_group + resistance_group + optional_code_group + '?'


def decode_match(match):
    return Resistor(resistor_type=resistor_type[match.group(1)],
                    manufacturer="Yaego",
                    partnumber=match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
                        5) + match.group(6) + match.group(7) + match.group(8),
                    series=match.group(1),
                    resistance=resistance_string_to_ohm(match.group(7)),
                    power=power[match.group(2)],
                    max_working_voltage=max_working_voltage[match.group(2)],
                    tolerance=tolerance[match.group(3)],
                    case=size[match.group(2)],
                    note=series[match.group(1)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
