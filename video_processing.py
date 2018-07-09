# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:51:11 2018

@author: Carmen
"""
import cv2
import numpy as np
import getopt, sys
import os
import csv



def detect_colour(hsv,lower_colour,upper_colour,colour):
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    
    moments = cv2.moments(mask)
    area = moments['m00']
    
    if area == 0:
        if colour == 'b':
            rod1_data.append([rod1_data[-1][0],rod1_data[-1][1]])
            
            #Draw the center of the colour detected with a rectangle
            cv2.rectangle(image, (rod1_data[-1][0], rod1_data[-1][1]), (rod1_data[-1][0]+2, rod1_data[-1][1]+2),(255,255,0), 2)
            
            print('rod1 not found')
        elif colour == 'r':
            rod2_data.append([rod2_data[-1][0],rod2_data[-1][1]])
            
            #Draw the center of the colour detected with a rectangle
            cv2.rectangle(image, (rod2_data[-1][0], rod2_data[-1][1]), (rod2_data[-1][0]+2, rod2_data[-1][1]+2),(255,255,0), 2)
            
            print('rod2 not found')
        else:
            print('you made a colour mistake!')
            
    else:
        x = int(moments['m10']/area) # x coordinate (centre)
        y = int(moments['m01']/area) # y coordinate (centre)
            
        if colour == 'b':
            rod1_data.append([x,y])
        elif colour == 'r':
            rod2_data.append([x,y])
        else:
            print('you made a colour mistake!')
            sys.exit()
        
        #Draw the center of the colour detected with a rectangle
        cv2.rectangle(image, (x, y), (x+2, y+2),(255,255,0), 2)
   


def write_data(colour,data):
    with open(os.path.join(video_folder, colour + '_data.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)




video_folder = sys.argv[1]
video_file = sys.argv[2]

rod1_data = []
rod2_data = []
counter = 0



#colours to find:
#1st rod (I chose blue)
rod1_lower = np.array([98,127,161])
rod1_upper = np.array([98,255,255])
#2nd rod (I chose rod2)
rod2_lower = np.array([0,84,94])
rod2_upper = np.array([0,255,255])

#loads video
capture = cv2.VideoCapture(os.path.join(video_folder, video_file))


while(1):
    #Gets an imagen and converts from rgb to hsv
    ret, image = capture.read()
    if ret == False: #no more frames to read (end of video)
        break
    #image.get()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    #looks for the positions of the first (green) and second (rod2) bar
    #detect_colour(hsv,rod1_lower,rod1_upper,'b')
    detect_colour(hsv,rod2_lower,rod2_upper,'r')
    
    #save image with rectangles
    cv2.imwrite(os.path.join(video_folder, str(counter) + '.png'), image)
    
    counter +=1

write_data('b',rod1_data) 
write_data('r',rod2_data)