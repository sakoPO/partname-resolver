from .capacitor import Capacitor
from .tolerance import Tolerance
from .common import *
import re

type_code = {'J': 'Jamicon Radial Type (PET sleeve)',
             'V': 'SMD (V-chip) Type (Nylon coating)',
             'T': 'Jamicon Snap-in Type (PET sleeve)',
             'P': 'Conductive Polymer Aluminum Solid Capacitor',
             'N': 'Screw Type (PVC sleeve)',
             'C': 'Jamicon Radial and Snap-in Type (PVC sleeve)',
             'H': 'Snap-in Type (No Insulating base, PET sleeve)',
             'M': 'Radial Type 8 pitch=2.5mm (PET sleeve'}

series = {'VP': 'Standard',
          'VB': 'High capacitance & Low E.S.R.',
          'SV': '5mmL, General purpose',
          'ST': '5mmL, Wide temperature range',
          'NT': '5mmL, Bi-polar',
          'SS': '7mmL, General purpose',
          'SH': '7mmL, Wide temperature range',
          'SL': '7mmL, Low impedance',
          'SA': '5&7mmL, Low impedance, Long life',
          'NS': '7mmL, Bi-pola',
          'SK': 'General purpose',
          'TK': 'Wide temperature range',
          'NK': 'Bi-polar',
          'LK': 'Low leakage current'}

tolerance = {'A': Tolerance('-8%', '+32%'),
             'B': Tolerance('-5%', '+10%'),
             'C': Tolerance('+10%', '+30%'),
             'D': Tolerance('-40%', '0%'),
             'E': Tolerance('-12%', '+20%'),
             'F': Tolerance('-5%', '+20%'),
             'G': Tolerance('-30%', '0%'),
             'H': Tolerance('-5%', '+15%'),
             'I': Tolerance('-20%', '0%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'L': Tolerance('15%'),
             'M': Tolerance('20%'),
             'N': Tolerance('30%'),
             'O': Tolerance('20%', '+10%'),
             'P': Tolerance('0%', '+30%'),
             'R': Tolerance('0%', '+20%'),
             'S': Tolerance('0%', '+50%'),
             'T': Tolerance('-10%', '+50%'),
             'U': Tolerance('-10%', '+75%'),
             'V': Tolerance('-10%', '+20%'),
             'Y': Tolerance('-10%', '+150%'),
             'Z': Tolerance('-20%', '+80%')}

voltage = {'0J': '6.3V',
           '1A': '10V',
           '1C': '16V',
           '1E': '25V',
           '1V': '35V',
           '1H': '50V',
           '1J': '63V',
           '2A': '100V',
           '2C': '160V',
           '2D': '200V',
           '2E': '250V',
           '2V': '350V',
           '2G': '400V',
           '2W': '450V'}

case_size_diameter = {'A': '3',
                      'B': '4',
                      'C': '5',
                      'D': '5.5',
                      'E': '6.3',
                      'F': '7.3',
                      'G': '8',
                      '8': '8.2',
                      'H': '10',
                      '9': '10.2',
                      'J': '12',
                      'K': '12.5',
                      'L': '13',
                      'M': '16',
                      'N': '18',
                      '7': '18.5',
                      'P': '20',
                      'Q': '22',
                      'R': '25',
                      'S': '30',
                      'T': '35',
                      'U': '40',
                      'V': '45',
                      'W': '51',
                      'X': '64',
                      'Y': '77',
                      'Z': '90'}

case_size_length = {'05': '5',
                    '07': '7',
                    '09': '9',
                    '10': '10',
                    '1A': '10.5',
                    '11': '11',
                    '1B': '11.5',
                    'BB': '11.5',
                    '12': '12',
                    '1C': '12.5',
                    '13': '13',
                    '14': '14',
                    '15': '15',
                    '16': '16',
                    '17': '17',
                    '18': '18',
                    '20': '20'
                    }


def build_regexpr():
    series_name_group = build_group(series)  # 1
    unknown_1_group = '(P|R)' # 2
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 3
    tolerance_group = build_group(tolerance)  # 4
    voltage_group = build_group(voltage)  # 5
    case_size_diameter_group = build_group(case_size_diameter) # 6
    case_size_length_group = build_group(case_size_length) # 7
    unknown2 = '(M)' # 8
    unknown3 = '(E2)'
    return series_name_group + unknown_1_group + capacitance_group + tolerance_group + voltage_group + \
           case_size_diameter_group + case_size_length_group + unknown2 + unknown3 + '?'


def decode_match(match):
    partname = match.group(1)+match.group(2)+match.group(3)+match.group(4)+match.group(5)+match.group(6) +\
               match.group(7) + match.group(8)
    partname += match.group(9) if match.group(9) is not None else ""
    return Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                     manufacturer="Jamicon",
                     partnumber=partname,
                     series=match.group(1),
                     capacitance=capacitance_string_to_farads(match.group(3)) * Decimal('1000000'),
                     voltage=voltage[match.group(5)],
                     tolerance=tolerance[match.group(4)],
                     dielectric_type="Aluminium oxide",
                     case=case_size_diameter[match.group(6)] + "x" + case_size_length[match.group(7)],
                     note=series[match.group(1)])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
