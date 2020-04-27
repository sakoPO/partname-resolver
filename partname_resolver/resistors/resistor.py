from enum import Enum
from .tolerance import Tolerance
from .resistance import Resistance
from .power import Power


class Resistor:
    class Type(Enum):
        ThinFilmResistor = "Thin Film Resistor"
        ThickFilmResistor = "Thick Film Resistor"
        ThinFilmResistorArray = "Thin Film Resistor Array"
        ThickFilmResistorArray = "Thick Film Resistor Array"

    def __init__(self, resistor_type, manufacturer, partnumber, series, resistance, tolerance, power,
                 max_working_voltage, case, note):
        self.type = resistor_type  # should be moved to parts common base class
        self.manufacturer = manufacturer  # should be moved to parts common base class
        self.partnumber = partnumber  # should be moved to parts common base class
        self.series = series
        self.resistance = Resistance(resistance)
        self.tolerance = tolerance
        self.power = Power(power) if power is not None else None
        self.max_working_voltage = max_working_voltage
        self.case = case
        self.note = note

    def get_description(self):
        prefix = {Resistor.Type.ThinFilmResistor: "Resistor",
                  Resistor.Type.ThickFilmResistor: "Resistor",
                  Resistor.Type.ThinFilmResistorArray: "Resistor array",
                  Resistor.Type.ThickFilmResistorArray: "Resistor array"}
        description = prefix[self.type]
        description += ' ' + str(self.resistance)
        if isinstance(self.tolerance, Tolerance):
            description += ' ' + str(self.tolerance)
        if self.power is not None:
            description += ' ' + str(self.power)
        if self.max_working_voltage is not None:
            description += ' ' + self.max_working_voltage + 'V'
        description += ' ' + self.case
        return description

    def __repr__(self):
        return str(self.manufacturer) + " " + str(self.partnumber) + " " + str(self.series) + " " + str(
            self.resistance) + " " + str(self.tolerance) + " " + str(self.power) + " " + str(
            self.max_working_voltage) + " " + str(self.case) + " " + str(self.note)
