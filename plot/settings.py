from math import sqrt

def apply_settings(matplotlib, stylename):
    if stylename == 'latex':
        fig_width_pt = 246.0  # Get this from LaTeX using \showthe\columnwidth
        inches_per_pt = 1.0/72.27               # Convert pt to inch
        golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
        fig_width = fig_width_pt*inches_per_pt  # width in inches
        fig_height = fig_width*golden_mean      # height in inches
        fig_size =  [fig_width,fig_height]
        params = {'backend': 'ps',
                  'axes.labelsize': 10,
                  'text.fontsize': 10,
                  'legend.fontsize': 10,
                  'xtick.labelsize': 8,
                  'ytick.labelsize': 8,
                  'text.latex.unicode': True,
                  'font.family' : 'serif',
                  'font.serif': 'Times, Palatino, New Century Schoolbook, Bookman, Computer Modern Roman',
                  'text.usetex': True,
                  'figure.autolayout' : True,
                  'figure.figsize': fig_size}
        matplotlib.rcParams.update(params)
