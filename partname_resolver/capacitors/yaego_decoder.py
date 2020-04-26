from .capacitor import Capacitor
from .tolerance import Tolerance
from .common import *
import re

size = {'0201': '0201',
        '0402': '0402',
        '0603': '0603',
        '0805': '0805',
        '1206': '1206',
        '1210': '1210',
        '1812': '1812'}

tolerance = {'B': Tolerance('-0.1pF', '+0.1pF'),
             'C': Tolerance('-0.25pF', '+0.25pF'),
             'D': Tolerance('0.5pF'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'Z': Tolerance('-20%', '+80%')}

packing_style = {'R': 'Paper/PE taping reel; Reel 7 inch',
                 'K': 'Blister taping reel; Reel 7 inch',
                 'P': 'Paper/PE taping reel; Reel 13 inch',
                 'F': 'Blister taping reel; Reel 13 inch',
                 'C': 'Bulk case'}

voltage = {'5': '6.3V',
           '6': '10V',
           '7': '16V',
           '8': '25V',
           '9': '50V',
           'C': '1000V',
           'D': '2000V',
           'S': '2500V',
           'E': '3000V'}

dielectric_type = {'COG': 'C0G',
                   'NPO': 'NP0',
                   'X5R': 'X5R',
                   'X7R': 'X7R',
                   'X8R': 'X8R',
                   'Y5V': 'Y5V'}


def build_regexpr(product_id):
    product_series_group = '(' + product_id + ')'  # 1
    dimensions_group = build_group(size)  # 2 (1)
    tolerance_group = build_group(tolerance)  # 3 (2)
    packing_style_group = build_group(packing_style)  # 4 (3)
    dielectric_type_group = build_group(dielectric_type)  # 5
    voltage_group = build_group(voltage)  # 6 (4)
    bn_const = '(BN|BB)'  # 7
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 8 (4)

    return product_series_group + dimensions_group + tolerance_group + packing_style_group + dielectric_type_group + voltage_group + bn_const + capacitance_group + '?'


def decode_match(match):
    partname = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
                         5) + match.group(6) + match.group(7)
    partname += match.group(8) if match.group(8) is not None else ""
    return Capacitor(capacitor_type=Capacitor.Type.MLCC,
                     manufacturer="Yaego",
                     partnumber=partname,
                     series='CC',
                     capacitance=capacitance_string_to_farads(match.group(8)),
                     voltage=voltage[match.group(6)],
                     tolerance=tolerance[match.group(3)],
                     dielectric_type=dielectric_type[match.group(5)],
                     case=size[match.group(2)],
                     note=packing_style[match.group(4)])


def resolve_CC(partname):
    product_id = 'CC'

    regexpr = build_regexpr(product_id)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)


def resolve(partname):
    part = resolve_CC(partname)
    if part:
        return part
