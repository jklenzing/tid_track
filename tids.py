# -*- coding: utf-8 -*-
"""Quick and simple view of TIDS in DE2 data."""

import pysat

from funcs import calculate_delta

lang = pysat.Instrument('de2', 'lang', use_header=True, strict_time_flag=False)
lang.custom_attach(calculate_delta,
                   kwargs={'labels': ['plasmaDensity'],
                           'normalize': True})

nacs = pysat.Instrument('de2', 'nacs', use_header=True)
nacs.custom_attach(calculate_delta,
                   kwargs={'labels': ['O_density', 'N2_density'],
                           'normalize': True})

lang.load(1983, 22)
nacs.load(1983, 22)
