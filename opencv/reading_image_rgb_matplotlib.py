import cv2
import numpy as numpy

image = cv2.imread("xray.jpg")
blurred = cv2.pyrMeanShiftFiltering(image, 31, 91)
ret, threshold = cv2.threshold(blurred, 0, 255,
                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, conturs, _ = cv2.findContours(threshold, cv2.RETR_LIST,
                                 cv2.CHAIN_APPROX_NONE)
print("Number of contours detected {}".format(len(conturs)))

cv2.drawContours(image, conturs, 0, (0, 0, 255), 6)
cv2.namedWindow("Display", cv2.WINDOW_NORMAL)
cv2.imshow("Display", image)
cv2.waitKey()
