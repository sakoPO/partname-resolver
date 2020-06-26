from partname_resolver.components.inductor import Inductor
from partname_resolver.units.temperature import TemperatureRange
from partname_resolver.inductors.common import *
from partname_resolver.case.chip import Chip
from partname_resolver.units.length import Dimmension, Length, LengthTolerance
from partname_resolver.inductors.murata_common import *
import re

product_id = {'BL': 'Chip Ferrite Beads'}

structure = {'A': 'Array Type',
             'M': 'Ferrite Bead Single Type',
             'T': 'Assembly Type'}

applications = {'AG': 'For General Use',
                'AX': 'For General Use',
                'TG': 'For General Use',
                'BA': 'For High-speed Signal Lines',
                'BB': 'For High-speed Signal Lines',
                'BC': 'For High-speed Signal Lines',
                'BD': 'For High-speed Signal Lines',
                'BX': 'For High-speed Signal Lines',
                'KD': 'For Power Lines',
                'KG': 'For Power Lines',
                'KN': 'For Power Lines',
                'KX': 'For Power Lines',
                'PD': 'For Power Lines',
                'PG': 'For Power Lines',
                'PX': 'For Power Lines',
                'PT': 'For Power Lines',
                'SD': 'For Power Lines',
                'SG': 'For Power Lines',
                'SN': 'For Power Lines',
                'SP': 'For Power Lines',
                'RK': 'For Digital Interface',
                'HG': 'For GHz Band General Use',
                'EB': 'For GHz Band High-speed Signal Lines (Low Direct Current Type)',
                'EG': 'For GHz Band General Use(Low DC Resistance Type)',
                'EX': 'For GHz Band General Use(Low DC Resistance Type)',
                'HB': 'For GHz Band High-speed Signal Lines',
                'HD': 'For GHz Band High-speed Signal Lines',
                'HE': 'For GHz Band High-speed Signal Lines',
                'HK': 'For GHz Band Digital Interface',
                'GA': 'For High-GHz Band High-speed Signal Lines',
                'GG': 'For High-GHz Band General Use'}


def build_regexpr():
    product_id_group = build_group(product_id)  # 1
    structure_group = build_group(structure)  # 2
    dimension_group = build_group(dimensions)  # 3
    applications_group = build_group(applications)  # 4
    impedance_group = '(R\d{2}|\dR\d|\d{3})'  # 5
    electrode_group = build_group(features)  # 6
    category_group = '(C)'  # 7
    number_of_circuits_group = '(1|4)'  # 8
    package_group = build_group(package)  # 9
    return product_id_group + structure_group + dimension_group + applications_group + impedance_group + \
           electrode_group + category_group + number_of_circuits_group + package_group


def decode_match(match):
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
        5) + match.group(6) + match.group(7) + match.group(8) + match.group(9)
    series = match.group(2)
    return Inductor(inductor_type=inductor_type[match.group(2)],
                    manufacturer="Murata Manufacturing",
                    partnumber=partnumber,
                    working_temperature_range=None,
                    series=match.group(1) + series,
                    inductance=None,
                    tolerance=None,
                    q=None,
                    dc_resistance=None,
                    rated_current=None,
                    self_resonant_frequency=None,
                    max_working_voltage=None,
                    case=dimensions[match.group(3)],
                    note=applications[match.group(4)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
