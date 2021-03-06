from . import samsung_decoder, murata_decoder, yaego_decoder, vishay_decoder, \
    nichicon_decoder, kemet_decoder, avx_decoder, samwha_decoder, taiyo_yuden_decoder, aishi_decoder, jamicon_decoder, \
    fenghua_decoder, jbcapacitors_decoder


def resolve(partname):
    component = murata_decoder.resolve(partname)
    if component:
        return component
    component = kemet_decoder.resolve(partname)
    if component:
        return component
    component = samsung_decoder.resolve(partname)
    if component:
        return component
    component = yaego_decoder.resolve(partname)
    if component:
        return component
    component = vishay_decoder.resolve(partname)
    if component:
        return component
    component = nichicon_decoder.resolve(partname)
    if component:
        return component
    component = avx_decoder.resolve(partname)
    if component:
        return component
    component = samwha_decoder.resolve(partname)
    if component:
        return component
    component = taiyo_yuden_decoder.resolve(partname)
    if component:
        return component
    component = aishi_decoder.resolve(partname)
    if component:
        return component
    component = jamicon_decoder.resolve(partname)
    if component:
        return component
    component = fenghua_decoder.resolve(partname)
    if component:
        return component
    component = jbcapacitors_decoder.resolve(partname)
    if component:
        return component
