from partname_resolver.components.capacitor import Capacitor
from partname_resolver.units.capacitanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
from .common import *
import re

size = {'0201': '0201',
        '0402': '0402',
        '0603': '0603',
        '0805': '0805',
        '1206': '1206',
        '1210': '1210',
        '1812': '1812'}

dielectric_type = {'CG': 'C0G',
                   'CH': 'C0H',
                   'HG': 'HG',
                   'LG': 'LG',
                   'PH': 'PH',
                   'RH': 'RH',
                   'SH': 'SH',
                   'TH': 'TH',
                   'UJ': 'UJ',
                   'SL': 'SL',
                   'X': 'X5R',
                   'B': 'X7R',
                   'BS': 'X7S',
                   'DS': 'X6S',
                   'E': 'Z5U',
                   'F': 'Y5V'}

tolerance = {'A': Tolerance('0.05pF'),
             'B': Tolerance('-0.1pF', '+0.1pF'),
             'C': Tolerance('-0.25pF', '+0.25pF'),
             'D': Tolerance('0.5pF'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'S': Tolerance('-20%', '+50%'),
             'Z': Tolerance('-20%', '+80%')}

termination = {'S': 'Silver Solderable Termination',
               'C': 'Copper Solderable Termination',
               'N': 'Nickel Barrier Termination'}

package_style = {'B': 'Bulk Bag',
                 'T': 'Taping Package'}

operating_temperature_range = {'COG': TemperatureRange('-55', '125'),
                               'COH': TemperatureRange('-55', '125'),
                               'HG': TemperatureRange('-25', '85'),
                               'LG': TemperatureRange('-25', '85'),
                               'PH': TemperatureRange('-25', '85'),
                               'RH': TemperatureRange('-25', '85'),
                               'SH': TemperatureRange('-25', '85'),
                               'TH': TemperatureRange('-25', '85'),
                               'UJ': TemperatureRange('-25', '85'),
                               'SL': TemperatureRange('-25', '85'),
                               'X7R': TemperatureRange('-55', '125'),
                               'X5R': TemperatureRange('-55', '85'),
                               'X7S': TemperatureRange('-55', '125'),
                               'X6S': TemperatureRange('-55', '105'),
                               'Z5U': TemperatureRange('10', '85'),
                               'Y5V': TemperatureRange('-25', '85')}


def decode_voltage(voltage_str):
    if voltage_str.find('R') != -1:
        return voltage_str.replace('R', '.') + 'V'
    else:
        value = Decimal(voltage_str[:-1])
        mul = Decimal('1E' + voltage_str[-1])
        return str(value * mul) + 'V'


def build_regexpr():
    size_group = build_group(size)  # 1
    dielectric_type_group = build_group(dielectric_type)  # 2
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 3
    tolerance_group = build_group(tolerance)  # 4
    voltage_group = '(R\d{2}|\dR\d|\d{3})'  # 5
    termination_group = build_group(termination)  # 6
    packing_style_group = build_group(package_style)  # 7
    return size_group + dielectric_type_group + capacitance_group + tolerance_group + voltage_group + \
           termination_group + packing_style_group


def decode_match(match):
    partname = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
        5) + match.group(6) + match.group(7)
    dielectric = dielectric_type[match.group(2)]
    note = "Termination: " + termination[match.group(6)] + ", Packing: " + package_style[match.group(7)]
    return Capacitor(capacitor_type=Capacitor.Type.MLCC,
                     manufacturer="Fenghua Advanced Technology",
                     partnumber=partname,
                     working_temperature_range=operating_temperature_range[dielectric],
                     series=None,
                     capacitance=capacitance_string_to_farads(match.group(3)),
                     voltage=decode_voltage(match.group(5)),
                     tolerance=tolerance[match.group(4)],
                     dielectric_type=dielectric,
                     case=size[match.group(1)],
                     note=note)


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
