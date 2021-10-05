from PIL import Image
import extcolors
import sys
import random
import getopt
import os
import subprocess
import time
import signal
import numpy as np

table=[]

colors, pc = extcolors.extract_from_path("conv.png")
print(colors)

for i in range(len(colors)):
	table.append(list(colors[i][0]))

print(table)

for i in range(len(table)):
        img = Image.open('conv.png')
            
        p_img = Image.new('P', (16, 16))
        p_img.putpalette(table[i])

        conv = img.quantize(palette=p_img, dither=0)
        conv.show()	
