from PIL import Image
import sys
import random
import getopt
import os
import subprocess
import time
import signal
import cv2
import numpy as np

#list = [[67, 153, 0], [255, 0, 0],[0,255,0], [0,0,255], [98, 190, 48], [122, 130, 188], [159, 4, 22], [0.412453, 0.357580, 0.180423]]  
list = [[255, 0, 0], [0, 0, 255],[0,128,0]]

img = Image.open('conv.png')
img.show() 
  
for i in range(len(list)):
           
        p_img = Image.new('P', (16, 16))
        p_img.putpalette(list[i])

        conv = img.quantize(palette=p_img, dither=0)
        conv.show()

