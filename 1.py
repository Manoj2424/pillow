from PIL import Image
import sys
import random
import getopt
import os
import subprocess
import time
import signal
import numpy as np

tup=(0.412453, 0.357580, 0.180423,0)
tup=tuple(tup)
colorImage = Image.open("Output.png")
imageWithColorPalette = colorImage.convert("RGB", palette=Image.ADAPTIVE)
imageWithColorPalette.save("conv.png")

a=Image.open("Output.png")
a.show()
