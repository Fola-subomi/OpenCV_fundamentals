import cv2
import numpy as np

#Events = [i for i in dir(cv2) if "EVENT" in i]
#print(Events)

def click_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + " , " + str(y)
        cv2.putText(img, strXY, (x,y), font, .5, (255,255,0), 1)
        cv2.imshow("image", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = int(img[x, y, 0])
        green = int(img[x, y, 1])
        red = int(img[x, y, 2])
        print( blue , " , ", green , " , ", red)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR= str(blue) + " , " + str(green) + " , " + str(red)
        cv2.putText(img, strBGR, (x,y), font, .5, (red,green,blue), 1)
        cv2.imshow("image", img)


#img = np.zeros((512,512, 3), np.uint8)
img = cv2.imread("Precious.jpg", 1)

cv2.imshow("image", img)
cv2.setMouseCallback("image", click_mouse)

cv2.waitKey(0)
cv2.destroyAllWindows