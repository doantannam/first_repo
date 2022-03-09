import numpy as np
import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("dark_night.jpg"))
cv.rectangle(img,(600,300),(900,600),(0,0,255),3)
cv.rectangle(img,(700,400),(800,500),(0,0,255),3)
cv.line(img,(700,300),(600,400),(255,0,0),2)
cv.line(img,(800,600),(900,500),(255,0,0),2)
cv.line(img,(600,500),(700,600),(255,0,0),2)
cv.line(img,(800,300),(900,400),(255,0,0),2)
cv.line(img,(600,450),(685,425),(255,0,0),2)
cv.line(img,(600,400),(685,425),(255,0,0),2)
cv.line(img,(600,500),(685,475),(255,0,0),2)
cv.line(img,(600,450),(685,475),(255,0,0),2)
cv.line(img,(700,300),(725,385),(255,0,0),2)
cv.line(img,(750,300),(725,385),(255,0,0),2)
cv.line(img,(750,300),(775,385),(255,0,0),2)
cv.line(img,(800,300),(775,385),(255,0,0),2)
cv.line(img,(725,515),(700,600),(255,0,0),2)
cv.line(img,(725,515),(750,600),(255,0,0),2)
cv.line(img,(775,515),(750,600),(255,0,0),2)
cv.line(img,(775,515),(800,600),(255,0,0),2)
cv.line(img,(815,425),(900,400),(255,0,0),2)
cv.line(img,(815,425),(900,450),(255,0,0),2)
cv.line(img,(815,475),(900,450),(255,0,0),2)
cv.line(img,(815,475),(900,500),(255,0,0),2)
cv.circle(img,(750,450), 50, (255,0,255),2)
cv.line(img,(750,400),(800,450),(255,255,255),2)
cv.line(img,(700,450),(750,400),(255,255,255),2)
cv.line(img,(750,500),(700,450),(255,255,255),2)
cv.line(img,(800,450),(750,500),(255,255,255),2)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Doan Tan Nam',(400,700), font, 3,(255,255,255),2,cv.LINE_AA)

if img is None:
    sys.exit("Could not read the image.")
    
cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("dark_night.png", img)
    

