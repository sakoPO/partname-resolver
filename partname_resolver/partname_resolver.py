from partname_resolver.capacitors import capacitors_partname_decoder
from partname_resolver.resistors import resistors_partname_decoder


def resolve(partname):
    part = capacitors_partname_decoder.resolve(partname)
    if part is not None:
        return part

    part = resistors_partname_decoder.resolve(partname)
    if part is not None:
        return part

