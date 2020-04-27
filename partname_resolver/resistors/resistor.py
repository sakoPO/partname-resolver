from enum import Enum
from .tolerance import Tolerance
from .resistance import Resistance
from .power import Power
from ..units.temperature import Temperature, TemperatureRange

class Resistor:
    class Type(Enum):
        ThinFilmResistor = "Thin Film Resistor"
        ThickFilmResistor = "Thick Film Resistor"
        ThinFilmResistorArray = "Thin Film Resistor Array"
        ThickFilmResistorArray = "Thick Film Resistor Array"

    def __init__(self, resistor_type, manufacturer, partnumber, working_temperature_range, series, resistance,
                 tolerance, power, max_working_voltage, case, note):
        self.type = resistor_type  # should be moved to parts common base class
        self.manufacturer = manufacturer  # should be moved to parts common base class
        self.partnumber = partnumber  # should be moved to parts common base class
        self.working_temperature_range = working_temperature_range  # should be moved to parts common base class
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
        if self.type is not None:
            description = prefix[self.type]
        else:
            description = "Resistor"
        description += ' ' + str(self.resistance)
        if isinstance(self.tolerance, Tolerance):
            description += ' ' + str(self.tolerance)
        if self.power is not None:
            description += ' ' + str(self.power)
        if self.max_working_voltage is not None:
            description += ' ' + self.max_working_voltage
        if self.working_temperature_range is not None:
            description += ' ' + str(self.working_temperature_range)
        description += ' ' + self.case
        return description

    def partial_compare(self, other):
        """This functions compare two resistors but ignores None parameters.
           ie.:
           resistor A:
                - resistance = 100Ohm
                - power = 100mW
                - all other parameters are unknown
           resistor B:
                - resistance = 100Ohm
                - power = 100mW
                - voltage = 25V
                - all other parameters are unknown
           resistor C:
                - resistance = 20Ohm
                - power = 100mW
                - voltage = 25V
                - all other parameters are unknown

            A.partial_compare(B) => True
            B.partial_compare(A) => True
            C.partial_compare(A) => False
            A.partial_compare(C) => False
            """
        if self.type is not None and other.type is not None:
            if self.type != other.type:
                return False
        if self.manufacturer is not None and other.manufacturer is not None:
            if self.manufacturer != other.manufacturer:
                return False
        if self.partnumber is not None and other.partnumber is not None:
            if self.partnumber != other.partnumber:
                return False
        if self.working_temperature_range is not None and other.working_temperature_range is not None:
            if self.working_temperature_range != other.working_temperature_range:
                return False
        if self.series is not None and other.series is not None:
            if self.series != other.series:
                return False
        if self.resistance is not None and other.resistance is not None:
            if self.resistance != other.resistance:
                return False
        if self.tolerance is not None and other.tolerance is not None:
            if self.tolerance != other.tolerance:
                return False
        if self.power is not None and other.power is not None:
            if self.power != other.power:
                return False
        if self.max_working_voltage is not None and other.max_working_voltage is not None:
            if self.max_working_voltage != other.max_working_voltage:
                return False
        if self.case is not None and other.case is not None:
            if self.case != other.case:
                return False
        if self.note is not None and other.note is not None and len(self.note) > 0 and len(other.note) > 0:
            if self.note != other.note:
                return False
        return True

    def __repr__(self):
        series = str(self.series) if self.series is not None else ''
        working_temperature_range = str(self.working_temperature_range) if self.working_temperature_range is not None else ''
        return str(self.manufacturer) + " " + str(self.partnumber) + " " + series + " " + str(
            self.resistance) + " " + str(self.tolerance) + " " + str(self.power) + " " + str(
            self.max_working_voltage) + " " + working_temperature_range + " " + str(self.case) + " " + str(self.note)
