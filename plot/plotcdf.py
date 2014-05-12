#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Plot CDF.

Prints the cumulative density function of input values. It accepts one value
per line.

Usage:
  plotcdf [DATAFILE ...] [options]

Options:
  -t STR --title=STR       title
  -x STR --xlabel=STR      x axis label [default: Values]
  -y STR --ylabel=STR      y axis label [default: CDF]
  -b INT --nbins=INT       number of bins
  -lb --logbin             logarithmic binning
  -ls STR --linestyle=STR  linestyle (matplotlib) [default: -]
  -ps STR --plotstyle=STR  plotstyle
  -o FILE --output=FILE    save to file (do not show)
  --xlog                   x logarithmic scale
  --ylog                   y logarithmic scale
  -r --rasterized          rasterize data points (to speed up rendering of many data points).
  --dpi=INT                resolution (only has sense when using rasterize) [default: 300]

"""

import fileinput
import sys

from docopt import docopt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import settings
from utils import common_settings

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
    plt.plot(bin_edges[1:], n, args['--linestyle'], rasterized=args['--rasterized'])
    if args['--output']:
        plt.savefig(args['--output'])
        plt.savefig(args['--output'], dpi=int(args['--dpi']))
    else:
        plt.show()
