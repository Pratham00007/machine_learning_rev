import cv2
img=cv2.imread("r1.jpg",1)
cv2.imshow("original",img)
scale=1.0
centre=(img.shape[0]/2,img.shape[1]/2)
angle90=90

m=cv2.getRotationMatrix2D(centre,angle90,scale)
rotated=cv2.warpAffine(img,m,(img.shape[0],img.shape[1]))
cv2.imshow("rotaed",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()