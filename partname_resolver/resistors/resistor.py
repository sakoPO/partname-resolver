from enum import Enum


class Resistor:
    class Type(Enum):
        ThinFilmResistor = "Thin Film Resistor"
        ThickFilmResistor = "Thick Film Resistor"
        ThinFilmResistorArray = "Thin Film Resistor Array"
        ThickFilmResistorArray = "Thick Film Resistor Array"

    def __init__(self, resistor_type, manufacturer, partnumber, series, resistance, tolerance, power,
                 max_working_voltage, case, note):
        self.type = resistor_type
        self.manufacturer = manufacturer
        self.partnumber = partnumber
        self.series = series
        self.resistance = resistance
        self.tolerance = tolerance
        self.power = power
        self.max_working_voltage = max_working_voltage
        self.case = case
        self.note = note

    def __repr__(self):
        return str(self.manufacturer) + " " + str(self.partnumber) + " " + str(self.series) + " " + str(
            self.resistance) + " " + str(self.tolerance) + " " + str(self.power) + " " + str(
            self.max_working_voltage) + " " + str(self.case) + " " + str(self.note)


def ohms_to_string(ohms):
    mul = {'G': 1000000000,
           'M': 1000000,
           'k': 1000,
           'R': 1,
           'm': 0.001,
           'u': 0.000001,
           'n': 0.000000001,
           'p': 0.000000000001,
           'f': 0.000000000000001}
    for key in mul.keys():
        unit = mul[key]
        if ohms >= unit and ohms <= 1000*unit:
            return str(ohms / unit).rstrip('0').rstrip('.') + str(key)
