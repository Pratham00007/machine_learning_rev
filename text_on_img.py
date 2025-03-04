import cv2
img=cv2.imread("r1.jpg",1)

font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img=img,text="ronaldo",org=(25,200),fontFace=font,fontScale=1,color=(255,0,0),thickness=5)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()