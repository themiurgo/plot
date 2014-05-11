#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Plot PDF.

Usage:
  plotpdf FILE [options]

Options:
  -t STR --title=STR      title
  -x STR --xlabel=STR     x axis label [default: Values]
  -y STR --ylabel=STR     y axis label [default: CDF]
  -b INT --nbins=INT      number of bins
  -lb --logbin            logarithmic binning

"""

import fileinput

from docopt import docopt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import settings
#settings.apply_settings(mpl)
from utils import common_settings

def histogram(args, data):
    left, right = min(data), max(data)
    if not args['--nbins']:
        args['--nbins'] = 1+ np.log2(len(data))
    if args['--logbin']:
        bins = np.logspace(left, right, args['--nbins'])
    else:
        bins = np.linspace(left, right, args['--nbins'])
    return np.histogram(data, bins=bins, density=True)

if __name__ == "__main__":
    args = docopt(__doc__, version='Plot 0.1')
    finput = fileinput.FileInput(openhook=fileinput.hook_compressed)
    data = [float(i) for i in finput]
    n, bin_edges = histogram(args, data)

    common_settings(args, plt)
    plt.plot(bin_edges[1:], n, 'o')
    plt.show()
