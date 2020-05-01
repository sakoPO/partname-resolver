from partname_resolver.components.inductor import Inductor
from partname_resolver.units.capacitanceTolerance import Tolerance
from partname_resolver.units.temperature import TemperatureRange
from partname_resolver.inductors.common import *
from partname_resolver.units.length import Dimmension, Length, LengthTolerance
import re

series = {'MPX': 'Metal Composite Power Inductors',
          'MPLCG': 'Large-Current Power Inductors',
          'MPLCV': 'Large-Current Power Inductors'}

version = {'1': ''}

size_code = {'D0520': 'D0520',
             'D0530': 'D0530',
             'D0618': 'D0618',
             'D0624': 'D0624',
             'D0630': 'D0630',
             'D0650': 'D0650',
             'D0830': 'D0830',
             'D0840': 'D0840',
             'D1040': 'D1040',
             'D1235': 'D1235',
             'D1250': 'D1250',
             'D1264': 'D1264',
             'D1740': 'D1740',
             'D1770': 'D1770',
             'D2213': 'D2213',
             '0530': '0530',
             '0630': '0630',
             '0645': '0645',
             '0654': '0654',
             '1054': '1054'}


def build_regexpr():
    series_group = build_group(series)  # 1
    version_group = build_group(version) + '?'  # 2
    size_code_group = build_group(size_code)  # 3
    inductor_code = '(L)'  # 4
    inductance_group = '(R\d{2}|\dR\d|\d{3})'  # 5
    return series_group + version_group + size_code_group + inductor_code + inductance_group


def decode_match(match):
    partnumber = match.group(1) + match.group(2) if match.group(2) is not None else ""
    partnumber += match.group(3) + match.group(4) + match.group(5)
    return Inductor(inductor_type=Inductor.Type.WireWoundInductor,
                    manufacturer="Kemet",
                    partnumber=partnumber,
                    working_temperature_range=TemperatureRange('-55', '125'),
                    series=match.group(1),
                    inductance=inductance_string_to_henry(match.group(5)) * Decimal(1000000),
                    tolerance=Tolerance('20%'),
                    q=None,
                    dc_resistance=None,
                    rated_current=None,
                    self_resonant_frequency=None,
                    max_working_voltage=None,
                    case=size_code[match.group(3)],
                    note=series[match.group(1)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
