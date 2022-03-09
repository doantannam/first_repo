import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
  
img = cv.imread('capture.PNG')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]


img1 = img.copy()
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)

img2 = img.copy()
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img2,[box],0,(0,0,255),2)

img3 = img.copy()
(x, y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)
cv.circle(img3, center, radius, (0, 255, 0), 2)
# text1 = 'Center: (' + str(int(x)) + ', ' + str(int(y)) + ') '
# text2 = 'Diameter: ' + str(2*radius)
# cv.putText(img3, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv.LINE_AA, 0)
# cv.putText(img3, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv.LINE_AA, 0)

img4 = img.copy()
ellipse = cv.fitEllipse(cnt)
cv.ellipse(img4,ellipse,(0,255,0),2)

img5 = img.copy()
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img5,(cols-1,righty),(0,lefty),(0,255,0),2)

cv.imshow('1', img)
cv.imshow('2', img1)
cv.imshow('3', img2)
cv.imshow('4', img3)
cv.imshow('5', img4)
cv.imshow('6', img5)
 
cv.waitKey(0)
cv.destroyAllWindows()

 
