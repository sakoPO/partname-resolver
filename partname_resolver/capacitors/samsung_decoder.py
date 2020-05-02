from partname_resolver.components.capacitor import Capacitor
from partname_resolver.units.capacitanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
from .common import *
import re

size = {'03': '0201',
        '05': '0402',
        '10': '0603',
        '21': '0805',
        '31': '1206',
        '32': '1210',
        '43': '1812',
        '55': '2220'}

dielectric_type = {'C': 'C0G',
                   'P': 'P2H',
                   'R': 'R2H',
                   'S': 'S2H',
                   'T': 'T2H',
                   'U': 'U2J',
                   'L': 'S2L',
                   'A': 'X5R',
                   'B': 'X7R',
                   'X': 'X6S',
                   'F': 'Y5V'}

tolerance = {'A': Tolerance("-0.05pF", "+0.05pF"),
             'B': Tolerance('-0.1pF', '+0.1pF'),
             'C': Tolerance('-0.25pF', '+0.25pF'),
             'D': Tolerance('0.5pF'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'Z': Tolerance('-20%', '+80%')}

voltage = {'R': '4V',
           'Q': '6.3V',
           'P': '10V',
           'O': '16V',
           'A': '25V',
           'L': '35V',
           'B': '50V',
           'C': '100V',
           'D': '200V',
           'E': '250V',
           'G': '500V',
           'H': '630V',
           'I': '1000V',
           'J': '2000V',
           'K': '3000V'}

thickness = {'3': '0.3mm',  # 0201
             '5': '0.5mm',  # 0402
             '8': '0.8mm',  # 0603
             'A': '0.65mm',  # 0805
             'C': '0.85mm',
             'F': '1.25mm',
             'Q': '1.25mm',
             'Y': '1.25mm',
             # 'C': '0.85mm',  # 1206
             # 'F': '1.25mm',
             # 'H': '1.6mm',
             # 'F': '1.25mm',  # 1210
             'H': '1.6mm',
             'I': '2.0mm',
             'J': '2.5mm',
             'V': '2.5mm',
             # 'F': '1.25mm',  # 1812
             # 'H': '1.6mm',
             # 'I': '2.0mm',
             # 'J': '2.5mm',
             'L': '3.2mm',
             # 'F': '1.25mm',  # 2220
             # 'H': '1.6mm',
             # 'I': '2.0mm',
             # 'J': '2.5mm',
             # 'L': '3.2mm',
             'U': "2.00mm"
             }

plating = {'A': 'Pd/Ag/Sn',
           'N': 'Ni/Cu/Sn',
           'G': 'Cu/Cu/Sn',
           'L': "Unknown"}

samsung_control_code = {'A': 'Array 2 element',
                        'B': 'Array 4 element',
                        'C': 'High - Q',
                        'N': 'Normal',
                        'P': 'Automotive',
                        'L': 'LICC'}

packing_type = {'B': 'Bulk',
                'P': 'Bulk Case',
                'C': 'Paper 7"',
                'D': 'Paper 13" (10.000EA)',
                'E': 'Embosing 7"',
                'F': 'Embosing 13" (10.000EA)',
                'L': 'Paper 13" (15.000EA)',
                'O': 'Paper 10"',
                'S': 'Embossing 10"',
                'G': 'Unknown'}

operating_temperature_range = {'C': TemperatureRange('-55', '125'),
                               'P': TemperatureRange('-55', '125'),
                               'R': TemperatureRange('-55', '125'),
                               'S': TemperatureRange('-55', '125'),
                               'T': TemperatureRange('-55', '125'),
                               'U': TemperatureRange('-55', '125'),
                               'L': TemperatureRange('-55', '125'),
                               'A': TemperatureRange('-55', '85'),
                               'B': TemperatureRange('-55', '125'),
                               'X': TemperatureRange('-55', '105'),
                               'F': TemperatureRange('-30', '85')}


def build_regexpr(product_id):
    product_series_group = '(' + product_id + ')'  # 1
    dimensions_group = build_group(size)  # 2
    temperature_group = build_group(dielectric_type)  # 3
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 4
    tolerance_group = build_group(tolerance)  # 5
    voltage_group = build_group(voltage)  # 6
    thickness_group = build_group(thickness)  # 7
    plating_group = build_group(plating)  # 8
    samsung_control_code_group = build_group(samsung_control_code)  # 9
    reserved_for_future_use_group = '(N)'  # 10
    packing_type_group = build_group(packing_type)  # 11

    return product_series_group + dimensions_group + temperature_group + capacitance_group + tolerance_group + voltage_group + thickness_group + plating_group + samsung_control_code_group + reserved_for_future_use_group + packing_type_group + '?'


def decode_match(match):
    return Capacitor(capacitor_type=Capacitor.Type.MLCC,
                     manufacturer="Samsung",
                     partnumber=match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(5) +
                                match.group(6) + match.group(7) + match.group(8) + match.group(9) + match.group(10) +
                                match.group(11),
                     working_temperature_range=operating_temperature_range[match.group(3)],
                     series="CL",
                     capacitance=capacitance_string_to_farads(match.group(4)),
                     voltage=voltage[match.group(6)],
                     tolerance=tolerance[match.group(5)],
                     dielectric_type=dielectric_type[match.group(3)],
                     case=size[match.group(2)],
                     note=samsung_control_code[match.group(8)])


def resolve_CL(partname):
    product_id = 'CL'

    regexpr = build_regexpr(product_id)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)


def resolve(partname):
    part = resolve_CL(partname)
    if part:
        return part
