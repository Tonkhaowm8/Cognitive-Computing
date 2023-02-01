import cv2
import numpy as np

img = cv2.imread("fingerprint.png", cv2.IMREAD_GRAYSCALE) 
cv2.imshow("input image", img)
cv2.waitKey(0)

th,maxVal = 0,0#Choose the threshold and the maxVal [ Experiment with different values]

retval, segmentedImg = cv2.threshold(img, th,maxVal,cv2.THRESH_BINARY)
cv2.imshow("THRESH_BINARY", segmentedImg)
cv2.waitKey(0)

retval, segmentedImg = cv2.threshold(img, th,maxVal, cv2.THRESH_BINARY_INV) 
cv2.imshow("THRESH_BINARY_INV", segmentedImg)
cv2.waitKey(0)

retval, segmentedImg = cv2.threshold(img, th,maxVal, cv2.THRESH_TRUNC) 
cv2.imshow("THRESH_TRUNC", segmentedImg)
cv2.waitKey(0)

retval, segmentedImg = cv2.threshold(img, th,maxVal, cv2.THRESH_TOZERO)
cv2.imshow("THRESH_TOZERO", segmentedImg)
cv2.waitKey(0)

retval, segmentedImg = cv2.threshold(img, th,maxVal, cv2.THRESH_TOZERO_INV) 
cv2.imshow("THRESH_TOZERO_INV", segmentedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
