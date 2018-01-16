import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

def cost(im1, im2):
    return np.sum(np.absolute(im1 - im2))

def process(img):
    img[img >= 64] = 255
    img[img < 64] = 0
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

