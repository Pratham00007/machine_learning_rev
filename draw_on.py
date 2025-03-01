import cv2
img=cv2.imread("r1.jpg",1)
centr=(int(img.shape[0]/2)-1 , int(img.shape[1]/2)-1)
cv2.circle(img=img,center=centr,radius=50,color=(0,255,0),thickness=10)
cv2.imshow("circle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
