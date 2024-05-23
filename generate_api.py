# SPDX-License-Identifier: Creative Commons 4.0

 #############################################################################
# ~#~ AI Power Measure Sharing ~#~                                            #
# 'Facilitate knowledge sharing and open data in AI's power consumption'      #
# Orange/INNOV/DATA-AI, Orange Innovation Research Program 'Responsible AI'   #
 #############################################################################

#!/usr/bin/python

import os
from services.api_generator import ApiGenerator

HEADER = """
# SPDX-License-Identifier: Creative Commons 4.0

 #############################################################################
# ~#~ AI Power Measure Sharing ~#~                                            #
# 'Facilitate knowledge sharing and open data in AI's power consumption'      #
# Orange/INNOV/DATA-AI, Orange Innovation Research Program 'Responsible AI'   #
 #############################################################################

#!/usr/bin/python
"""

api_gen = ApiGenerator(input_uri=os.sep.join([ '.', 'model' ]))

with open(os.sep.join([ '.', 'api', 'api.py' ]), mode='w', encoding='utf-8') as fp:
    fp.write(api_gen.generate(header=HEADER))



