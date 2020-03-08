import cv2
import argparse
import numpy as np
import os
import glob
import ntpath
from pathlib import Path
import time



def main():
    parser = argparse.ArgumentParser(description='Canny threshold values')
    parser.add_argument('--impath',
                        default="/home/soumik/code/nikko_debone/out/JPEGImages/*.jpg",
                        type=str,
                        help='Image Path for JPEGImages')
    # parser.add_argument('--th01',
    #                     default=15,
    #                     type=int,
    #                     help='Lower threshold value')
    # parser.add_argument('--th02',
    #                     default=50,
    #                     type=int,
    #                     help='Higher threshold value')

    args = parser.parse_args()




    count = 0
    save_dir = "roi_output/"
    for bb, file in enumerate(glob.glob(args.impath)):
        print(bb, file)
        head, tail = ntpath.split(file)



        start_time = time.time()
        new_img = crop_roi(file)
        
        count +=  (time.time() - start_time)
        os.makedirs(save_dir, exist_ok=True)
        cv2.imwrite(save_dir + "{}".format(tail), new_img)
        cv2.waitKey(0)
    print("--- %s seconds ---" % count)

def crop_roi(path, sigma=0.15):
    image = cv2.imread(path)


    sigma=0.33
    v = np.mean(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))


    edged = cv2.Canny(image, lower, upper)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) != 0:
        # find the contour with the biggest area
        c_max = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c_max)
        new_img = image[y:y + h, x:x + w]
    return new_img


if __name__ == "__main__":
    main()
