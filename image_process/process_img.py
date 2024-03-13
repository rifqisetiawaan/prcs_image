#!/usr/bin/env python3
# IMAGE PROCESSING PROGRAM

import numpy as np
import cv2
import math
import imutils
import matplotlib.pyplot as plt
from scipy import stats

class process_image:

    def __init__(self, centroid):
        self.centroid = centroid

    def find_centroid(x1, y1, x2, y2):
        centx = int((x1+x2)/2)
        centy = int((y1+y2)/2)

        return centx, centy
    
    def plot_line(frame, centroid):
        # plot hasil centroid
        cv2.circle(frame, (centroid[0], centroid[1]), 
                    radius=3, color=(0, 0, 255), thickness=-1)
        
        cv2.line(frame, (centroid[0], centroid[1]), (300, 240),
                    color=(0, 0, 255), thickness=1)
        cv2.line(frame, (300, 240), (373, 289),
                    color=(0, 0, 255), thickness=1)
        
    def slope(x1s, y1s, x2s, y2s):
        return abs(y2s-y1s)/(x2s-x1s)
    
    def know_angle(s1, s2):
        # return math.degrees(math.atan((s2-s1)/(1+(s2*s1))))
        # ang = math.degrees(math.atan(s1-s2)/(1+(s1*s2)))
        ang = math.atan2(s1-s2)/(1+(s1*s2))
        return ang
    
    def penentuan_derajat(x_bola, y_bola):
        # menentukan perhitungan
        x_frame = 640; y_frame = 480
        pos_x = x_bola-(x_frame/2)
        pos_y = (y_frame/2)-y_bola

        if pos_x<0 and pos_y==0: # done
            radii = '-------'
            deg = 0

        elif pos_x==0 and pos_y>0: # done
            radii = '-------'
            deg = 90

        elif pos_x>0 and pos_y==0: # 
            radii = '-------'
            deg = 180

        elif pos_x==0 and pos_y<0:
            radii = '-------'
            deg = -90

        elif pos_x<0 and pos_y<0: # R4 done
            radii = math.atan(pos_x/pos_y)
            deg = (math.degrees(radii))-90

        elif pos_x>0 and pos_y<0: # R3
            radii = math.atan(pos_x/pos_y)
            deg = (math.degrees(radii))-90

        elif pos_x>0 and pos_y>0: # R2 done
            radii = math.atan(pos_x/pos_y)
            deg = 180+(math.degrees(radii))-90

        elif pos_x<0 and pos_y>0: # R1 done
            radii = math.atan(pos_x/pos_y)
            deg = (math.degrees(radii))+90

        # else:
        #     a = print('No Ball')

        deg = np.round(deg, decimals=2)

        return pos_x,pos_y, radii, deg
    
    def dist_pixel(cent1, cent2, cntx, cnty):
        # distance pixel
        dpx = math.dist([cent1, cent2], [cntx, cnty])
        dpx = np.round(dpx, decimals=2)
        return dpx
    
    def dist_real(dpx):
        if dpx is not None:
            dist_real = (-100.2*(np.log(dpx)) - 28.43)
            dist_real = np.round(dist_real, decimals=2)
            return dist_real
        else:
            pass

    def text_display_det(classes, frame, ang, dist_real):
        font = cv2.FONT_HERSHEY_SIMPLEX
        if classes == [0.0]:
            cv2.putText(frame,'Angle Bola: '+str(ang)+' deg', 
                        (50, 50), font, 0.5,
                        (0, 255, 255), 1, cv2.LINE_4)
            cv2.putText(frame,'Distance Bola: '+str(dist_real)+' cm', 
                        (50, 65), font, 0.5,
                        (0, 255, 255), 1, cv2.LINE_4)
        else:
            cv2.putText(frame,'Angle Bola: N/A', 
                        (50, 50), font, 0.5,
                        (0, 255, 255), 1, cv2.LINE_4)
                    
            
    