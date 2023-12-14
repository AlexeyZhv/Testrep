import numpy as np
import scipy.optimize as opt
import matplotlib

def line(x, a, b):
    return a + b * x

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}

matplotlib.rc('font', **font)