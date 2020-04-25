from .capacitance import Capacitance
from .tolerance import Tolerance
from enum import Enum


class Capacitor:
    class Type(Enum):
        MLCC = "Multi layer ceramic capacitor"
        ElectrolyticAluminium = "Aluminium Electrolytic Capacitor"

    def __init__(self, capacitor_type, manufacturer, partnumber, series, capacitance, voltage, tolerance, dielectric_type, case, note):
        self.type = capacitor_type
        self.manufacturer = manufacturer
        self.partnumber = partnumber
        self.series = series
        self.capacitance = Capacitance(capacitance)
        self.voltage = voltage
        if isinstance(tolerance, Tolerance):
            self.tolerance = tolerance
        else:
            self.tolerance = Tolerance(tolerance['min'], tolerance['max'])
        self.dielectric_type = dielectric_type
        self.case = case
        self.note = note

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

    def __repr__(self):
        return str(self.manufacturer) + " " + str(self.partnumber) + " " + str(self.series) + " " + str(
            self.capacitance) + " " + str(self.voltage) + " " + str(self.tolerance) + " " + str(
            self.dielectric_type) + " " + str(self.case) + " " + str(self.note)

    def __eq__(self, other):
        return self.manufacturer == other.manufacturer and self.partnumber == other.partnumber and \
               self.series == other.series and self.capacitance == other.capacitance and \
               self.voltage == other.voltage and self.tolerance == other.tolerance and \
               self.dielectric_type == other.dielectric_type and self.case == other.case and self.note == other.note
