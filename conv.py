import numpy as np
from PIL import Image

# Open image
im = Image.open('Z1.png')

# Get palette and reshape into 3 columns
a=im.quantize(colors=1)
im.show()
