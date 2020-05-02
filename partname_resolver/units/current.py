from .unit_base import Unit
from decimal import Decimal


class Current(Unit):
    def __init__(self, current):
        if isinstance(current, Decimal):
            amps = current
        elif isinstance(current, str):
            amps = self.__convert_str_to_decimal_value(current, 'A')
        else:
            print(current)
            raise TypeError(current)
        super().__init__("Ampre",  'A', amps)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == self.__convert_str_to_decimal_value(other, 'A')
        if isinstance(other, Current):
            return self.value == other.value




