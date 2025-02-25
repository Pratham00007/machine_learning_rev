import cv2 
img=cv2.imread("r1.jpg",1)
# cv2.imshow("image1",img)

# colour scheme changing
# img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",img2)

img3=cv2.cvtColor(img,cv2.COLOR_BG2RGB)
cv2.imshow("rgb",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()