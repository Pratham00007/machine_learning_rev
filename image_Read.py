import cv2 as cv
# 0 for black and white and for colorfull
img=cv.imread("r1.jpg",0)
cv.imshow("Color_image",img)
print(img)
cv.waitKey(0)
cv.destroyAllWindows()