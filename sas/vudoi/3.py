import cv2
d=cv2.VideoCapture("qq.mp4")
frame=d.get(cv2.CAP_PROP_FRAME_COUNT)
t=d.get(cv2.CAP_PROP_FPS)
print(frame)
print(t)
i=1
while(True):
    ret,frame=d.read()
    print(ret)
    if(ret):
        name='image/'+str(i)+'.jpg'
        cv2.imwrite(name,frame)
        i+=1

        cv2.imshow('frame',frame)
        if (cv2.waitKey(1)& 0xFF==ord('z')):
            break
d.release()
cv2.destroyAllWindows()    
