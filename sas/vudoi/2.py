import cv2
d=cv2.VideoCapture("qq.mp4")
while(True):
    ret,frame=d.read()
    cv2.imshow('frame',frame)
    if (cv2.waitKey(1)& 0xFF==ord('z')):
        break
d.release()
cv2.distroyAllWindow()    
