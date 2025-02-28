import cv2
img=cv2.imread("r1.jpg",1)
cv2.imshow("original",img)
print("dimension earier",img.shape)
height=100
width=100
dimension=(height,width)
resized=cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)
cv2.imshow("resized",resized)
print(resized.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()