#Siraphop Mukdaphetcharat 64011614
import cv2
import numpy as np

#img1 = np.zeros((300, 300, 3), dtype="uint8")
#for i in range(7):
#    cv2.circle(img1, (150, 150), i * 25, (255, 255, 255))
#
#cv2.imshow('circles', img1)
#cv2.waitKey(0)



#img2 = cv2.imread("/Users/tonkhaow/Desktop/Cognitive-Computing/OpenCV/Week 2/Assignment2_pycharm/Cat03.jpg")
#img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grayscale Cat", img2)
#cv2.waitKey()


img3 = cv2.imread("/Users/tonkhaow/Desktop/Cognitive-Computing/OpenCV/Week 2/Assignment2_pycharm/cat_image.png")

mask = np.zeros(img3.shape[:2], dtype = "uint8")
(cX, cY) = (img3.shape[1] // 2, img3.shape[0] // 2)
cv2.circle(mask, (cX, cY), cY, color=150, thickness=-1)

masked = cv2.bitwise_and(img3, img3, mask = mask)
cv2.imshow("Circle Puss", masked)
cv2.waitKey(0)



