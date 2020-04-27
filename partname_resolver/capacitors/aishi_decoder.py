from .capacitor import Capacitor
from partname_resolver.units.capacitanceTolerance import Tolerance
from .common import *
import re

category_code = {'E': ''}

series = {'WH': 'Miniature aluminium electrolytic capacitors'}

voltage = {'0J': '6.3V',
           '1A': '10V',
           '1C': '16V',
           '1E': '25V',
           '1V': '35V',
           '1H': '50V',
           '1J': '63V',
           '1K': '100V',
           '2C': '160V',
           '2D': '200V',
           '2E': '250V',
           '2V': '350V',
           '2G': '400V',
           '2W': '450V',
           '2H': '500V'}

tolerance = {'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%')}

size_code = {'D11': '5x11',
             'E11': '6.3x11',
             'F11': '8x11',
             'F12': '8x12',
             'G20': '10x20',
             'W20': '12.5x20',
             'W25': '12.5x25',
             'L25': '16x25',
             'L35': '16x35',
             'M40': '18x40'}

terminal_code = {'O': ''}

sleeve_code = {'C': 'PVC Sleeve',
               'T': 'PET Sleeve'}


def build_regexpr():
    category_code_group = build_group(category_code)  # 1
    series_name_group = build_group(series)  # 2
    voltage_group = build_group(voltage)  # 3
    tolerance_group = build_group(tolerance)  # 4
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 5
    size_code_group = build_group(size_code)  # 6
    terminal_code_group = build_group(terminal_code)  # 7
    sleeve_code_group = build_group(sleeve_code)  # 8
    return category_code_group + series_name_group + voltage_group + tolerance_group + capacitance_group + \
           size_code_group + terminal_code_group + sleeve_code_group + '?'


def decode_match(match):
    partnumber = match.group(1)+match.group(2)+match.group(3)+match.group(4)+match.group(5)+match.group(6)+\
                 match.group(7) + match.group(8)
    return Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                     manufacturer="Aishi",
                     partnumber=partnumber,
                     series=match.group(2),
                     capacitance=capacitance_string_to_farads(match.group(5)) * Decimal('1000000'),
                     voltage=voltage[match.group(3)],
                     tolerance=tolerance[match.group(4)],
                     dielectric_type="Aluminium oxide",
                     case=size_code[match.group(6)],
                     note=series[match.group(2)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
