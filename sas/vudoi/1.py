import cv2
d=cv2.VideoCapture("0")
i=1
while(True):
    ret,frame=d.read()
    if(ret):
        name='image/'+str(i)+'.jpg'
        cv2.imshow('frame',frame)
        if (cv2.waitKey(1)& 0xFF==ord('z')):
            break
d.release()
cv2.destroyAllWindow()   

# while(True):
#     ret,frame=d.read()
#     print(ret)
#     if(ret):
#         name='image/'+str(i)+'.jpg'
#         cv2.imwrite(name,frame)
#         i+=1

#         cv2.imshow('frame',frame)
#         if (cv2.waitKey(1)& 0xFF==ord('z')):
#             break 
# d.release()
# cv2.destroyAllWindows() 
