#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Plot scatter plots.

Prints a scatter plot. It accepts a two field csv input.

Usage:
  plotxy [DATAFILE ...] [options]

Options:
  -t STR --title=STR          title
  -x STR --xlabel=STR         x axis label [default: Values]
  -y STR --ylabel=STR         y axis label [default: CDF]
  -ms STR --markerstyle=STR   markerstyle (matplotlib) [default: o]
  -ps STR --plotstyle=STR     plotstyle
  -o FILE --output=FILE       save to file (do not show)

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

import settings
from utils import common_settings

if __name__ == "__main__":
    args = docopt(__doc__, version='Plot 0.1')
    sys.argv = [sys.argv[0]] + args['DATAFILE']
    if args['--plotstyle']:
        settings.apply_settings(mpl, args['--plotstyle'])
    finput = fileinput.FileInput(openhook=fileinput.hook_compressed)
    x, y = zip(*(map(float, row) for row in csv.reader(finput)))

    common_settings(args, plt)
    plt.plot(x, y, args['--markerstyle'], rasterized=args['--rasterized'])
    if args['--output']:
        plt.savefig(args['--output'], dpi=int(args['--dpi']))
    else:
        plt.show()
