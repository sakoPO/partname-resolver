# partname-resolver
![Build status](https://travis-ci.com/sakoPO/partname-resolver.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/sakoPO/partname-resolver/badge.svg?branch=master)](https://coveralls.io/github/sakoPO/partname-resolver?branch=master)

Electronic component name resolver 

Simple python 3 script for decoding component parameters from its manufacturer part number.
Designed to work with Capacitors and Resistors.

This script can extract parameters like:
- component type (resistor or capacitor)
- Resistance and tolerance
- Capacitance and tolerance
- Maximal working voltage
- Maximal power dissipation
- Dielectric type
- Component Case


### Supported capacitors series
- Aishi: WH
- AVX: standard product for chip capacitor
- Jamicon: VP, VB, SV, ST, NT, SS, SH, SL, SA, NS, SK, TK, NK, LK
- Kemet:
- Murata: GRT, GCM, GC3, GCJ, GCD, GCE, KCM, KC3, KCA, GCG
- Nichicon: VZ, VR, KA, CS, CY
- Samsung: CL
- Samwha: CA, RC, RD, SD
- Vishay: VJ
- Yaego: CC

