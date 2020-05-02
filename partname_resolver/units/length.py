from decimal import Decimal
from .unit_base import Unit
import re


class Length(Unit):
    def __init__(self, length):
        if isinstance(length, str):
            if length.find("mm") != -1:
                self.length = Decimal(length.replace("mm", "")) / Decimal('1000')
            else:
                raise ValueError
        else:
            self.length = length
        super().__init__("Length", 'm', self.length)
        self.str_conversion_prefixes = ['m', '-', 'k']


class LengthTolerance:
    def __init__(self, min, max=None):
        if max==None:
            self.is_relative = False
            self.min = min if isinstance(min, Length) else Length(min)
            self.max = self.min
        else:
            self.is_relative = False
            self.min = min if isinstance(min, Length) else Length(min)
            self.max = max if isinstance(min, Length) else Length(min)

    def __str__(self):
        if self.min == self.max:
            return '\u00B1' + str(self.min)
        else:
            return "Error"

    def __eq__(self, other):
        return self.min == other.min and self.max == other.max


class Dimmension:
    def __init__(self, length, tolerance):
        if not isinstance(tolerance, LengthTolerance):
            raise ValueError
        self.length = length if isinstance(length, Length) else Length(length)
        self.tolerance = tolerance

    def __str__(self):
        return str(self.length)[:-2] + str(self.tolerance)

    def __eq__(self, other):
        return self.length == other.length and self.tolerance == other.tolerance
