from partname_resolver.units.capacitance import Capacitance, CapacitanceRange
from partname_resolver.units.capacitanceTolerance import Tolerance
from enum import Enum


class Capacitor:
    class Type(Enum):
        MLCC = "MLCC"
        ElectrolyticAluminium = "Aluminium Electrolytic Capacitor"
        ElectrolyticTantalum = "Tantalum Capacitor"
        CeramicTrimmer = "Ceramic Trimmer"
        MonoliticCapacitor = "Monolitic Capacitor"
        CeramicCapacitor = "Ceramic Capacitor"

    def __init__(self, capacitor_type, manufacturer, partnumber, working_temperature_range, series, capacitance,
                 voltage, tolerance, dielectric_type, case, note):
        self.type = capacitor_type  # should be moved to parts common base class
        self.manufacturer = manufacturer  # should be moved to parts common base class
        self.partnumber = partnumber  # should be moved to parts common base class
        self.working_temperature_range = working_temperature_range  # should be moved to parts common base class
        self.series = series
        if isinstance(capacitance, CapacitanceRange):
            self.capacitance = capacitance
        else:
            self.capacitance = Capacitance(capacitance)
        self.voltage = voltage
        if isinstance(tolerance, Tolerance):
            self.tolerance = tolerance
        elif tolerance is None:
            self.tolerance = "Missing tolerance parameter"
        else:
            self.tolerance = Tolerance(tolerance['min'], tolerance['max'])
        self.dielectric_type = dielectric_type
        self.case = case
        self.note = note

    def get_description(self):
        prefix = {Capacitor.Type.MLCC: "Capacitor MLCC",
                  Capacitor.Type.ElectrolyticAluminium: "Capacitor Electrolytic",
                  Capacitor.Type.ElectrolyticTantalum: "Capacitor Tantalum",
                  Capacitor.Type.CeramicTrimmer: "Capacitor Ceramic Trimmer",
                  Capacitor.Type.MonoliticCapacitor: "Capacitor Monolithic",
                  Capacitor.Type.CeramicCapacitor: "Ceramic Capacitor"
                  }
        description = prefix[self.type]
        description += ' ' + str(self.capacitance)
        if isinstance(self.tolerance, Tolerance):
            description += ' ' + str(self.tolerance)
        if self.voltage is not None:
            description += ' ' + str(self.voltage)
        if self.dielectric_type is not None:
            description += ' ' + self.dielectric_type
        if self.working_temperature_range is not None:
            description += ' ' + str(self.working_temperature_range)
        if self.case is not None:
            description += ' ' + self.case
        return description

    def from_dict(self, dictionary):
        self.manufacturer = dictionary["Manufacturer"]
        self.partnumber = dictionary["Partnumber"]
        self.series = dictionary["Series"]
        self.capacitance = Capacitance(dictionary["Capacitance"])
        self.voltage = dictionary["Voltage"]
        self.tolerance = dictionary["Tolerance"]
        self.dielectric_type = dictionary["Dielectric Type"]
        self.case = dictionary["Case"]
        self.note = dictionary["Note"]

    def to_dict(self):
        component = {'Series': self.series,
                     'Note': self.note,
                     'Case': self.case,
                     'Height': '',
                     'Dielectric Type': self.dielectric_type,
                     'Voltage': self.voltage,
                     'Capacitance': str(self.capacitance),
                     'Tolerance': str(self.tolerance),
                     'Manufacturer': self.manufacturer}
        return component

    def to_json(self):
        pass

    def to_str(self):
        pass

    def partial_compare(self, other, debug=False):
        """This functions compare two capacitors but ignores None parameters.
           ie.:
           capacitor A:
                - capacitance = 1nF
                - voltage = 20V
                - all other parameters are unknown
           capacitor B:
                - capacitance = 1nF
                - voltage = 20V
                - tolerance = 10%
                - all other parameters are unknown
           capacitor C:
                - capacitance = 2nF
                - voltage = 20V
                - tolerance = 10%
                - all other parameters are unknown

            A.partial_compare(B) => True
            B.partial_compare(A) => True
            C.partial_compare(A) => False
            A.partial_compare(C) => False
            """
        if self.type is not None and other.type is not None:
            if self.type != other.type:
                if debug:
                    print("type mismatch")
                return False
        if self.manufacturer is not None and other.manufacturer is not None:
            if self.manufacturer.casefold() != other.manufacturer.casefold():
                if debug:
                    print("manufacturer mismatch")
                return False
        if self.partnumber is not None and other.partnumber is not None:
            if self.partnumber != other.partnumber:
                if debug:
                    print("partnumber mismatch")
                return False
        if self.working_temperature_range is not None and other.working_temperature_range is not None:
            if self.working_temperature_range != other.working_temperature_range:
                if debug:
                    print("Temperature range mismatch")
                return False
        if self.series is not None and other.series is not None:
            if self.series != other.series:
                if debug:
                    print("series mismatch")
                return False
        if self.capacitance is not None and other.capacitance is not None:
            if self.capacitance != other.capacitance:
                if debug:
                    print("capacitance mismatch")
                return False
        if self.voltage is not None and other.voltage is not None:
            if self.voltage != other.voltage:
                if debug:
                    print("voltage mismatch")
                return False
        if self.tolerance is not None and other.tolerance is not None:
            if self.tolerance != other.tolerance:
                if debug:
                    print("tolerance mismatch")
                return False
        if self.dielectric_type is not None and other.dielectric_type is not None:
            if self.dielectric_type != other.dielectric_type:
                if debug:
                    print("dielectric mismatch")
                return False
        if self.case is not None and other.case is not None:
            if self.case != other.case:
                if debug:
                    print("Case mismatch: ", self.case, " != ", other.case)
                return False
        if self.note is not None and other.note is not None and len(self.note) > 0 and len(other.note) > 0:
            if self.note != other.note:
                if debug:
                    print("note mismatch")
                return False
        return True

    def __repr__(self):
        working_temperature_range = str(
            self.working_temperature_range) + " " if self.working_temperature_range is not None else ''
        return str(self.manufacturer) + " " + str(self.partnumber) + " " + str(self.series) + " " + str(
            self.capacitance) + " " + str(self.voltage) + " " + str(self.tolerance) + " " + str(
            self.dielectric_type) + " " + working_temperature_range + str(self.case) + " " + str(self.note)

    def __eq__(self, other):
        return self.manufacturer == other.manufacturer and self.partnumber == other.partnumber and \
               self.series == other.series and self.capacitance == other.capacitance and \
               self.voltage == other.voltage and self.tolerance == other.tolerance and \
               self.dielectric_type == other.dielectric_type and self.case == other.case and \
               self.note == other.note and self.working_temperature_range == other.working_temperature_range
