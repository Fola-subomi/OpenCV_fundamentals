import cv2

x = 2+3
print(x)
img = cv2.imread("Precious.jpg", 1)
cv2.imshow("Frame", img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("Precious_copy", img)
    cv2.destroyAllWindows
    

    
