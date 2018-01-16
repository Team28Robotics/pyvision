import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

def cost(im1, im2):
    return np.sum(np.absolute(im1 - im2))

#low = np.array([0,32,0], dtype='uint8')
#mid = np.array([64,64,64], dtype='uint8')
high = np.array([224,224,224], dtype='uint8')
def process(img):
    mid = np.mean(np.mean(img, axis=0, dtype='uint8'), axis=0, dtype='uint8')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #img = cv2.inRange(hsv, low, mid) / 2
    img =  cv2.inRange(hsv, mid, high)
    return img

plt.ion()
y = np.zeros(100)
x = np.arange(0,100,1)

cap = cv2.VideoCapture('sample1.avi')

ret, frame = cap.read()
frame = process(frame)
prevtime = time.time()
while(True):
    # Capture frame-by-frame
    prevframe = frame
    ret, frame = cap.read()

    frame = process(frame)
    c = cost(frame, prevframe)
    y = np.append(y[1:], c)
    plt.clf()
    plt.plot(x,y)
    plt.pause(0.01)


    print(c)

    # Display the resulting frame
    cv2.imshow('frame',frame)

    t = time.time()
    print(t-prevtime)
    prevtime = t
    #time.sleep(0.12)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

