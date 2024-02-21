import os
import cv2
import shutil
import random
import pytesseract
try:
    from PIL import Image
except ImportError:
     import Image

import numpy as np
import matplotlib.pyplot as plt

image_path = input("Enter the path to the image file: ")

if not os.path.exists(image_path):
    print("Error: The provided path does not exist.")
    exit()
image_orignal=cv2.imread(image_path)
plt.imshow(image_orignal)
plt.axis("off")
plt.show()

image_path_in_colab=image_path
extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab))
print(extractedInformation)