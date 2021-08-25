import cv2
import time
face=cv2.CascadeClassifier("C:/Users/Ashu/Desktop/AI Projects/haarcascade_frontalface_default.xml")
a=cv2.VideoCapture(0)
cl='Press q to Quit'
while 1:
    check,frame=a.read()
    gr=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gr,scaleFactor=1.05,minNeighbors=5)
    k=1
    for x,y,w,h in faces:
        cv2.putText(frame,'Person '+str(k),(x,y-10),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,0),2)
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        k+=1
    cv2.putText(frame,cl,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)    
    cv2.imshow("Live Camera",frame)
    t=cv2.waitKey(1)
    if t==ord('q'):break
a.release()
cv2.destroyAllWindows()