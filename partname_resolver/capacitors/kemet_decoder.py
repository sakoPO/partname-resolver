# http://www.kemet.com/Lists/FileStore/f2097g.pdf
from .common import capacitance_string_to_farads
from .capacitor import Capacitor
from partname_resolver.units.capacitanceTolerance import Tolerance
from ..units.temperature import TemperatureRange
import re
from decimal import Decimal

tolerance = {'B': Tolerance('0.10pF'),
             'C': Tolerance('0.25pF'),
             'D': Tolerance('0.5pF'),
             'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%')}

operating_temperature_range = {'B': TemperatureRange('-55', '125'),
                               'C': TemperatureRange('-55', '125'),
                               'D': TemperatureRange('-55', '125'),
                               'F': TemperatureRange('-55', '125'),
                               'G': TemperatureRange('-55', '125'),
                               'J': TemperatureRange('-55', '125'),
                               'K': TemperatureRange('-55', '125'),
                               'M': TemperatureRange('-55', '125')}


def kemet(partname):
    voltage = {'9': '6.3V', '8': '10V', '4': '16V', '3': '25V', '6': '35V', '5': '50V', '1': '100V', '2': '200V',
               'A': '250V'}

    match = re.match(
        r'(C)(0201|0402|0603|0805|1206|1210|1808|1812|1825|2220|2225)(C)(\d{3})(B|C|D|F|G|J|K|M)(8|4|3|5|1|2|A)(G)',
        partname)

    def capacitanceStringToFarads_kamet(string):
        value = Decimal(string[:2])
        mul = Decimal(string[2])
        if mul == Decimal(8):
            return value / Decimal(100) * Decimal(10 ** -12)
        if mul == Decimal(9):
            return value / Decimal(10) * Decimal(10 ** -12)
        return value * Decimal('10') ** mul * Decimal('10') ** Decimal('-12')

    if match:
        return Capacitor(capacitor_type=Capacitor.Type.MLCC,
                         manufacturer="Kemet",
                         partnumber=partname,
                         working_temperature_range=operating_temperature_range[match.group(5)],
                         series=match.group(1),
                         capacitance=capacitanceStringToFarads_kamet(match.group(4)),
                         voltage=voltage[match.group(6)],
                         tolerance=tolerance[match.group(5)],
                         dielectric_type='C0G',
                         case=match.group(2),
                         note='Standard')
    #        component = {}
    #        component['series'] = 'C - Standard'
    #        component['Case'] = match.group(2)
    #        component['Dielectric Type'] = 'C0G'
    #        component['Voltage'] = voltage[match.group(6)]
    # component['Capacitance'] = capacitor.farads_to_string(capacitanceStringToFarads_kamet(match.group(4)))
    #        component['Capacitance'] = capacitanceStringToFarads_kamet(match.group(4))
    #        component['Tolerance'] = tolerance[match.group(5)]
    #        component['Manufacturer'] = 'Kemet'
    #        return component

    match = re.match(
        r'(C)(0201|0402|0603|0805|1206|1210|1808|1812|1825|2220|2225)(C)(\d{3})(J|K|M)(9|8|4|3|6|5|1|2|A)(R)', partname)
    if match:
        return Capacitor(capacitor_type=Capacitor.Type.MLCC,
                         manufacturer="Kemet",
                         partnumber=partname,
                         working_temperature_range=operating_temperature_range[match.group(5)],
                         series=match.group(1),
                         capacitance=capacitanceStringToFarads_kamet(match.group(4)),
                         voltage=voltage[match.group(6)],
                         tolerance=tolerance[match.group(5)],
                         dielectric_type='X7R',
                         case=match.group(2),
                         note='Standard')


#        component = {}
#        component['series'] = 'C - Standard'
#        component['Case'] = match.group(2)
#        component['Dielectric Type'] = 'X7R'
#        component['Voltage'] = voltage[match.group(6)]
# component['Capacitance'] = capacitor.farads_to_string(capacitanceStringToFarads(match.group(4)))
#        component['Capacitance'] = capacitanceStringToFarads_kamet(match.group(4))
#        component['Tolerance'] = tolerance[match.group(5)]
#        component['Manufacturer'] = 'Kemet'
#        return component


def resolve(partname):
    part = kemet(partname)
    if part:
        return part
