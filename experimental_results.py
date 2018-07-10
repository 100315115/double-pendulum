# -*- coding: utf-8 -*-
"""
Created on Sat May  5 21:40:19 2018

@author: Carmen
"""
from matplotlib.pyplot import *
from numpy import linspace
from pandas import read_csv
import os
import getopt, sys


def plot_data(rod):
    number_frames = len(x_dots)
    title = None
    
    if rod == '1':
        title = 'First rod'
    elif rod == '2':
        title = 'Second rod'
    
    # x versus y pixel positions
    setInfo('$x$ [pixels]','$y$ [pixels]',title)
    gca().invert_yaxis()
    plot(x_dots, y_dots, 'o')
    show()
    
    #frames versus x
    setInfo('frames ','$x$ [pixels]',title)
    plot(linspace(1,number_frames,number_frames), x_dots, 'o')
    show()
    
    #frames versus y
    setInfo('frames ','$y$ [pixels]',title)
    gca().invert_yaxis()
    plot(linspace(1,number_frames,number_frames), y_dots, 'o')
    show()


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:d:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print('experimental_results.py -f <inputfile> -d <inputdata [inputdata2...]>')  
        sys.exit(2)
    
    data_folder = None
    data_files = None
    
    for o, a in opts:
        if o == "-f":
            data_folder = a
        elif o == "-v":
            data_files = a #mirar bien esto!!!
        else:
            assert False, "unhandled option"

    #me imagino que data_files es una lista

    x_dots = None
    y_dots = None
    
    for data_file in data_files:
        data = read_csv(os.path.join(data_folder, data_file), header=None)
    
        x_dots = data.iloc[:,0]
        y_dots = data.iloc[:,1]
        
        if '1' in data_file:
            plot_data('1')
        elif '2' in data_file:
            plot_data('2')
    

if __name__ == "__main__":
    main()
