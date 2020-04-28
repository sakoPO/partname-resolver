from .capacitor import Capacitor
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

voltage = {'4': '4V',
           '6': '6.3V',
           'Z': '10V',
           'Y': '16V',
           '3': '25V',
           '5': '50V',
           '1': '100V',
           '2': '200V',
           '7': '500V'}

dielectric_type = {'C': 'X7R'}

tolerance = {'B': Tolerance('-0.1pF', '+0.1pF'),
             'C': Tolerance('-0.25pF', '+0.25pF'),
             'D': Tolerance('0.5pF'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'R': 'Depends on individual standards.',
             'W': Tolerance('-0.05pF', '+0.05pF')}

failure_rate = {'A': "Not Applicable"}

terminations = {'T': 'Plated Ni and Sn',
                '7': 'Gold Plated',
                'Z': 'FLEXITERM'}

packing = {'2': '7" Reel',
           '4': '13" Reel',
           '7': 'Bulk Cass.',
           '9': 'Bulk'}

special_code = {'A': 'Standard product'}

operating_temperature_range = {'C': TemperatureRange('-55', '125')}


def build_regexpr():
    dimensions_group = build_group(size)  # 1
    voltage_group = build_group(voltage)  # 2
    temperature_group = build_group(dielectric_type)  # 3
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 4
    tolerance_group = build_group(tolerance)  # 5
    failure_rate_group = build_group(failure_rate)  # 6
    terminations_group = build_group(terminations)  # 7
    packing_type_group = build_group(packing)  # 8
    special_code_group = build_group(special_code)  # 9
    return dimensions_group + voltage_group + temperature_group + capacitance_group + tolerance_group + \
           failure_rate_group + terminations_group + packing_type_group + special_code_group + '?'


def decode_match(match):
    return Capacitor(capacitor_type=Capacitor.Type.MLCC,
                     manufacturer="AVX",
                     partnumber=match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
                         5) + match.group(6) + match.group(7) + match.group(8) + match.group(9),
                     working_temperature_range=operating_temperature_range[match.group(3)],
                     series="",
                     capacitance=capacitance_string_to_farads(match.group(4)),
                     voltage=voltage[match.group(2)],
                     tolerance=tolerance[match.group(5)],
                     dielectric_type=dielectric_type[match.group(3)],
                     case=size[match.group(1)],
                     note=special_code[match.group(9)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
