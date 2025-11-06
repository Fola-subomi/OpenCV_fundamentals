import cv2
import numpy as np

def mouse_call_events(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img [x, y, 0]
        green = img [x, y, 1]
        red = img [x, y, 2]

        cv2.circle(img, (x,y), 3, (0,0,225), -1)
        my_color = np.zeros((512,512,3), np.uint8)

        my_color[:] = [blue,green,red]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(red) + " , " + str(green) + " , " + str(blue)
        cv2.putText(my_color,text,(10,50), font, 1, (225,100, 65), 1, cv2.LINE_AA)
        cv2.imshow("color", my_color)
        

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("Precious.jpg")

cv2.imshow("Image", img)
cv2.setMouseCallback("Image", mouse_call_events)

cv2.waitKey(0)
cv2.destroyAllWindows