#!/usr/bin/env python3
# IMAGE PROCESSING PROGRAM

import numpy as np
import cv2
import math
import imutils
import matplotlib.pyplot as plt
from scipy import stats

class velo:

    def kejar(ang, dist_real):
        if dist_real >=50:
            speed = 0.2
            if ang >= 0 and ang < 30: # Region 12 
                com = '12'
            elif ang >= 30 and ang < 60: # Region 11 -depan (v)
                com = '11'
            elif ang >= 60 and ang < 90: # Region 10 
                com = '10'
            elif ang >= 90 and ang < 120: # Region 9 
                com = '9'
            elif ang >= 120 and ang < 150: # Region 8 -kanan (v)
                com = '8'
            elif ang >= 150 and ang <= 180: # Region 7 
                com = '7'
                # minus region
            elif ang < 0 and ang >= -30: # Region 6 
                com = '6'
            elif ang < -30 and ang >= -60: # Region 5 -kiri (v)
                com = '5'
            elif ang < -60 and ang >= -90: # Region 4 
                com = '4'
            elif ang < -90 and ang >= -120: # Region 3 
                com = '3'
            elif ang < -120 and ang >= -150: # Region 2 -belakang (v)
                com = '2'
            elif ang < -150 and ang >= -180: # Region 1 
                com = '1'
        # elif dist_real < 50 and dist_real > 50:
        #     com = 'Rotasi'
        #     speed = 0.5
        #     if ang < -120 and ang >= -150: # Region 11
        #         com = '11'
        elif dist_real < 50:
            com = 'Stop !!'
            speed = 0


        return com, speed
    
    def inv_motor(cmd_vel,speed):
        a =[[-0.33, 0.58, 0.33],
             [-0.33, -0.58, 0.33],
             [0.67, 0, 0.33]]
        speed = speed
        if cmd_vel=='1':
            # b = ([0.6, -0.3, -0.3])
            b =([0.3, -0.6, 0.3])
        elif cmd_vel=='2':
            b = ([0.6, -0.6, 0])
        elif cmd_vel=='3':
            b = ([1, -0.5, -0.5])
        elif cmd_vel=='4':
            b = ([0.6, 0, -0.6]) #
        elif cmd_vel=='5':
            b = ([0.33, 0.33, -0.67])
        elif cmd_vel=='6':
            b = ([0, 0.6, -0.6])
        elif cmd_vel=='7':
            b = ([0, -0.6, 0.6])
        elif cmd_vel=='8':
            b = ([-0.33, -0.33, 0.67])
        elif cmd_vel=='9':
            b = ([-0.67, 0, 0.67])
        elif cmd_vel=='10':
            b = ([-1, 0.5, 0.5])
        elif cmd_vel=='11':
            b = ([-0.58, 0.58, 0])
        elif cmd_vel=='12':
            b = ([-0.3, 0.6, -0.3])
        elif cmd_vel=='Stop !!':
            b = ([0, 0, 0])
        elif cmd_vel=='Rotasi':
            b = ([0, 0, 1])
        # b = ([ax, by, w])
        # res = np.dot(a,b)
        f1 = b[0]; f2 = b[1]; f3 = b[2]
        # res = (f1*255, f2*255, f3*255)
        res = (f1, f2, f3)
        # f1 = np.round(f1, decimals=1)
        # f2 = np.round(f2, decimals=1)
        # f3 = np.round(f3, decimals=1)
        
        return res
