# Source code was copied from this web site: https://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame-by-frame 		####### Don't want to display frame here--instead send it to RTSP url
    cv2.imshow('frame',gray)					####         However, want to keep this for another program that displays what's given by RTSP url
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()