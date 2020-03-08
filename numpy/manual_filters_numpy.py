"""
Make filters manually and apply on the image. 
"""

import numpy as np
from scipy import signal
import cv2

filter_1 = np.array([[1, 1, 1, 1, 1]])

image = cv2.imread("xray_20180112_125809.pnm.png")
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = signal.correlate(gray_img, filter_1)
cv2.imwrite("blurred_image.png", blurred_image)
cv2.waitKey(0)
