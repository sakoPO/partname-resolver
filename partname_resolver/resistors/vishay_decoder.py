from .common import *
from .resistor import Resistor
from .tolerance import Tolerance
from ..units.temperature import TemperatureRange
import re
from decimal import Decimal

series = {'CRCW': 'Lead (Pb)-Bearing Thick Film, Rectangular Chip Resistors',
          'PAT': 'Precision Automotive Thin Film Chip Resistors,AEC-Q200 Qualified, 2 kV ESD Rating',
          'PNM': 'Precision Thin Film Non-Magnetic Resistor,Surface Mount Chip, ± 25 ppm/°C, Tolerances to 0.1 %',
          'TNPW': 'High Stability Thin Film Flat Chip Resistors'}

resistor_type = {'CRCW': Resistor.Type.ThickFilmResistor,
                 'PAT': Resistor.Type.ThinFilmResistor,
                 'PNM': Resistor.Type.ThinFilmResistor,
                 'TNPW': Resistor.Type.ThinFilmResistor}

size = {'0201': '0201',
        '0402': '0402',
        '0603': '0603',
        '0805': '0805',
        '0508': '0508',
        '1206': '1206',
        '0612': '0612',
        '1210': '1210',
        '1812': '1812',
        '1218': '1218',
        '2010': '2010',
        '1020': '1020',
        '2512': '2512',
        '1225': '1225'}

tolerance = {'B': Tolerance('0.1%'),
             'C': Tolerance('0.25%'),
             'D': Tolerance('0.5%'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'Z': Tolerance('0%')}

temperature_coefficient = {'Y': '10ppm/K',
                           'X': '15ppm/K',
                           'E': '25ppm/K',
                           'H': '50ppm/K',
                           'K': '100ppm/K',
                           'L': '200ppm/K',
                           'N': '200ppm/K',
                           'S': 'Jumper or special'}

packing_type = {'T0': '100 min., 100 mult',
                'T1': '1000 min., 1000 mult',
                'T3': '300 min., 300 mult',
                'T5': '500 min., 500 mult',
                'TS': '100 min., 1 mult.',
                'TI': '',
                'TP': '',
                'TA': '',
                'TB': '',
                'TC': '',
                'TD': '',
                'TE': '',
                'TF': 'full reel',
                'TG': '',
                'TH': '',
                'TK': '',
                'EA': '',
                'EB': '',
                'EC': '',
                'ED': '',
                'EE': '',
                'EF': '',
                'EG': '',
                'EH': '',
                'EI': '',
                'EL': '',
                'EK': '',
                'EP': '',
                'EN': ''}

packing_type_TNPWe3 = ['ED', 'EP', 'EI', 'EN', 'EA', 'EC']

special = {'P': 'Semi-Precision',
           'BC': 'Unknown'}

termination = {'B': 'wraparound Sn/Pb solder63 % Sn/ 37 % Pb',
               'S': 'wraparound lead (Pb)-free solder w/nickel barrier'}

max_working_voltage_CRCW = {'0402': '50V',
                            '0603': '75V',
                            '0805': '150V',
                            '1206': '200V',
                            '1210': '200V',
                            '1218': '200V',
                            '2010': '200V',
                            '2512': '200V'}

max_working_voltage_TNPW = {'0201': '25V',
                            '0402': '50V',
                            '0603': '75V',
                            '0805': '150V',
                            '1206': '200V',
                            '1210': '200V',
                            '2010': '300V',
                            '2512': '300V'}

max_working_voltage_PAT = {'0402': '75V',
                           '0603': '75V',
                           '0805': '100V',
                           '1206': '200V',
                           '1505': '150V',
                           '2208': '150V',
                           '2010': '200V',
                           '2512': '200V'}

max_working_voltage_PNM = {'0402': '75V',
                           '0502': '75V',
                           '0505': '75V',
                           '0603': '75V',
                           '0805': '100V',
                           '0705': '100V',
                           '1005': '100V',
                           '1010': '150V',
                           '1206': '200V',
                           '1505': '150V',
                           '2208': '150V',
                           '2010': '200V',
                           '2512': '200V'}

max_working_voltage = {'CRCW': max_working_voltage_CRCW,
                       'PAT': max_working_voltage_PAT,
                       'PNM': max_working_voltage_PNM,
                       'TNPW': max_working_voltage_TNPW,
                       'TNPWe3': max_working_voltage_TNPW}

power_CRCW = {'0402': Decimal('0.063'),  # 1/16W
              '0603': Decimal('0.1'),
              '0805': Decimal('0.125'),
              '1206': Decimal('0.25'),
              '1210': Decimal('0.5'),
              '1218': Decimal('1'),
              '2010': Decimal('0.75'),
              '2512': Decimal('1')}

power_PAT = {'0402': Decimal('0.050'),
             '0603': Decimal('0.150'),
             '0805': Decimal('0.200'),
             '1206': Decimal('0.400'),
             '1505': Decimal('0.400'),
             '2208': Decimal('0.750'),
             '2010': Decimal('0.8'),
             '2512': Decimal('1')}

power_PNM = {'0402': Decimal('0.050'),
             '0502': Decimal('0.100'),
             '0505': Decimal('0.150'),
             '0603': Decimal('0.150'),
             '0805': Decimal('0.200'),
             '0705': Decimal('0.200'),
             '1005': Decimal('0.250'),
             '1010': Decimal('0.500'),
             '1206': Decimal('0.400'),
             '1505': Decimal('0.400'),
             '2208': Decimal('0.750'),
             '2010': Decimal('0.8'),
             '2512': Decimal('1')}

power_TNPW = {'0402': Decimal('0.063'),  # 1/16W
              '0603': Decimal('0.1'),
              '0805': Decimal('0.125'),
              '1206': Decimal('0.25'),
              '1210': Decimal('0.33'),
              '2010': Decimal('0.4'),
              '2512': Decimal('0.5')}

power_TNPW_e3 = {'0201': Decimal('0.075'),
                 '0402': Decimal('0.1'),
                 '0603': Decimal('0.125'),
                 '0805': Decimal('0.200'),
                 '1206': Decimal('0.400'),
                 '1210': Decimal('0.500')}

power = {'CRCW': power_CRCW,
         'PAT': power_PAT,
         'PNM': power_PNM,
         'TNPW': power_TNPW,
         'TNPWe3': power_TNPW_e3}


def build_regexpr_PAT_PNM():
    series_group = '(PAT|PNM)'  # 1
    size_group = build_group(size)  # 2
    temperature_coefficient_group = build_group(temperature_coefficient)  # 3
    resistance_group = '(\d{4}|\d{2}[RKM]\d{1}|\d{1}[RKM]\d{2}|\d{3}[RKM])'  # 4
    tolerance_group = build_group(tolerance)  # 5
    termination_group = build_group(termination)  # 6
    packing_type_group = build_group(packing_type)  # 7
    return series_group + size_group + temperature_coefficient_group + resistance_group + tolerance_group + \
           termination_group + packing_type_group + '?'


def decode_match_PAT_PNM(match):
    series_name = match.group(1)
    return Resistor(resistor_type=resistor_type[match.group(1)],
                    manufacturer="Vishay",
                    partnumber=match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(
                        5) + match.group(6) + match.group(7),
                    working_temperature_range=TemperatureRange(Decimal('-55'), Decimal('155')),
                    series=series_name,
                    resistance=resistance_string_to_ohm(match.group(4)),
                    power=power[series_name][match.group(2)],
                    max_working_voltage=max_working_voltage[series_name][match.group(2)],
                    tolerance=tolerance[match.group(5)],
                    case=size[match.group(2)],
                    note=series[series_name])


def build_regexpr():
    series_group = build_group(series)  # 1
    size_group = build_group(size)  # 2
    resistance_group = '(\d{2}[RKM]\d{1}|\d{1}[RKM]\d{2}|\d{3}[RKM])'  # 3
    tolerance_group = build_group(tolerance)  # 4
    temperature_coefficient_group = build_group(temperature_coefficient)  # 5
    packing_type_group = build_group(packing_type)  # 6
    special_group = build_group(special)  # 7

    return series_group + size_group + resistance_group + tolerance_group + temperature_coefficient_group + \
           packing_type_group + special_group + '?'


def decode_match(match):
    series_name = match.group(1)
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(5) + match.group(6)
    partnumber += match.group(7) if match.group(7) is not None else ''
    is_e3 = 'e3' if series_name == "TNPW" and match.group(6) in packing_type_TNPWe3 else ''
    return Resistor(resistor_type=resistor_type[match.group(1)],
                    manufacturer="Vishay",
                    partnumber=partnumber,
                    series=series_name,
                    working_temperature_range=TemperatureRange(Decimal('-55'), Decimal('155')),
                    resistance=resistance_string_to_ohm(match.group(3)),
                    power=power[series_name + is_e3][match.group(2)],
                    max_working_voltage=max_working_voltage[series_name + is_e3][match.group(2)],
                    tolerance=tolerance[match.group(4)],
                    case=size[match.group(2)],
                    note=series[series_name])


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)

    regexpr = build_regexpr_PAT_PNM()
    match = re.match(regexpr, partname)
    if match:
        return decode_match_PAT_PNM(match)
