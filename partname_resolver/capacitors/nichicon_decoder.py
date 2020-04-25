from .capacitor import Capacitor
from .tolerance import Tolerance
from .common import *
import re

series = {'VZ': 'Wide Temperature Range',
          'VR': 'Miniature Sized',
          'KA': 'For High Grade Audio Equipment, Wide Temperature Range',
          'CS': 'Miniature Sized, High Ripple Current, High Reliability',
          'CY': 'Miniature Sized, High Ripple Current, High Reliability'}

voltage = {'0E': '2.5VDC',
           '0G': '4VDC',
           '0J': '6.3VDC',
           '1A': '10VDC',
           '1C': '16VDC',
           '1E': '25VDC',
           '1V': '35VDC',
           '1H': '50VDC',
           '1J': '63VDC',
           '1K': '80VDC',
           '2A': '100VDC',
           '2C': '160VDC',
           '2D': '200VDC',
           '2E': '250VDC',
           '2F': '315VDC',
           '2V': '350VDC',
           '2G': '400VDC',
           '2W': '450VDC',
           '2J': '630VDC',
           '3A': '1000VDC',
           'MF': '250VAC'}

tolerance = {'B': Tolerance('-0.1pF', '+0.1pF'),
             'C': Tolerance('-0.25pF', '+0.25pF'),
             'D': Tolerance('-0.5pF', '+0.5pF'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'R': 'Depends on individual standards.',
             'W': Tolerance('-0.05pF', '+0.05pF')}

configuration = {'DD': '5',
                 'ED': '6.3',
                 'PD': '8 - 10',
                 'HD': '12.5 - 18',
                 'RD': '20 - 25'}


def build_regexpr(product_id):
    product_series_group = '(' + product_id + ')'  # 1
    series_name_group = build_group(series)  # 2
    voltage_group = build_group(voltage)  # 3
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 4
    tolerance_group = build_group(tolerance)  # 5
    configuration_group = build_group(configuration)  # 6

    return product_series_group + series_name_group + voltage_group + capacitance_group + tolerance_group + configuration_group + '?'


def decode_match(match):
    return Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                     manufacturer="Nichicon",
                     partnumber=match.group(1)+match.group(2)+match.group(3)+match.group(4)+match.group(5)+match.group(6),
                     series=match.group(2),
                     capacitance=capacitance_string_to_farads(match.group(4)) * Decimal('1000000'),
                     voltage=voltage[match.group(3)],
                     tolerance=tolerance[match.group(5)],
                     dielectric_type="Aluminium oxide",
                     case=configuration[match.group(6)],
                     note=series[match.group(2)])


def resolve_U(partname):
    product_id = 'U'

    regexpr = build_regexpr(product_id)
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)


def resolve(partname):
    part = resolve_U(partname)
    if part:
        return part
