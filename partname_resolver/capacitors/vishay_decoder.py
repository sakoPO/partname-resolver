from .common import *
from .capacitor import Capacitor
from partname_resolver.units.capacitanceTolerance import Tolerance
import re

size = {'0201': '0201',
        '0402': '0402',
        '0603': '0603',
        '0805': '0805',
        '1206': '1206',
        '1210': '1210',
        '1812': '1812'}

dielectric_type = {'D': 'C0G',  # High frequency
                   'Q': 'C0G',  # High Q
                   'A': 'C0G',
                   'G': 'X5R',
                   'Y': 'X7R',
                   'V': 'Y5V'
                   }

tolerance = {'B': Tolerance('0.1pF'),
             'C': Tolerance('0.25pF'),
             'D': Tolerance('0.5pF'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'Z': Tolerance('-20%', '+80%')}

termination = {'E': 'AgPd',
               'X': 'Ni barrier100 % tin platematte finish',
               'N': 'Non-magnetic',
               'L': 'Ni barrierwith tin leadplated finishmin. 4 % lead'}

voltage = {'S': '4V',
           'Y': '6.3V',
           'Q': '10V',
           'J': '16V',
           'X': '25V',
           'Z': '35V',
           'A': '50V',
           'B': '100V',
           'C': '200V',
           'P': '250V'}

packing_style = {'T': '7" reel/plastic tape',
                 'C': '7" reel/paper tape',
                 'O': '7" reel/flamed paper tape',
                 'J': '7" reel (low quantity)',
                 'R': '1 1/4"/13" reel/plastic tape',
                 'P': '11 1/4"/13" reel/paper tape',
                 'I': '11 1/4"/13" reel/flamed paper tape',
                 'B': 'Bulk'}


def build_regexpr(product_id):
    product_series_group = '(' + product_id + ')'  # 1
    dimensions_group = build_group(size)  # 2
    dielectric_type_group = build_group(dielectric_type)  # 3
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 4
    tolerance_group = build_group(tolerance)  # 5
    termination_group = build_group(termination)  # 6
    voltage_group = build_group(voltage)  # 7
    marking_group = '(A)'  # 8
    packing_style_group = build_group(packing_style)  # 9

    return product_series_group + dimensions_group + dielectric_type_group + capacitance_group + tolerance_group + termination_group + voltage_group + marking_group + packing_style_group + '?'


def build_regexpr_v2(product_id):
    product_series_group = '(' + product_id + ')'  # 1
    dimensions_group = build_group(size)  # 2
    dielectric_type_group = build_group(dielectric_type)  # 3
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 4
    tolerance_group = build_group(tolerance)  # 5
    termination_group = build_group(termination)  # 6
    voltage_group = build_group(voltage)  # 7
    packing_style_group = build_group(packing_style)  #
    process_code = '(W1BC)'

    return product_series_group + dimensions_group + dielectric_type_group + capacitance_group + tolerance_group + termination_group + voltage_group + packing_style_group + process_code + '?'


def decode_match(match):
    return Capacitor(capacitor_type=Capacitor.Type.MLCC,
                     manufacturer="Vishay",
                     partnumber=match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
                         5) + match.group(6) + match.group(7) + match.group(8) + match.group(9),
                     series='VJ',
                     capacitance=capacitance_string_to_farads(match.group(4)),
                     voltage=voltage[match.group(7)],
                     tolerance=tolerance[match.group(5)],
                     dielectric_type=dielectric_type[match.group(3)],
                     case=size[match.group(2)],
                     note=termination[match.group(6)])


def resolve_VJ(partname):
    product_id = 'VJ'
    regexpr = build_regexpr(product_id)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
    regexpr = build_regexpr_v2(product_id)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)


def resolve(partname):
    part = resolve_VJ(partname)
    if part:
        return part
