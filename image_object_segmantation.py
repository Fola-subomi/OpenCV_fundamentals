import cv2

img = cv2.imread("crimping tool.jpeg")
#img= cv2.resize(img,(512,512))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    l=y+h
    b=x+w
    font = cv2.FONT_HERSHEY_SIMPLEX
    text= "[" +  "(" + str(x)+" , "+str(y) + ")" + " " + "(" + str(b)+" , "+str(l)  + ")" + "]"
    print(f"({x},{y}), ({b} , {l})")
    cv2.rectangle(img, (x, y), (b,l), (0,0, 255), 2)
    cv2.putText(img,text,(x,y),font,.5, (0,0,0), 1)

cv2.imshow("frame", img)

cv2.waitKey(0)
cv2.destroyAllWindows
    