# -*- coding: utf-8 -*-
"""
Created on Sat May  5 21:40:19 2018

@author: Carmen
"""
from matplotlib.pyplot import *
from numpy import *
from pandas import *
import os

data = read_csv(os.path.join('90_0_1st', 'r_data.csv'), header=None)

x_dots = data.iloc[:,0]
y_dots = data.iloc[:,1]


# x versus y pixel positions
setInfo('$x$ [pixels]','$y$ [pixels]','First rod')
gca().invert_yaxis()
plot(x_dots, y_dots, 'o')
show()


frames = range(1, 900+1)
print(len(frames))

#frames versus x
setInfo('frames ','$x$ [pixels]','First rod')
plot(linspace(1,900,900), x_dots, 'o')
show()

#frames versus y
setInfo('frames ','$y$ [pixels]','First rod')
gca().invert_yaxis()
plot(linspace(1,900,900), y_dots, 'o')
show()