from partname_resolver.components.inductor import Inductor
from partname_resolver.units.temperature import TemperatureRange
from partname_resolver.inductors.common import *
from .murata_common import *
import re

product_id = {'LQ': 'Chip inductor'}

structure = {'M': 'Multilayer Type (Ferrite Core)',
             'H': 'Wire Wound Type (Ferrite Core',
             'G': 'Multilayer Type (Air-core Inductors (Coils)',
             'W': 'Wire Wound Type (Ferrite Core'}

application_and_haracteristics = {'LQM': {'D': 'for Choke (Low-current DC Power Supplies)',
                                          'F': 'for Choke (DC Power Supplies)',
                                          'P': 'for Power Line'},
                                  'LQH': {'D': 'for Choke',
                                          'S': 'for Choke (Magnetically Shielded Type)',
                                          'C': 'for Choke (Coating Type)',
                                          'P': 'for Power Line'},
                                  'LQW': {'D': 'for Power Line'}}

category = {'N': 'Standard Type',
            'B': 'Special Feature Classification',
            'W': 'Special Feature Classification'}

features = {'0': 'Standard Type',
            '2': 'Standard Type',
            '3': 'Low DC Resistance',
            '5': 'Low Profile Type',
            '7': 'Large Current Type',
            '8': 'Low DC Resistance/Large Current Type',
            'P': ''}

thickness = {'B': '',
             'C': '',
             'D': '',
             'E': '',
             'F': '',
             'O': '',
             'G': '',
             'J': '',
             'M': '',
             'N': '',
             'P': '',
             'T': '',
             '26': '',
             '38': ''}

electrode = {'0': 'Sn',
             '2': 'Sn',
             '3': 'LF Solder',
             'A': 'Au Plating',
             'L': 'Lead-Free Solder Plating',
             'S': 'Sn Plating',
             'F': 'Sn Plating',
             'T': 'Sn Plating'}

specification = {'0': '',
                 'S': '',
                 'C': '',
                 'H': '',
                 'A': '',
                 'E': '',
                 'R': ''}

operating_temperature_range = {'G': TemperatureRange('-55', '125'),
                               'H': TemperatureRange('-40', '105')}

inductor_type = {'G': Inductor.Type.MultilayerInductor,
                 'H': Inductor.Type.WireWoundInductor,
                 'P': Inductor.Type.FilmInductor,
                 'W': Inductor.Type.WireWoundInductor}

def build_regexpr():
    product_id_group = build_group(product_id)  # 1
    series_group = build_group(structure)  # 2
    dimension_group = build_group(dimensions)  # 3
    application_and_haracteristics_group = '(C|H|M|P|T|A)'  # build_group(application_and_haracteristics)  # 4
    category_group = build_group(category)  # 5
    inductance_group = '(R\d{2}|\dR\d|\d{3})'  # 6
    tolerance_group = build_group(tolerance)  # 7
    features_group = build_group(features)  # 8
    # thickness_group = build_group(thickness)  # 9
    electrode_group = build_group(electrode)  # 10
    # specification_group = build_group(specification) + '?'  # 11
    package_group = build_group(package)  # 12
    return product_id_group + series_group + dimension_group + application_and_haracteristics_group + \
           category_group + inductance_group + tolerance_group + features_group + electrode_group + \
           package_group


def decode_match(match):
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
        5) + match.group(6) + match.group(7) + match.group(8) + match.group(9) + match.group(10)
    series = match.group(2)

    return Inductor(inductor_type=inductor_type[match.group(2)],
                    manufacturer="Murata Manufacturing",
                    partnumber=partnumber,
                    working_temperature_range=operating_temperature_range[series],
                    series=match.group(1) + series,
                    inductance=inductance_string_to_henry(match.group(6)) * Decimal(1000000),
                    tolerance=tolerance[match.group(7)],
                    q='8',
                    dc_resistance=None,
                    rated_current=None,
                    self_resonant_frequency=None,
                    max_working_voltage=None,
                    case=dimensions[match.group(3)],
                    note=None)


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
