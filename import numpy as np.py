import numpy as np
import scipy.optimize as opt
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from colorsys import hsv_to_rgb as hsv

def line(x, a, b):
    return a + b * x

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}

matplotlib.rc('font', **font)