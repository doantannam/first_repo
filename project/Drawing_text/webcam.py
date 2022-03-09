import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    pts = np.array([[100,10],[20,50],[20,140],[100,180],[180,140],[180,50]], np.int32)
    pts = pts.reshape((-1,1,2))
    isClosed = True
    color = (0, 255, 255)
    thickness = 1
    cv.fillPoly(frame, pts =[pts], color=color)   
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame,'Doan Tan Nam',(10,450), font, 1,(0,0,0),2,cv.LINE_AA)
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()