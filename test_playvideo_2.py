import numpy as np
import cv2

cap = cv2.VideoCapture('samples/data/vtest.avi')

_, frame = cap.read()

assert frame is not None, "Fmmpeg seems not to be installed properly"

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()

while(cap.isOpened()):
    ret, frame = cap.read()
	
    if ret == True:

        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
		
        cv2.imshow('frame',fgmask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break

cap.release()
cv2.destroyAllWindows()