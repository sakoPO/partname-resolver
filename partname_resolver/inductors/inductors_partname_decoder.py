from . import murata_decoder, vishay_decoder, kemet_decoder

def resolve(partname):
    component = murata_decoder.resolve(partname)
    if component:
        return component
    component = vishay_decoder.resolve(partname)
    if component:
        return component
    component = kemet_decoder.resolve(partname)
    if component:
        return component
