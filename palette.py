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

im = Image.open('Z.png').convert('P')
im.show()
a=np.array(im.getpalette()).reshape(256,3)

print(a)

num=len(a)
print(num)
for i in range(0,num,50):
        img = Image.open('Z.png')
            
        p_img = Image.new('P', (16, 16))
        p_img.putpalette(a[i])

        conv = img.quantize(palette=p_img, dither=0)
        conv.show()
