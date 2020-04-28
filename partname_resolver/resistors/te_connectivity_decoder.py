from .common import *
from .resistor import Resistor
from partname_resolver.units.resistanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
import re
from decimal import Decimal

series = {'CRGCQ': 'AEC-Q200 compliant Thick Film Chip Resistor'}

resistor_type = {'CRGCQ': Resistor.Type.ThickFilmResistor}

working_temperature_range = {'CRGCQ': TemperatureRange(Decimal('-55'), Decimal('155'))}

temperature_coefficient = {'CRGCQ': lambda
    resistance: "400ppm/K" if resistance <= Decimal('10') else "200ppm/K" if resistance <= Decimal('100') else "100ppm/K"}

size = {'0402': '0402',
        '0603': '0603',
        '0805': '0805',
        '1206': '1206',
        '1210': '1210',
        '2010': '2010',
        '2512': '2512'}

tolerance = {'F': Tolerance('1%'),
             'J': Tolerance('5%')}

max_working_voltage = {'0402': '50V',
                       '0603': '75V',
                       '0805': '150V',
                       '1206': '200V',
                       '1210': '200V',
                       '2010': '200V',
                       '2512': '200V'}

power_rating = {'0402': Decimal('0.0625'),
                '0603': Decimal('0.1'),
                '0805': Decimal('0.125'),
                '1206': Decimal('0.25'),
                '1210': Decimal('0.5'),
                '2010': Decimal('0.75'),
                '2512': Decimal('1')}


def build_regexpr():
    series_group = build_group(series)  # 1
    size_group = build_group(size)  # 2
    tolerance_group = build_group(tolerance)  # 3
    resistance_group = '(\d{2}[RKM]\d{1}|\d{1}[RKM]\d{1,2}|\d{1,3}[RKM])'  # 4
    return series_group + size_group + tolerance_group + resistance_group


def decode_match(match):
    series_name = match.group(1)
    size_name = size[match.group(2)]
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4)
    resistance = resistance_string_to_ohm(match.group(4))
    note = series[series_name] + ", TCR=" + temperature_coefficient[series_name](resistance)
    return Resistor(resistor_type=resistor_type[series_name],
                    manufacturer="TE Connectivity",
                    partnumber=partnumber,
                    working_temperature_range=working_temperature_range[series_name],
                    series=series_name,
                    resistance=resistance,
                    power=power_rating[size_name],
                    max_working_voltage=max_working_voltage[size_name],
                    tolerance=tolerance[match.group(3)],
                    case=size_name,
                    note=note)

def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
