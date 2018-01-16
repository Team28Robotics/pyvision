import numpy as np
import cv2
import time

def cost(im1, im2):
    return np.sum(np.absolute(im1 - im2))

y = np.zeros(100)
x = np.arange(0,100,1)

cap = cv2.VideoCapture('sample1.avi')

ret, frame = cap.read()
pt = time.time()
while(True):
    t = time.time()

    # Capture frame-by-frame
    prevframe = frame
    ret, frame = cap.read()

    y = np.append(y[1:], cost(frame, prevframe))

    # Our operations on the frame come here
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    print(cost(frame, prevframe))
    #print(1/(t-pt))
    pt = t
    time.sleep(0.12)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

