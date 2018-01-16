import numpy as np
import cv2
import time

cap = cv2.VideoCapture('sample1.avi')

pt = time.time()

low = np.array([0,192,0])
high= np.array([256,256,256])
def process(img):
    # high saturation pixels displayed
    hsv = cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), low, high)
    return np.bitwise_and(img, np.rollaxis(np.array([hsv,hsv,hsv]), 0, 3))

while(True):

    t = time.time()
    print(1/(t-pt))
    pt = t

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame=process(frame)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

