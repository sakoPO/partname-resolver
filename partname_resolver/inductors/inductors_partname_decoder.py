from . import murata_decoder

def resolve(partname):
    component = murata_decoder.resolve(partname)
    if component:
        return component
