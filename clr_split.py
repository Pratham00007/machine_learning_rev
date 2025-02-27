import cv2
img=cv2.imread("r2.jpg",1)
b,g,r=cv2.split(img)
cv2.imshow("normal",img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("R",r)


cv2.waitKey(0)
