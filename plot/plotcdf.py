#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Plot CDF.

Prints the cumulative density function of input values. It accepts one value
per line.

Usage:
  plotcdf DATAFILE ... [options]

Options:
  -t STR --title=STR       title
  -x STR --xlabel=STR      x axis label [default: Values]
  -y STR --ylabel=STR      y axis label [default: CDF]
  -b INT --nbins=INT       number of bins
  -lb --logbin             logarithmic binning
  -ls STR --linestyle=STR  linestyle (matplotlib) [default: -]
  -o FILE --output=FILE    save to file (do not show)

"""

import fileinput
import sys

from docopt import docopt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import settings
from utils import common_settings
#settings.apply_settings(mpl)

import plotpdf

if __name__ == "__main__":
    args = docopt(__doc__, version='Plot 0.1')
    sys.argv = [sys.argv[0]] + args['DATAFILE']
    finput = fileinput.FileInput(openhook=fileinput.hook_compressed)
    data = [float(i) for i in finput]
    n, bin_edges = plotpdf.histogram(args, data)
    n = np.cumsum(n*np.diff(bin_edges))

    common_settings(args, plt)
    plt.plot(bin_edges[1:], n, args['--linestyle'])
    if args['--output']:
        plt.savefig(args['--output'])
    else:
        plt.show()
