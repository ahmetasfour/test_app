import numpy
import matplotlib
import cv2

image = cv2.imread("image.jpg",0)
cv2.imshow("image",image)
cv2.waitKey(0)
out_image = cv2.medianBlur(image,image,3)
cv2.ConnectedComponentsAlgorithmsTypes(image,image)
