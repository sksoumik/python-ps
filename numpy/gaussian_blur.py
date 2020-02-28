import numpy as np
from scipy import stats
from scipy import signal
import cv2

pdf = stats.norm(5, 10).pdf
lin = np.linspace(0, 10, 2)
gaussian_filter = np.array([[pdf(x) * pdf(y) for x in lin] for y in lin])

image = cv2.imread("xray_20180112_125809.pnm.png")
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = signal.correlate(gray_img, gaussian_filter)
cv2.imwrite("gaussian_image.png", blurred_image)
cv2.waitKey(0)
