import numpy as np
import cv2, time

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('sample-640x480.avi',fourcc, 30.0, (640,480))

pt = time.time()

while(cap.isOpened()):

    t = time.time()

    ret, frame = cap.read()
    frame = cv2.putText(frame, str(int(1/(t-pt))), (30,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,230,255))

    pt = t

    if ret:
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
