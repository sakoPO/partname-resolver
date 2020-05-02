from enum import Enum
from partname_resolver.units.resistanceTolerance import Tolerance
from partname_resolver.units.inductance import Inductance


class Inductor:
    class Type(Enum):
        MultilayerInductor = "Multilayer Inductor"
        WireWoundInductor = "Wire Wound Inductor"
        FilmInductor = "Film Inductor"

    def __init__(self, inductor_type, manufacturer, partnumber, working_temperature_range, series, inductance,
                 tolerance, q, dc_resistance, rated_current, self_resonant_frequency, max_working_voltage, case, note):
        self.type = inductor_type  # should be moved to components common base class
        self.manufacturer = manufacturer  # should be moved to components common base class
        self.partnumber = partnumber  # should be moved to components common base class
        self.working_temperature_range = working_temperature_range  # should be moved to components common base class
        self.series = series
        self.inductance = Inductance(inductance)
        self.tolerance = tolerance
        self.q = q
        self.dc_resistance = dc_resistance
        self.rated_current = rated_current
        self.self_resonant_frequency = self_resonant_frequency
        self.max_working_voltage = max_working_voltage
        self.case = case
        self.note = note

    def get_description(self):
        prefix = {Inductor.Type.MultilayerInductor: "Inductor",
                  Inductor.Type.WireWoundInductor: "Inductor",
                  Inductor.Type.FilmInductor: "Inductor"}
        if self.type is not None:
            description = prefix[self.type]
        else:
            description = "Inductor"
        description += ' ' + str(self.inductance)
        if isinstance(self.tolerance, Tolerance):
            description += ' ' + str(self.tolerance)
        if self.rated_current is not None:
            description += ' ' + str(self.rated_current)
        if self.dc_resistance is not None:
            description += ' ' + self.dc_resistance
        if self.q is not None:
            description += ' ' + self.q
        if self.working_temperature_range is not None:
            description += ' ' + str(self.working_temperature_range)
        description += ' ' + str(self.case)
        return description

    def __repr__(self):
        working_temperature = ' ' + str(self.working_temperature_range) if self.working_temperature_range is not None else ''
        note = ' ' + self.note if self.note is not None else ''
        return self.manufacturer + " " + self.partnumber + " " + str(self.inductance) + " " + str(self.tolerance) + \
               working_temperature + " " + str(self.case) + note

    def __eq__(self, other):
        return self.type == other.type and self.manufacturer == other.manufacturer and \
               self.partnumber == other.partnumber and \
               self.working_temperature_range == other.working_temperature_range and \
               self.series == other.series and \
               self.inductance == other.inductance and \
               self.tolerance == other.tolerance and \
               self.q == other.q and \
               self.dc_resistance == other.dc_resistance and \
               self.rated_current == other.rated_current and \
               self.self_resonant_frequency == other.self_resonant_frequency and \
               self.max_working_voltage == other.max_working_voltage and \
               self.case == other.case and \
               self.note == other.note
