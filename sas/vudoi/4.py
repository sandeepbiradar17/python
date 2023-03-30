import cv2
d=cv2.VideoCapture("qq.mp4")
i=1
while(True):
    ret,frame=d.read()
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'wlecome',(500,50),font,1,(6,255),2,cv2.LINE_4)    
    cv2.imshow('frame',frame)
    if (cv2.waitKey(1)& 0xFF==ord('z')):
            break
d.release()
cv2.destroyAllWindows()   



