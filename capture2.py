import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

pt = time.time()

low = np.array([128,128,128], dtype='uint8')
high= np.array([255,255,255], dtype='uint8')
def process(img):
    return cv2.inRange(img,low,high)

while(True):

    t = time.time()
    print(1/(t-pt))
    pt = t

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame=process(frame)

    # Display the resulting frame
#   cv2.imshow('frame',frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

