# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pysat


def calculate_delta(inst, labels, normalize=False):
    """Calculate the deltas for a list of labels

    Parameters
    ----------
    inst : pysat.Instrument()
        The instrument to attach this function to.
    labels : listlike
        list of labels to calculate delta for
    """

    for label in labels:
        mean_label = '_'.join(('mean', label))
        delta_label = '_'.join(('delta', label))
        norm_label = '_'.join(('delta', label, 'norm'))

        inst[mean_label] = inst[label].rolling(window=60, center=True).mean()
        inst[delta_label] = inst[label] - inst[mean_label]

        if normalize:
            inst[norm_label] = inst[delta_label] / inst[mean_label]

    return


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
