from partname_resolver import partname_resolver
from partname_resolver.resistors.resistor import Resistor
from partname_resolver.capacitors.capacitor import Capacitor


def find_capacitor():
    print("----------------- Resolving part GC331AD72W153KX01 -----------------")
    resolved = partname_resolver.resolve('GC331AD72W153KX01')
    if resolved is not None:
        print("Component is capacitor:", isinstance(resolved, Capacitor))
        print("Component is resistor:", isinstance(resolved, Resistor))
        print("Component found:", resolved)
        print("Component type:", resolved.type.value)
        print("Component capacitance:", resolved.capacitance)
        print("Component dielectric type:", resolved.dielectric_type)
        print("Component max voltage", resolved.voltage)


def find_resistor():
    print("----------------- Resolving part CRCW0805562RFKTA -----------------")
    resolved = partname_resolver.resolve('CRCW0805562RFKTA')
    if resolved is not None:
        print("Component is capacitor:", isinstance(resolved, Capacitor))
        print("Component is resistor:", isinstance(resolved, Resistor))
        print("Component found:", resolved)
        print("Component type:", resolved.type.value)
        print("Component resistance", resolved.resistance)
        print("Component max power", resolved.power)
        print("Component max operating voltage", resolved.max_working_voltage)


if __name__ == "__main__":
    find_capacitor()
    find_resistor()