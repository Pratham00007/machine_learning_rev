import cv2 
img=cv2.imread("r1.jpg",1)
# create img r3 same directory
status=cv2.imwrite("r3.jpg",img)
print("file written",status)