# -*- coding: utf-8 -*-
"""
Created on Sat May  5 16:51:11 2018

@author: Carmen
"""
import cv2
import getopt, sys
import os
from numpy import array
from csv import writer

 

def detect_colour(hsv,lower_colour,upper_colour,rod):
    mask = cv2.inRange(hsv, lower_colour, upper_colour)
    
    moments = cv2.moments(mask)
    area = moments['m00']
    
    if area == 0:#if the rod could not be deteced
        if rod == '1':
            rod1_data.append([rod1_data[-1][0],rod1_data[-1][1]])
            
            #Draws a turqoise rectangle at the last position recorded 
            cv2.rectangle(image, (rod1_data[-1][0], rod1_data[-1][1]), (rod1_data[-1][0]+2, rod1_data[-1][1]+2),(255,255,0), 2)
        
            print('rod1 not found')
        
        elif rod == '2':
            rod2_data.append([rod2_data[-1][0],rod2_data[-1][1]])
            
            #Draws a turqoise rectangle at the last position recorded
            cv2.rectangle(image, (rod2_data[-1][0], rod2_data[-1][1]), (rod2_data[-1][0]+2, rod2_data[-1][1]+2),(255,255,0), 2)
            
            print('rod2 not found')
        
        else:
            print('there are only 2 rods')#raise an expection!
            
    else:
        x = int(moments['m10']/area) #x coordinate of the centre
        y = int(moments['m01']/area) #y coordinate of the centre
            
        if rod == '1':
            rod1_data.append([x,y])
        elif rod == '2':
            rod2_data.append([x,y])
        else:
            print('you made a colour mistake!')#raise an expection!
            sys.exit()
        
        #Draws the center of the colour detected with a turqoise rectangle
        cv2.rectangle(image, (x, y), (x+2, y+2),(255,255,0), 2)
   


def write_data(rod,data):
    with open(os.path.join(video_folder, video_file + '_' + rod + '_data.csv'), 'w', newline='') as csvfile:
        w = writer(csvfile, delimiter=',')
        w.writerows(data)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:v:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print('video_processing.py -f <inputfile> -v <inputvideo>')  
        sys.exit(2)
    
    video_folder = None
    video_file = None
    
    for o, a in opts:
        if o == "-f":
            video_folder = a
        elif o == "-v":
            video_file = a
        else:
            assert False, "unhandled option"

    #creates folder to store frames
    os.makedirs(os.path.join(video_folder, video_file + '_frames'))
    
    rod1_data = []
    rod2_data = []
    counter = 0
    
    #colours to find:
    #1st rod (I chose blue)
    rod1_lower = array([98,127,161])
    rod1_upper = array([98,255,255])
    #2nd rod (I chose red)
    rod2_lower = array([0,84,94])
    rod2_upper = array([0,255,255])
    
    #loads video
    capture = cv2.VideoCapture(os.path.join(video_folder, video_file))
    
    image = None
    
    while(1):
        #Gets a frame or image (rgb format) 
        ret, image = capture.read()
        if ret == False: #no more frames to read (end of video)
            break
        #converts the frame from rgb to hsv
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        #looks for the positions of the lower end of the first (blue) and second (red) rods
        detect_colour(hsv,rod1_lower,rod1_upper,'1')
        detect_colour(hsv,rod2_lower,rod2_upper,'2')
        
        #save frame with rectangles
        cv2.imwrite(os.path.join(video_folder, video_file + '_frames', str(counter) + '.png'), image)
        
        counter +=1
    
    write_data('1',rod1_data) 
    write_data('2',rod2_data)
    

if __name__ == "__main__":
    main()