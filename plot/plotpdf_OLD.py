#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Convert CSV to a CDF or PDF graph
Author: ILIAS LEONTIADIS

"""

from __future__ import print_function

import csv
import sys

import docopt
import numpy as np
import matplotlib as mpl
mpl.use('Pdf')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *
import itertools

import settings
settings.apply_settings(mpl)

import fileinput

def readcsvcols(col, fileName,  *args, **kwargs):
    out = []
    reader = csv.reader(*args, **kwargs)
    for row in reader:
            try: 
                value = float(row[col])
                #trs = float(row[2])
                out.append(value)
            except:
                #print ("Warning, data format could not be parsed for row: ", row)
                continue
    return out

# Plot

def getCdf(data, numbins=100000, defaultreallimits=None):
    nData = np.array(data)
    nData = nData/60000
    print ("Median:" , np.median(nData))
    print ("Average:", np.average(data))
    n, bins = np.histogram(nData, bins=numbins, range=defaultreallimits)
    cdf = np.cumsum(n)
    scale = 1.0/len(data)
    return bins[:-1], cdf*scale

def getPdf(data, numbins=360, defaultreallimits=None):
    nData = np.array(data)
    n, bins = np.histogram(nData, bins=numbins, range=defaultreallimits)
    #cdf = np.cumsum(n)
    scale = 1.0/len(data)
    return bins[:-1], n*scale

def plotDistribution(data, upperLimit=None, lineStyle= None):
    #get CDF with or without limits
    if upperLimit: 
        bins, cdf = getCdf(data, defaultreallimits=(0, upperLimit))
    else:
         bins, cdf = getCdf(data)
    #plot     
    plt.plot(bins, cdf, ls=lineStyle)

def finalizePlot(pdf, limit = None):
    #setup labels, axis, etc
    plt.legend(['Moving', "Stationary"], loc='lower right')
   
    plt.xlabel("Duration associated to the same tower (min)")
    plt.ylabel("CDF")
    #plt.xscale('log')
    #plt.yscale('log')
    plt.ylim([0,1]) 
    if limit:
        plt.xlim([0,limit]) 
    #plt.grid(True)
    plt.draw()
    plt.show()
    plt.savefig(pdf, format='pdf') # note the format='pdf' argument!
    plt.close()
    pdf.close()



def main():
    maxValue = 300
    column = 0 
    #matplotlib.rcParams.update({'font.size': 18})
    linestyles = ['_', '-', '--', ':']
    for i in range(1, len(sys.argv) -1 ):
    #parse routing file 
        inputFileName = sys.argv[i]
        print ("parsing file: " , inputFileName)
        f = open(inputFileName)
        data =  readcsvcols(column,  inputFileName, f, delimiter=',')

        plotDistribution(data, maxValue, linestyles[i])
    pdf = PdfPages(sys.argv[len(sys.argv)-1])
    finalizePlot(pdf, maxValue)   



#if __name__ == "__main__":
    # Get Data
    #    sys.exit(main())
data = [line for line in fileinput.input()]
