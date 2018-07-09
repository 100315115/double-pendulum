# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 05:12:14 2018

@author: Carmen
"""
from scipy.integrate import odeint
from matplotlib.pyplot import plot, show
from numpy import sin, cos, pi, linspace, array

def vectorfield(c, t, p):
    theta_1, theta_2, w_1, w_2 = c
    
    g, m, l_1, l_2 = p
    
    a = ((g/l_1)*sin(theta_2)) - (w_1**2 * sin(theta_1 - theta_2))
    b = ((m + 1)*(g/l_2)*sin(theta_1)) + (w_2**2 * sin(theta_1 - theta_2))
    c = cos(theta_1 - theta_2)
    d = m + (sin(theta_1 - theta_2))**2
    
    f = [w_1, 
         w_2, 
        ((c*a)-((l_2/l_1)*b))/d, 
        ((c*b)-((m+1)*(l_1/l_2)*a))/d] 
    
    return f

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

#For each second specified by the numpy array time, gets the angular velocity 
#and angular displacement of both rods 
sol = odeint(vectorfield, c0, time, args=(p,))

#Angular displacements of both rods
theta_1_array = array([i[0] for i in sol]) 
theta_2_array = array([i[1] for i in sol])


#Theoretical data plots:

#setInfo('time [s]','$\theta_1$ [rad]','First rod')
#plot(time,theta_1_array)
#show()


#setInfo('time [s]','$\theta_2$ [rad]','Second rod')
#plot(time,theta_2_array)
#show()


#First-rod plots---------------------------------------------------------------
x = l_1*sin(theta_1_array) #x positions of the 1st mass
y = l_1*-1*cos(theta_1_array) #y positions of the 1st mass

#x vs y 
setInfo('$x$ [m]','$y$ [m]','First rod')
plot(x,y)
show()

#time vs x
setInfo('time [s]','$x$ [m]','First rod')
plot(time,x)
show()

#time vs y
setInfo('time [s]','$y$ [m]','First rod')
plot(time,y)
show()



#Second-rod plots--------------------------------------------------------------
x = (l_1*sin(theta_1_array))+(l_2*sin(theta_2_array))#x positions 2nd mass
y = (l_1*-1*cos(theta_1_array))+(l_2*-1*cos(theta_2_array))#y positions 2nd mass

#x vs y
setInfo('$x$ [m]','$y$ [m]','Second rod')
plot(x,y)
show()

#time vs x
setInfo('$time$ [s]','$x$ [m]','Second rod')
plot(time,x)
show()

#time vs y
setInfo('$time$ [s]','$y$ [m]','Second rod')
plot(time,y)
show()