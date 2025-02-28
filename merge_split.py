import cv2
img=cv2.imread("r2.jpg",1)
cv2.imshow("original",img)

b,g,r=cv2.split(img)
merged_bgr=cv2.merge((b,g,r))
meged_rgb=cv2.merge((r,g,b))
cv2.imshow("merged_bgr",merged_bgr)
cv2.imshow("meged_rgb",meged_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()