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

"""

import fileinput

from docopt import docopt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import settings
from utils import common_settings
#settings.apply_settings(mpl)

if __name__ == "__main__":
    args = docopt(__doc__, version='Plot 0.1')
    finput = fileinput.FileInput(openhook=fileinput.hook_compressed)
    data = [float(i) for i in finput]
    if not args['--nbins']:
        args['--nbins'] = 1+ np.log2(len(data))
    n, bins = np.histogram(data, bins=args['--nbins'], normed=True)
    n = np.cumsum(n*np.diff(bins))

    common_settings(args, plt)
    plt.plot(bins[1:], n, 'o')
    plt.show()
