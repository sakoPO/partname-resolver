from . import royal_ohm_decode
from . import yaego_decoder
from . import vishay_decoder
from . import bourns_decoder


def resolve(partname):
    component = vishay_decoder.resolve(partname)
    if component:
        return component
    component = royal_ohm_decode.resolve(partname)
    if component:
        return component
    component = yaego_decoder.resolve(partname)
    if component:
        return component
    component = bourns_decoder.resolve(partname)
    if component:
        return component
