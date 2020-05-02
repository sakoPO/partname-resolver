# based on https://www.yuden.co.jp/productdata/catalog/mlcc_all_e.pdf

from partname_resolver.components.capacitor import Capacitor
from partname_resolver.units.capacitanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
from .common import *
import re

voltage = {'P': '2.5V',
           'A': '4V',
           'J': '6.3V',
           'L': '10V',
           'E': '16V',
           'T': '25V',
           'G': '35V',
           'U': '50V',
           'H': '100V',
           'Q': '250V',
           'S': '630V',
           'X': '2000V'}

series_name = {'M': 'Multilayer ceramic capacitor',
               'V': 'Multilayer ceramic capacitor for high frequency',
               'W': 'LW reverse type multilayer capacitor'}

plating = {'K': 'Plated',
           'S': 'Cu Internal Electrodes (For High Frequency)'}

size = {'021': '008004',
        '042': '01005',
        '063': '0201',
        '105': '0402',
        '107': '0603',
        '212': '0805',
        '316': '1206',
        '325': '1210',
        '432': '1812'}

size_tolerance = {'A': '',
                  'B': '',
                  'C': '',
                  'E': ''}

dielectric_type = {'CG': 'C0G',
                   'UJ': 'U2J',
                   'UK': 'U2K',
                   'BJ': 'X5R',
                   'B7': 'X7R',
                   'C6': 'X6S',
                   'C7': 'X7S',
                   'LD': 'X5R'}

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

thickness = {'K': '0.125mm',
             'H': '0.13mm',
             'E': '0.18mm',
             'C': '0.2mm',
             # 'D': '0.2mm',
             'P': '0.3mm',
             'T': '0.3mm',
             # 'K': '0.45mm',
             'V': '0.5mm',
             'W': '0.5mm',
             'A': '0.8mm',
             'D': '0.85mm',
             'F': '1.15mm',
             'G': '1.25mm',
             'L': '1.6mm',
             'N': '1.9mm',
             'Y': '2.0mm',
             'M': '2.5mm'}

packing_type = {'F': 'φ178mm Taping (2mm pitch)',
                'T': 'φ178mm Taping (4mm pitch)',
                'P': 'φ178mm Taping (4mm pitch, 1000 pcs/reel) 325 type (Thickness code M)',
                'R': 'φ178mm Taping (2mm pitch) 105type only （Thickness code E,H）',
                'W': 'φ178mm Taping (1mm pitch)021/042type only'}

operating_temperature_range = {'CG': TemperatureRange('-55', '125'),
                               'UJ': TemperatureRange('-55', '125'),
                               'UK': TemperatureRange('-55', '125'),
                               'BJ': TemperatureRange('-55', '85'),
                               'B7': TemperatureRange('-55', '125'),
                               'C6': TemperatureRange('-55', '105'),
                               'C7': TemperatureRange('-55', '125'),
                               'LD': TemperatureRange('-55', '85')}


def build_regexpr():
    voltage_group = build_group(voltage)  # 1
    series_name_group = build_group(series_name)  # 2
    plating_group = build_group(plating)  # 3
    dimensions_group = build_group(size)  # 4
    # dimensions_tolerance_group = build_group(size_tolerance)  # 5
    temperature_group = build_group(dielectric_type)  # 5
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 6
    tolerance_group = build_group(tolerance)  # 7
    thickness_group = build_group(thickness)  # 8
    special_code_group = '(\-)'  # 9
    packing_type_group = build_group(packing_type)  # 10

    return voltage_group + series_name_group + plating_group + dimensions_group + temperature_group + capacitance_group \
           + tolerance_group + thickness_group + special_code_group + packing_type_group + '?'


def decode_match(match):
    return Capacitor(capacitor_type=Capacitor.Type.MLCC,
                     manufacturer="Taiyo Yuden",
                     partnumber=match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
                         5) + match.group(6) + match.group(7) + match.group(8) + match.group(9) + match.group(10),
                     working_temperature_range=operating_temperature_range[match.group(5)],
                     series=match.group(2),
                     capacitance=capacitance_string_to_farads(match.group(6)),
                     voltage=voltage[match.group(1)],
                     tolerance=tolerance[match.group(7)],
                     dielectric_type=dielectric_type[match.group(5)],
                     case=size[match.group(4)],
                     note=series_name[match.group(2)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
