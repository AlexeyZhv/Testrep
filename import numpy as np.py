import numpy as np
import scipy.optimize as opt
import matplotlib
import matplotlib.pyplot as plt
import pandas
from colorsys import hsv_to_rgb as hsv

def line(x, a, b):
    return a + b * x + 29

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}

matplotlib.rc('font', **font)