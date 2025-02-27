import cv2
img=cv2.imread("r1.jpg",1)
dim=img.shape
height=img.shape[0]
width=img.shape[1]
channels=img.shape[2]

size=img.size
print("dim: ",dim)
print("height: ",height)
print("width: ",width)
print("channel: ",channels)
print("size: ",size)