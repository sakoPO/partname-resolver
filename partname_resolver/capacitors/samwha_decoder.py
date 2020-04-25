from .capacitor import Capacitor
from .tolerance import Tolerance
from .common import *
import re

series = {'CA': 'Chip type, Long Life Series',
          'RC': 'Chip type, Wide Temperature Range Series',
          'RD': 'Wide Temperature Range Series',
          'SD': 'Standard, For General Purposes Series'}

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

tolerance = {'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'V': Tolerance('-10%', '+20%'),
             'Q': Tolerance('-10%', '+30%'),
             'T': Tolerance('-10%', '+50%')}

case_diameter = {'03': '3mm',
                 '04': '4mm',
                 '05': '5mm',
                 '6L': '6.3mm',
                 '08': '8mm',
                 '10': '10mm',
                 '12': '12.5mm',
                 '14': '14.5mm',
                 '16': '16mm',
                 '18': '18mm',
                 '22': '22mm',
                 '25': '25.5mm'}


def build_regexpr():
    series_name_group = build_group(series)  # 1
    voltage_group = build_group(voltage)  # 2
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 3
    tolerance_group = build_group(tolerance)  # 4
    case_diameter_group = build_group(case_diameter)  # 5
    case_height_group = '(\d{3}|\d{2}M)'  # 6
    lead_taping_group = '(VR|BB)'  # 7
    # internal_control_code =
    return series_name_group + voltage_group + capacitance_group + tolerance_group + case_diameter_group + \
           case_height_group + lead_taping_group + '?'


def decode_match(match):
    return Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                     manufacturer="Samwha",
                     partnumber=match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
                         5) + match.group(6) + match.group(7),
                     series=match.group(1),
                     capacitance=capacitance_string_to_farads(match.group(3)),
                     voltage=voltage[match.group(2)],
                     tolerance=tolerance[match.group(4)],
                     dielectric_type="Aluminium oxide",
                     case=case_diameter[match.group(5)],
                     note=series[match.group(1)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
