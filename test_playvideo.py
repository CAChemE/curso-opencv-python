import numpy as np
import cv2

cap = cv2.VideoCapture('samples/data/vtest.avi')

_, frame = cap.read()

assert frame is not None, "Fmmpeg seems not to be installed properly"

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		cv2.imshow('frame',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
		

cap.release()
cv2.destroyAllWindows()