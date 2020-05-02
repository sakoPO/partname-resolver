from decimal import Decimal
from .range_base import RangeBase
from .unit_base import Unit


class Temperature(Unit):
    def __init__(self, temperature):
        super().__init__("Celsius", u"\u2103", Decimal(temperature))




class TemperatureRange(RangeBase):
    def __init__(self, min, max):
        if isinstance(min, Temperature):
            self.min = min
        else:
            self.min = Temperature(min)

        if isinstance(max, Temperature):
            self.max = max
        else:
            self.max = Temperature(max)

    def __eq__(self, other):
        return self.min == other.min and self.max == other.max

    def __str__(self):
        return str(self.min)[:-1] + ".." + str(self.max)

    def __repr__(self):
        return self.__str__()
