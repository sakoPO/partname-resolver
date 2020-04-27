from .common import *
from .resistor import Resistor
from partname_resolver.units.resistanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
import re
from decimal import Decimal

size = {'0201': '0201',
        '0402': '0402',
        '0603': '0603',
        '0805': '0805',
        '0508': '0508',
        '1206': '1206',
        '0612': '0612',
        '1210': '1210',
        '1812': '1812',
        '1218': '1218',
        '2010': '2010',
        '1020': '1020',
        '2512': '2512',
        '1225': '1225',
        'CS03': '0603',
        'CS05': '0805',
        'CS06': '1206',
        'CS07': '1210',
        'CS10': '2010',
        'CS12': '2512',
        'CQ02': '0402',
        'CQ03': '0603',
        'CQ05': '0805',
        'CQ06': '1206',
        'CQ07': '1210',
        'CQ10': '2010',
        'CQ12': '2512',
        '2D02': '2D02',
        '4D02': '4D02',
        '4D03': '4D03',
        '10P8': '10P8',
        '16P8': '16P8'}

power = {'WH': Decimal('0.03125'),
         'WM': Decimal('0.05'),
         'WG': Decimal('0.0625'),
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

tolerance = {'D': Tolerance('0.5%'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%')}

packing_type = {'T': "Tape/Reel"}

packing_quantity = {'1': '1000pcs',
                    '2': '2000pcs',
                    '4': '4000pcs',
                    '5': '5000pcs',
                    'A': '500pcs',
                    'C': '10000pcs',
                    'D': '20000pcs',
                    'E': '15000pcs',
                    'F': '40000pcs',
                    'G': '60000pcs'}

special_feature = {'E': 'Lead (Pb) Free Plating Type/ RoHS compliant',
                   'T': 'Special T.C.R.'}

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
                       '1225': '200V',
                       '2D02': '50V',
                       '4D02': '50V',
                       '4D03': '50V',
                       '10P8': '50V',
                       '16P8': '25V'}


def build_regexpr():
    size_group = build_group(size)  # 1
    wattage_group = build_group(power)  # 2
    tolerance_group = build_group(tolerance)  # 3
    resistance_group = '(\d{4}|\d{3}J|\d{3}K|\d{3}L)'  # 4
    packing_type_group = build_group(packing_type)  # 5
    packing_quantity_group = build_group(packing_quantity)  # 6
    special_feature_group = build_group(special_feature)  # 7
    return size_group + wattage_group + tolerance_group + resistance_group + packing_type_group + \
           packing_quantity_group + '?' + special_feature_group + '?'


def resistance_string_to_ohm(string):
    mul_map = {'J': Decimal('0.1'), 'K': Decimal('0.01'), 'L': Decimal('0.001')}
    if string[3] in ['J', 'K', 'L']:
        mul = mul_map[string[3]]
    else:
        mul = Decimal("1E" + string[3])

    value = Decimal(string[0:-1])
    return value * mul


def decode_match(match):
    size_name = size[match.group(1)]
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(5)
    partnumber += match.group(6) if match.group(6) is not None else ""
    partnumber += match.group(7) if match.group(7) is not None else ""
    array = ['2D02', '4D02', '4D03', '10P8', '16P8']
    return Resistor(resistor_type=Resistor.Type.ThickFilmResistorArray if match.group(
        1) in array else Resistor.Type.ThickFilmResistor,
                    manufacturer="Royal Ohm",
                    partnumber=partnumber,
                    working_temperature_range=TemperatureRange(Decimal('-55'), Decimal('155')),
                    series='',
                    resistance=resistance_string_to_ohm(match.group(4)),
                    power=power[match.group(2)],
                    max_working_voltage=max_working_voltage[size_name],
                    tolerance=tolerance[match.group(3)],
                    case=size_name,
                    note=special_feature[match.group(7)] if match.group(7) is not None else "")


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
