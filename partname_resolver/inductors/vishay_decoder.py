from partname_resolver.components.inductor import Inductor
from partname_resolver.units.inductanceTolerance import Tolerance
from partname_resolver.units.temperature import TemperatureRange
from partname_resolver.inductors.common import *
from partname_resolver.units.length import Dimmension, Length, LengthTolerance
import re

product_family = {'IHLP': '',
                  'IHLE': '',
                  'IHCL': '',
                  'IHLD': '',
                  'IHLW': '',
                  'IHLM': ''}

dimensions = {'1212': '1212',
              '1616': '1616',
              '2020': '2020',
              '2525': '2525',
              '3232': '3232',
              '4040': '4040',
              '5050': '5050',
              '6767': '6767'}

profile_height = {'A': Length('1mm'),
                  'B': Length('2mm'),
                  'C': Length('3mm'),
                  'D': Length('4mm'),
                  'Z': Length('0mm'),
                  'AB': Length('1.2mm'),
                  'CZ': Length('3.0mm'),
                  'DZ': Length('4mm'),
                  'FD': Length('6.4mm'),
                  'AE': Length('4mm')}

package_code = {'RZ': '',
                'ER': 'tape / reel, lead free'}

tolerance = {'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'N': Tolerance('30%')}

series = {'01': 'Commercial / High Saturation',
          '11': 'Commercial / Low DCR',
          '51': 'Commercial / High Temp (155 °C)',
          '81': 'Commercial / High Temp (180 °C)',
          'A1': 'Automotive / High Saturation',
          '1A': 'Automotive / Low DCR',
          '5A': 'Automotive / High Temp (155 °C)',
          '8A': 'Automotive / High Temp (180 °C)',
          '1L': ''}


def build_regexpr():
    product_family_group = build_group(product_family)  # 1
    dimension_group = build_group(dimensions)  # 2
    profile_height_group = build_group(profile_height)  # 3
    package_code_group = build_group(package_code)  # 4
    inductance_group = '(R\d{2}|\dR\d|\d{3})'  # 5
    tolerance_group = build_group(tolerance)  # 6
    series_group = build_group(series)  # 7
    return product_family_group + dimension_group  + profile_height_group + package_code_group + inductance_group + \
           tolerance_group + series_group


def decode_match(match):
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
        5) + match.group(6) + match.group(7)
    return Inductor(inductor_type=Inductor.Type.WireWoundInductor,
                    manufacturer="Vishay",
                    partnumber=partnumber,
                    working_temperature_range=TemperatureRange('-55', '125'),
                    series=match.group(1),
                    inductance=inductance_string_to_henry(match.group(5)) * Decimal(1000000),
                    tolerance=tolerance[match.group(6)],
                    q=None,
                    dc_resistance=None,
                    rated_current=None,
                    self_resonant_frequency=None,
                    max_working_voltage='40V',
                    case=dimensions[match.group(2)],
                    note=series[match.group(7)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
