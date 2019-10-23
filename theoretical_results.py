# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 05:12:14 2018

@author: Carmen
"""
import sys
from scipy.integrate import odeint
from matplotlib.pyplot import plot, figure, show
from numpy import sin, cos, pi, linspace, array
from useful_functions import *

#Parameter values: gravity, first mass, second mass, lenght of the first rod 
#and lenght of the second rod
g = 9.81
m_1 = 0.190
m_2 = 0.116
l_1 = 0.29
l_2 = 0.29

#Initial conditions: angle of the first rod, angle of the second rod, angular 
#velocity of the first rod and angular velocity of the second rod. 
theta_1 = pi/2
theta_2 = 0
w_1 = 0
w_2 = 0

#Time (in seconds)
time = linspace(0,21,5000)

#Parameters 
p = [g,m_1/m_2,l_1,l_2]
#Initial conditions
c0 = [theta_1,theta_2,w_1,w_2]


def vectorfield(c, t, p):
    theta_1, theta_2, w_1, w_2 = c
    
    g, m, l_1, l_2 = p
    
    a = ((g/l_1) * sin(theta_2)) - (w_1**2 * sin(theta_1 - theta_2))
    b = ((m + 1) * (g/l_2) * sin(theta_1)) + (w_2**2 * sin(theta_1 - theta_2))
    c = cos(theta_1 - theta_2)
    d = m + (sin(theta_1 - theta_2))**2
    
    f = [w_1, 
         w_2, 
        ((c * a)-((l_2 / l_1) * b)) / d, 
        ((c * b) - ((m+1) * (l_1/l_2) * a)) / d] 
    
    return f

def main(prog_args):
    
    #For each second in the numpy array time, gets the angular velocity 
    #and angular displacement of both rods 
    sol = odeint(vectorfield, c0, time, args=(p,))
    
    #Angular displacements of both rods
    theta_1_array = array([i[0] for i in sol]) 
    theta_2_array = array([i[1] for i in sol])
    
    ###########################################################################
    #                       FIRST-ROD PLOTS
    ###########################################################################
    x = l_1 * sin(theta_1_array) #x coordinates of the 1st mass
    y = l_1 * -1 * cos(theta_1_array) #y coordinates of the 1st mass
    
    #x vs y 
    figure('First rod x vs y')
    plot_info('$x$ [m]','$y$ [m]','First rod')
    plot(x,y)
    show()
    
    #time vs x
    figure('First rod time vs x')
    plot_info('time [s]','$x$ [m]','First rod')
    plot(time,x)
    show()
    
    #time vs y
    figure('First rod time vs y')
    plot_info('time [s]','$y$ [m]','First rod')
    plot(time,y)
    show()
    
    
    ###########################################################################
    #                       SECOND-ROD PLOTS
    ###########################################################################
    x = (l_1 * sin(theta_1_array))+(l_2 * sin(theta_2_array))#x coordinates 2nd mass
    y = (l_1 * -1 * cos(theta_1_array)) + (l_2 * -1 * cos(theta_2_array))#y coordinates 2nd mass
    
    #x vs y
    figure('Second rod x vs y')
    plot_info('$x$ [m]','$y$ [m]','Second rod')
    plot(x,y)
    show()
    
    #time vs x
    figure('Second rod time vs x')
    plot_info('$time$ [s]','$x$ [m]','Second rod')
    plot(time,x)
    show()
    
    #time vs y
    figure('Second rod time vs y')
    plot_info('$time$ [s]','$y$ [m]','Second rod')
    plot(time,y)
    show()
    
    pass
    
if __name__ == "__main__":
    sys.exit(main(sys.argv))