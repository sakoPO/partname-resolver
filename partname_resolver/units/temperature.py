from decimal import Decimal


class Temperature:
    def __init__(self, temperature):
        if isinstance(temperature, str):
            pass
        else:
            self.temperature = Decimal(temperature)

    def __eq__(self, other):
        return self.temperature == other.temperature

    def __str__(self):
        return str(self.temperature) + u"\u2103"


class TemperatureRange:
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
