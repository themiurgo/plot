#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Plot scatter plots.

Prints a scatter plot. It accepts a two field csv input.

Usage:
  plotdensity [DATAFILE ...] [options]

Options:
  -t STR --title=STR          title
  -x STR --xlabel=STR         x axis label [default: X]
  -y STR --ylabel=STR         y axis label [default: Y]
  -b INT --nbins=INT          number of bins
  --logbin                 logarithmic binning
  -ms STR --markerstyle=STR   markerstyle (matplotlib) [default: o]
  -ps STR --plotstyle=STR     plotstyle
  -o FILE --output=FILE       save to file (do not show)
  --xlog                      x logarithmic scale
  --ylog                      y logarithmic scale

Rasterize Options:
  -r --rasterized             Rasterize data points (to speed up rendering
                              of many data points).
  --dpi INT                   Resolution (only has sense when using rasterize)
                              [default: 300]

"""

import csv
import fileinput
import sys

from docopt import docopt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from pylab import *

import settings
from utils import common_settings

if __name__ == "__main__":
    args = docopt(__doc__, version='Plot 0.1')
    sys.argv = [sys.argv[0]] + args['DATAFILE']
    if args['--plotstyle']:
        settings.apply_settings(mpl, args['--plotstyle'])
    finput = fileinput.FileInput(openhook=fileinput.hook_compressed)
    #x, y = zip(*(map(float, row) for row in csv.reader(finput)))
    data = loadtxt(finput, delimiter=",")

    common_settings(args, plt)
    data = data+1
    left, right = min(data[:,0]), max(data[:,0])
    top, bottom = min(data[:,1]), max(data[:,1])
    if not args['--nbins']:
        args['--nbins'] = 1+ np.log2(len(data))
    if args['--logbin']:
        binsx = np.logspace(np.log(left), np.log(right), int(args['--nbins']))
        binsy = np.logspace(np.log(top), np.log(bottom), int(args['--nbins']))
    else:
        bins = np.linspace(left, right, int(args['--nbins']))
    H, xedges, yedges = np.histogram2d(data[:,0], data[:,1], bins=(binsx, binsy))
    extent = [np.log(yedges[0]), np.log(yedges[-1]), np.log(xedges[-1]), np.log(xedges[0])]
    plt.imshow(H, norm=mpl.colors.LogNorm(),
        cmap=cm.hsv,
        interpolation='None',
        #extent = extent,
    )
    colorbar()
    if args['--output']:
        plt.savefig(args['--output'], dpi=int(args['--dpi']))
    else:
        plt.show()

    #clf()
    # title(figtitle)


