from partname_resolver.components.capacitor import Capacitor
from partname_resolver.units.capacitanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
from .common import *
import re

series = {'VZ': 'Wide Temperature Range',
          'VR': 'Miniature Sized',
          'KA': 'For High Grade Audio Equipment, Wide Temperature Range',
          'CS': 'Miniature Sized, High Ripple Current, High Reliability',
          'CY': 'Miniature Sized, High Ripple Current, High Reliability'}

voltage = {'0E': '2.5V',
           '0G': '4V',
           '0J': '6.3V',
           '1A': '10V',
           '1C': '16V',
           '1E': '25V',
           '1V': '35V',
           '1H': '50V',
           '1J': '63V',
           '1K': '80V',
           '2A': '100V',
           '2C': '160V',
           '2D': '200V',
           '2E': '250V',
           '2F': '315V',
           '2V': '350V',
           '2G': '400V',
           '2W': '450V',
           '2J': '630V',
           '3A': '1000V',
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


operating_temperature_range = {'VZ': lambda voltage : TemperatureRange('-55', '105') if voltage < 101 else TemperatureRange('-40', '105') if voltage < 401 else TemperatureRange('-25', '105'),
                               'VR': lambda voltage : TemperatureRange('-40', '85') if voltage < 401 else TemperatureRange('-25', '85'),
                               'KA': lambda voltage: TemperatureRange('-55', '105'),
                               'CS': lambda voltage : TemperatureRange('-40', '105') if voltage < 401 else TemperatureRange('-25', '105'),
                               'CY': lambda voltage : TemperatureRange('-40', '105') if voltage < 401 else TemperatureRange('-25', '105')}

packing = {'1TD': 'Unknown'}

def build_regexpr(product_id):
    product_series_group = '(' + product_id + ')'  # 1
    series_name_group = build_group(series)  # 2
    voltage_group = build_group(voltage)  # 3
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 4
    tolerance_group = build_group(tolerance)  # 5
    configuration_group = build_group(configuration)  # 6
    packing_group = build_group(packing)
    return product_series_group + series_name_group + voltage_group + capacitance_group + tolerance_group +\
           configuration_group  + packing_group + '?'


def decode_match(match):
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(5) + match.group(6)
    partnumber += match.group(7) if match.group(7) is not None else ''
    voltage_str = voltage[match.group(3)]
    return Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                     manufacturer="Nichicon",
                     partnumber=partnumber,
                     working_temperature_range=operating_temperature_range[match.group(2)](Decimal(voltage_str[:-1])),
                     series=match.group(2),
                     capacitance=capacitance_string_to_farads(match.group(4)) * Decimal('1000000'),
                     voltage=voltage_str,
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
