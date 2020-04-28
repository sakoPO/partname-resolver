# based on https://search.murata.co.jp/Ceramy/image/img/A01X/partnumbering_e_02.pdf
from .capacitor import Capacitor
from partname_resolver.units.capacitanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
from .common import *
import re

dimension = {'03': '0201',
             '15': '0402',
             '18': '0603',
             '21': '0805',
             '31': '1206',
             '32': '1210',
             '43': '1812',
             '55': '2220'}

height_excepat_kc = {'3': '0.3mm',
                     '5': '0.5mm',
                     '6': '0.6mm',
                     '8': '0.8mm',
                     '9': '0.85mm',
                     'A': '1mm',
                     'B': '1.25mm',
                     'C': '1.6mm',
                     'D': '2mm',
                     'E': '2.5mm',
                     'M': '1.15mm',
                     #         'N': '1.35mm',
                     'Q': '1.5mm',
                     #         'R': '1.8mm',
                     'X': 'Depends on individual standards'}

height_kc_only = {'L': '2.8mm',
                  'Q': '3.7mm',
                  'T': '4.8mm',
                  'W': '6.4mm'}

dielectric_type = {'0C': 'CHA',
                   '1C': 'CG',
                   '2C': 'CH',
                   '3C': 'CJ',
                   '4C': 'CK',
                   '5C': 'C0G',
                   '5G': 'X8G',
                   '7U': 'U2J',
                   '9E': 'ZLM',
                   'C7': 'X7S',
                   'C8': 'X6S',
                   'D7': 'X7T',
                   'L8': 'X8L',
                   'M8': 'X8M',
                   'M9': 'X9M',
                   'R1': 'R',
                   'R6': 'X5R',
                   'R7': 'X7R',
                   'R9': 'X8R'}

operating_temperature_range = {'0C': TemperatureRange('-55', '150'),
                               '1C': None,
                               '2C': TemperatureRange('-55', '125'),
                               '3C': TemperatureRange('-55', '125'),
                               '4C': TemperatureRange('-55', '125'),
                               '5C': TemperatureRange('-55', '125'),
                               '5G': TemperatureRange('-55', '150'),
                               '7U': TemperatureRange('-55', '125'),
                               '9E': TemperatureRange('-55', '125'),
                               'C7': TemperatureRange('-55', '125'),
                               'C8': TemperatureRange('-55', '105'),
                               'D7': TemperatureRange('-55', '125'),
                               'L8': TemperatureRange('-55', '150'),
                               'M8': TemperatureRange('-55', '150'),
                               'M9': None,
                               'R1': TemperatureRange('-55', '125'),
                               'R6': TemperatureRange('-55', '85'),
                               'R7': TemperatureRange('-55', '125'),
                               'R9': TemperatureRange('-55', '150')}

voltage = {'0E': '2.5V',
           '0G': '4V',
           '0J': '6.3V',
           '1A': '10V',
           '1C': '16V',
           '1E': '25V',
           'YA': '35V',
           '1H': '50V',
           '1J': '63V',
           '1K': '80V',
           '2A': '100V',
           '2E': '250V',
           '2W': '450V',
           '2J': '630V',
           '3A': '1000V',
           'MF': '250VAC'}

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

package = {'L': 'ø180mm Embossed Taping',
           'D': 'ø180mm Paper Taping',
           'W': 'ø180mm Paper Taping',
           'K': 'ø330mm Embossed Taping',
           'J': 'ø330mm Paper Taping',
           '#': 'Unknown package'}


def build_regexpr(product_id, series, height_dimmension):
    product_series_group = '(' + product_id + ')'  # 1
    series_group = build_group(series)  # 2
    dimmensions_group = build_group(dimension)  # 3
    height_group = build_group(height_dimmension)  # 4
    temperature_group = build_group(dielectric_type)  # 5
    voltage_group = build_group(voltage)  # 6
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 7
    tolerance_group = build_group(tolerance)  # 8
    individual_specificatin_code_group = '(.{3})'  # 9
    package_group = build_group(package)

    return product_series_group + series_group + dimmensions_group + height_group + temperature_group + voltage_group + capacitance_group + tolerance_group + individual_specificatin_code_group + package_group + '?'


def decode_match(match, series_code, height):
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
        5) + match.group(6) + match.group(7) + match.group(8) + match.group(9)
    partnumber += match.group(10) if match.group(10) is not None else ""
    return Capacitor(capacitor_type=Capacitor.Type.MLCC,
                     manufacturer="Murata Manufacturing",
                     partnumber=partnumber,
                     working_temperature_range=operating_temperature_range[match.group(5)],
                     series=match.group(1) + match.group(2),
                     capacitance=capacitance_string_to_farads(match.group(7)),
                     voltage=voltage[match.group(6)],
                     tolerance=tolerance[match.group(8)],
                     dielectric_type=dielectric_type[match.group(5)],
                     case=dimension[match.group(3)],
                     note=series_code[match.group(2)])


def resolve_GC(partname):
    product_id = 'GC'
    series_code = {
        '3': 'High Effective Capacitance & High Ripple Current Chip Multilayer Ceramic Capacitors for Automotive',
        'B': 'Ni Plating + Pd Plating termination Conductive Glue Mounting Chip Multilayer Ceramic Capacitors for Automotive',
        'D': 'MLSC Design Chip Multilayer Ceramic Capacitors for Automotive',
        'E': 'Soft Termination MLSC Design Chip Multilayer Ceramic Capacitors for Automotive',
        'G': 'AgPd Termination Conductive Glue Mounting Chip Multilayer Ceramic Capacitors for Automotive',
        'J': 'Soft Termination Chip Multilayer Ceramic Capacitors for Automotive',
        'M': 'Chip Multilayer Ceramic Capacitors for Automotive',
        'Q': 'High Q Chip Multilayer Ceramic Capacitors for Automotive'}

    regexpr = build_regexpr(product_id, series_code, height_excepat_kc)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match, series_code, height_excepat_kc)


def resolve_GG(partname):
    product_id = 'GG'
    series_code = {'D': 'Water Repellent MLSC Design Chip Multilayer Ceramic Capacitors for Automotive',
                   'M': 'Water Repellent Chip Multilayer Ceramic Capacitors for Automotive'}

    regexpr = build_regexpr(product_id, series_code, height_excepat_kc)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match, series_code, height_excepat_kc)


def resolve_GR(partname):
    product_id = 'GR'
    series_code = {'T': 'AEC-Q200 Compliant Chip Multilayer Ceramic Capacitors for Infotainment',
                   'M': 'Chip Multilayer Ceramic Capacitors for General Purpose'}

    regexpr = build_regexpr(product_id, series_code, height_excepat_kc)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match, series_code, height_excepat_kc)


def resolve_GX(partname):
    product_id = 'GX'
    series_code = {'T': 'AEC-Q200 Compliant Water Repellent Chip Multilayer Ceramic Capacitors for Infotainment'}

    regexpr = build_regexpr(product_id, series_code, height_excepat_kc)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match, series_code, height_excepat_kc)


def resolve_KC(partname):
    product_id = 'KC'
    series_code = {
        '3': 'High Effective Capacitance & High Allowable Ripple Current Metal Terminal Type Multilayer Ceramic Capacitors for Automotive',
        'A': 'Safety Standard Certified Metal Terminal Type Multilayer Ceramic Capacitors for Automotive',
        'M': 'Metal Terminal Type Multilayer Ceramic Capacitors for Automotive'}

    regexpr = build_regexpr(product_id, series_code, height_kc_only)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match, series_code, height_kc_only)


def resolve(partname):
    part = resolve_GC(partname)
    if part:
        return part
    part = resolve_GG(partname)
    if part:
        return part
    part = resolve_GR(partname)
    if part:
        return part
    part = resolve_GX(partname)
    if part:
        return part
    part = resolve_KC(partname)
    if part:
        return part
