import cv2
import numpy as np

def click_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 3, (225,150,100), -1)
        circle_points.append((x,y))
        if len(circle_points)>=2:
            cv2.line(img,circle_points[-1],circle_points[-2],(225,225,220),1)

        cv2.imshow("image", img)

circle_points = []


img = np.zeros((512,512, 3), np.uint8)
#img = cv2.imread("Precious.jpg", 0)

cv2.imshow("image", img)
cv2.setMouseCallback("image", click_mouse)

cv2.waitKey(0)
cv2.destroyAllWindows