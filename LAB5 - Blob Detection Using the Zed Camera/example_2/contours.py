# Standard imports
import cv2
import numpy as np;
import imutils

# Read image
im = cv2.imread("frame0070.jpg")

hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

r1 = np.array([0, 100, 200])

r2 = np.array([15, 255, 255])
mask = cv2.inRange(hsv, r1, r2)

mask = cv2.GaussianBlur(mask, (21,21), 0)
mask = cv2.erode(mask, (3, 3), iterations=5)
contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im, contours, -1, (0, 255, 0))

for j in range(0, len(contours)):
    #rect = cv2.minAreaRect(contours[j])
    #box = cv2.cv.BoxPoints(rect)
    #box = np.int0(box)
    #cv2.drawContours(im,[box],0,(0,0,255),2)

    M = cv2.moments(contours[j])
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # draw the contour and center of the shape on the image
    cv2.drawContours(im, [contours[j]], -1, (0, 255, 0), 2)
    cv2.circle(im, (cX, cY), 4, (255, 255, 255), -1)
    cv2.putText(im, "center", (cX - 20, cY - 20),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Show blobs
cv2.imshow("o shit wadap", im)
cv2.waitKey(0)
