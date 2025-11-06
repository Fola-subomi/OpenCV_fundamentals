import cv2
import numpy as np

img = np.zeros([600,600,3],np.uint8)
img = cv2.line( img, (0,0), (255,255), (50,144,167), 5)
img = cv2.arrowedLine(img, (0,255), (255,255), (200,150,90), 5)
img = cv2.rectangle(img, (0,0), (255,255), (100,100,100), 5)
img = cv2.circle(img, (255,255), 100, (255,255,255), -1)

cv2.imshow("frame", img)

cv2.waitKey(0)
cv2.destroyAllWindows