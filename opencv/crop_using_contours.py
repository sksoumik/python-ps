# Find Contours 

import cv2
#reading the image 
image = cv2.imread("xray.jpg")
edged = cv2.Canny(image, 15, 50)
cv2.imshow("Edges", edged)
cv2.waitKey(0)
 
#applying closing function 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closed", closed)
cv2.waitKey(0)
 
#finding_contours 
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    new_img=image[y:y+h,x:x+w]
    cv2.imwrite('roi.jpg', new_img)

cv2.imshow("Output", image)
cv2.waitKey(0)