from partname_resolver.units.capacitanceTolerance import Tolerance
from partname_resolver.case.chip import Chip
from partname_resolver.units.length import Dimmension, Length, LengthTolerance

tolerance = {'F': Tolerance('1%'),
             'G': Tolerance('2%'),
             'J': Tolerance('5%'),
             'K': Tolerance('10%'),
             'M': Tolerance('20%'),
             'N': Tolerance('30%')}

dimensions = {'02': Chip('01005', T=Dimmension('0.2mm', LengthTolerance('0.02mm'))),
              '03': Chip('0201', T=Dimmension('0.3mm', LengthTolerance('0.03mm'))),
              '04': '',
              '15': Chip('0402', T=Dimmension('0.5mm', LengthTolerance('0.05mm'))),
              '18': Chip('0603', T=Dimmension('0.8mm', LengthTolerance('0.15mm'))),
              '21': Chip('0805', L=Length('2mm'), W=Length('1.25mm')),
              '2A': Chip('0804'),
              '2B': Chip('0805', L=Length('2mm'), W=Length('1.5mm')),
              '2M': '',
              '2U': Chip('1008'),
              '2H': '',
              '3N': '',
              '31': Chip('1206'),
              '32': Chip('1210'),
              '41': Chip('1806'),
              '43': '',
              '44': '',
              '5B': Chip('2020'),
              '55': '',
              '66': ''}

package = {'B': 'Bulk',
           'E': 'ø180mm Embossed Taping',
           'F': 'ø330mm Embossed Taping',
           'L': 'ø180mm Embossed Taping',
           'D': 'ø180mm Paper Taping',
           'W': 'ø180mm Paper Taping',
           'K': 'ø330mm Embossed Taping',
           'J': 'ø330mm Paper Taping',
           '#': 'Unknown package'}

