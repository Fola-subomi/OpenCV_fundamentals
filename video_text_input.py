import cv2
import datetime

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if ret== True:
        text= "width: "+str(cap.get(3))+ " Height: "+str(cap.get(4))
        dt= str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_TRIPLEX
        frame = cv2.putText(frame,text,(10,30),font,1,(200,100,150),2,cv2.LINE_AA)
        frame = cv2.putText(frame,dt,(10,60),font,1,(100,100,150),2,cv2.LINE_AA)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cv2.destroyAllWindows