from partname_resolver.components.inductor import Inductor
from partname_resolver.units.inductanceTolerance import Tolerance
from partname_resolver.units.temperature import TemperatureRange
from partname_resolver.inductors.common import *
from partname_resolver.units.length import Dimmension, Length, LengthTolerance
import re

series_name = {'NR': 'SMD Power Inductors',
               'NRH': '',
               'NRS': '',
               'NRV': ''}

dimensions = {'2010': '2010',
              '2012': '2012',
              '2410': '2410',
              '3010': '3010',
              '3012': '3012',
              '4010': '4010',
              '4012': '4012',
              '4018': '4018',
              '5010': '5010',
              '5012': '5012',
              '5014': '5014',
              '5020': '5020',
              '5024': '5024',
              '5030': '5030',
              '5040': '5040',
              '6010': '6010',
              '6012': '6012',
              '6014': '6014',
              '6020': '6020',
              '6028': '6028',
              '6045': '6045',
              '8030': '8030',
              '8040': '8040'}

packaging = {'T': 'Taping'}

tolerance = {'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'N': Tolerance('30%')}


def build_regexpr():
    series_name_group = build_group(series_name)  # 1
    dimension_group = build_group(dimensions)  # 2
    packaging_group = build_group(packaging)  # 3
    inductance_group = '(R\d{2}|\dR\d|\d{3})'  # 4
    tolerance_group = build_group(tolerance)  # 5
    return series_name_group + dimension_group + packaging_group + inductance_group + tolerance_group


def get_temperature_range(series, dimmensions):
    if series == 'NRS' and dimensions[:2] in ['40', '50', '60', '80']:
        return TemperatureRange('-25', '125')
    return TemperatureRange('-25', '120')

def decode_match(match):
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(5)
    return Inductor(inductor_type=Inductor.Type.WireWoundInductor,
                    manufacturer="Taiyo Yuden",
                    partnumber=partnumber,
                    working_temperature_range=get_temperature_range(match.group(1), match.group(2)),
                    series=match.group(1),
                    inductance=inductance_string_to_henry(match.group(4)) * Decimal(1000000),
                    tolerance=tolerance[match.group(5)],
                    q=None,
                    dc_resistance=None,
                    rated_current=None,
                    self_resonant_frequency=None,
                    max_working_voltage=None,
                    case=dimensions[match.group(2)],
                    note=series_name[match.group(1)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
