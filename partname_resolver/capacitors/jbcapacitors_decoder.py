# http://www.jbcapacitors.com/PartNumber.pdf
from partname_resolver.components.capacitor import Capacitor
from partname_resolver.units.capacitanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
from .common import *
import re

series = {'JRA': 'Radial Aluminum Electrolytic Capacitor',
          'JRB': '',
          'JRC': '',
          'JRD': '',
          'JRG': 'Radial Aluminum Electrolytic Capacitor',
          'JRK': ''}

voltage = {'0E': '2.5V',
           '0G': '4V',
           '0J': '6.3V',
           '1A': '10V',
           '1C': '16V',
           '1E': '25V',
           '1V': '35V',
           '1H': '50V',
           '1J': '63V',
           '1K': '80V',
           '2A': '100V',
           '2C': '160V',
           '2D': '200V',
           '2E': '250V',
           '2F': '315V',
           '2V': '350V',
           '2G': '400V',
           '2W': '450V',
           '2J': '630V',
           '3A': '1000V',
           'MF': '250VAC'}

tolerance = {'B': Tolerance('-0.1pF', '+0.1pF'),
             'C': Tolerance('-0.25pF', '+0.25pF'),
             'D': Tolerance('-0.5pF', '+0.5pF'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'W': Tolerance('-0.05pF', '+0.05pF')}

pitch = {'020': '2.0',
         '025': '2.5',
         '035': '3.5',
         '050': '5.0',
         '075': '7.5'}

lead_length = {'000': 'Standard',
               '040': '4.0',
               '045': '4.5',
               '050': '5.0'}

packing = {'A': 'Ammo',
           'B': 'Bulk'}

special = {'HR': 'Higher Ripple Current'}

operating_temperature_range = {'JRA': lambda voltage: TemperatureRange('-40', '85'),
                               'JRB': lambda voltage: TemperatureRange('-40',
                                                                       '105') if voltage <= 100 else TemperatureRange(
                                   '-25', '105'),
                               'JRC': lambda voltage: TemperatureRange('-55', '105'),
                               'JRD': lambda voltage: TemperatureRange('-55', '105'),
                               'JRG': lambda voltage: TemperatureRange('-40', '105'),
                               'JRK': lambda voltage: TemperatureRange('-40', '105')}


def decode_case(diameter_str, length_str):
    diameter = Decimal(diameter_str) / Decimal(10)
    length = Decimal(length_str) / Decimal(10)
    return str(diameter) + 'x' + str(length) + 'mm'


def build_regexpr():
    series_name_group = build_group(series)  # 1
    voltage_group = build_group(voltage)  # 2
    capacitance_group = '(R\d{2}|\dR\d|\d{3})'  # 3
    tolerance_group = build_group(tolerance)  # 4
    pitch_group = build_group(pitch)  # 5
    diameter = '(\d{4})'  # 6
    length = '(\d{4})'  # 7
    lead_length_group = build_group(lead_length)  # 8
    packing_group = build_group(packing)  # 9
    special_group = build_group(special) + '?'  # 10
    return series_name_group + voltage_group + capacitance_group + tolerance_group + pitch_group + diameter + length + \
           lead_length_group + packing_group + special_group


def decode_match(match):
    partnumber = match.group(1) + match.group(2) + match.group(3) + match.group(4) + match.group(5) + match.group(6) + \
                 match.group(7) + match.group(8) + match.group(9)
    partnumber += match.group(10) if match.group(10) is not None else ''
    series_name = match.group(1)
    voltage_str = voltage[match.group(2)]
    note = series[series_name] + ", Pitch=" + pitch[match.group(5)] + ", Lead length=" + lead_length[match.group(8)] + \
           ", Packing: " + packing[match.group(9)]
    note += special[match.group(10)] if match.group(10) is not None else ''
    return Capacitor(capacitor_type=Capacitor.Type.ElectrolyticAluminium,
                     manufacturer="JB Capacitors Company",
                     partnumber=partnumber,
                     working_temperature_range=operating_temperature_range[series_name](Decimal(voltage_str[:-1])),
                     series=series_name,
                     capacitance=capacitance_string_to_farads(match.group(3)) * Decimal('1000000'),
                     voltage=voltage_str,
                     tolerance=tolerance[match.group(4)],
                     dielectric_type="Aluminium oxide",
                     case=decode_case(match.group(6), match.group(7)),
                     note=note)


def resolve(partname):
    regexpr = build_regexpr()
    match = re.match(regexpr, partname)
    if match:
        return decode_match(match)
