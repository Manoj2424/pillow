from PIL import Image
import time
import signal
import cv2
import numpy as np


pall = [
    0, 0, 0,
    255, 0, 0,
    255, 255, 0,
    255, 153, 0,
]

colorImage = Image.open("Z.png")
conv = colorImage.quantize(palette=pall)
conv.show()

