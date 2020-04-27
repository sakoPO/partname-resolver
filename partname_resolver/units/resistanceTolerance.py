from decimal import Decimal
from partname_resolver.units.resistance import Resistance


class Tolerance:
    def __init__(self, tolerance_min, tolerance_max=None):
        if tolerance_max is None:
            if tolerance_min.find('%') != -1:
                self.is_relative = True
                self.min = Decimal(tolerance_min.rstrip('%')) * Decimal('-1')
                if self.min > 0:
                    raise ValueError
                self.max = abs(self.min)
            else:
                self.is_relative = False
                self.min = Resistance(tolerance_min)
                self.max = self.min
        else:
            if tolerance_min.find('%') != -1 and tolerance_max.find('%') != -1:
                self.is_relative = True
                self.min = Decimal(tolerance_min.rstrip('%'))
                self.max = Decimal(tolerance_max.rstrip('%'))
            else:
                self.is_relative = False
                if tolerance_min[0] == '-' and tolerance_max[0] == '+':
                    self.min = Resistance(tolerance_min[1:len(tolerance_min)])
                    self.max = Resistance(tolerance_max[1:len(tolerance_max)])
                else:
                    raise ValueError

    def __eq__(self, other):
        return self.is_relative == other.is_relative and self.min == other.min and self.max == other.max

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.is_relative:
            if abs(self.min) == abs(self.max):
                return '\u00B1' + str(abs(self.min)) + "%"
            else:
                return str(self.min) + "%...+" + str(self.max) + "%"
        else:
            if self.min == self.max:
                return '\u00B1' + str(self.min)
            else:
                return "-" + str(self.min) + "...+" + str(self.max)
