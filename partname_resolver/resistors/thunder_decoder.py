from .common import *
from partname_resolver.components.resistor import Resistor
from partname_resolver.units.resistanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
import re
from decimal import Decimal

series = {'RL': 'Thick Film Chip Resistor'}

resistor_type = {'RL': Resistor.Type.ThickFilmResistor}

working_temperature_range = {'RL': TemperatureRange(Decimal('-55'), Decimal('155'))}

size = {'0402': '0402',
        '0603': '0603',
        '0805': '0805',
        '1206': '1206',
        '1210': '1210',
        '2010': '2010',
        '2512': '2512'}

tolerance = {'F': Tolerance('1%'),
             'J': Tolerance('5%')}

packing = {'07': '7 inch diameter Reel',
           '10': '10 inch diameter Reel',
           '13': '13 inch diameter Reel',
           '7W': '7 inch dia. Reel & 2 x standard power'}

max_working_voltage = {'0402': '50V',
                       '0603': '75V',
                       '0805': '150V',
                       '1206': '200V',
                       '1210': '200V',
                       '2010': '200V',
                       '2512': '200V'}

power_rating_standard = {'0402': Decimal('0.0625'),
                         '0603': Decimal('0.1'),
                         '0805': Decimal('0.125'),
                         '1206': Decimal('0.25'),
                         '1210': Decimal('0.33'),
                         '2010': Decimal('0.75'),
                         '2512': Decimal('1')}

power_rating_high_power = {'0402': Decimal('0.1'),
                           '0603': Decimal('0.125'),
                           '0805': Decimal('0.25'),
                           '1206': Decimal('0.33'),
                           '1210': Decimal('0.5'),
                           '2010': Decimal('1'),
                           '2512': Decimal('2')}

temperature_coefficient_RL_tmp = {'0402': lambda
    resistance: "800ppm/K" if resistance < Decimal(
    '100') else "500ppm/K" if resistance < Decimal('500') else "200ppm/K",
                                  '0603': lambda
                                      resistance: "1200ppm/K" if resistance < Decimal(
                                      '48') else "800ppm/K" if resistance < Decimal(
                                      '100') else "500ppm/K" if resistance < Decimal('500') else "200ppm/K",
                                  '0805': lambda
                                      resistance: "1500ppm/K" if resistance < Decimal(
                                      '19') else "1200ppm/K" if resistance < Decimal(
                                      '48') else "800ppm/K" if resistance < Decimal(
                                      '100') else "500ppm/K" if resistance < Decimal('500') else "200ppm/K",
                                  '1210': lambda
                                      resistance: "1500ppm/K" if resistance < Decimal(
                                      '19') else "800ppm/K" if resistance < Decimal(
                                      '100') else "200ppm/K"
                                  }

temperature_coefficient_RL = {'0402': temperature_coefficient_RL_tmp['0402'],
                              '0603': temperature_coefficient_RL_tmp['0603'],
                              '0805': temperature_coefficient_RL_tmp['0805'],
                              '1206': temperature_coefficient_RL_tmp['0603'],
                              '1210': temperature_coefficient_RL_tmp['1210'],
                              '2010': temperature_coefficient_RL_tmp['1210'],
                              '2512': temperature_coefficient_RL_tmp['1210']
                              }


def build_regexpr():
    series_group = build_group(series)  # 1
    size_group = build_group(size)  # 2
    tolerance_group = build_group(tolerance)  # 3
    unknown = '(K|R)'  # 4
    separator = '(-)'  # 5
    packing_group = build_group(packing)  # 6
    separator2 = '( )'
    resistance_group = '(\d{2}[RKM]\d{1}|\d{1}[RKM]\d{1,2}|\d{1,3}[RKM])'  # 4
    return series_group + size_group + tolerance_group + unknown + separator + packing_group + separator2 + resistance_group


def decode_match(match):
    series_name = match.group(1)
    size_name = size[match.group(2)]
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(5) + match.group(
        6) + match.group(7) + match.group(8)
    resistance = resistance_string_to_ohm(match.group(8))
    note = series[series_name] + ", TCR=" + temperature_coefficient_RL[size_name](resistance)
    return Resistor(resistor_type=resistor_type[series_name],
                    manufacturer="Thunder",
                    partnumber=partnumber,
                    working_temperature_range=working_temperature_range[series_name],
                    series=series_name,
                    resistance=resistance,
                    power=power_rating_high_power[size_name] if match.group(6) == "7W" else power_rating_standard,
                    max_working_voltage=max_working_voltage[size_name],
                    tolerance=tolerance[match.group(3)],
                    case=size_name,
                    note=note)


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
