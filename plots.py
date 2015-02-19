# -*- coding: UTF-8 -*-
from pylab import *
import matplotlib.pyplot as p
import pandas as pd
from read_file_bbk import list_textfiles
from collections import Counter


font = {'family': 'Verdana',
        'weight': 'normal'}
rc('font', **font)

def bar_plot(x,y,x_axis,y_axis,label):

    p.bar(x,y)
    p.xlabel(x_axis)
    p.ylabel(y_axis)
    p.title(label)
    p.grid(axis='both')

    plt.show()