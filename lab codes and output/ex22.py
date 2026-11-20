import cv2
import numpy as np

img = cv2.imread('sample.jpg')

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Original Image', img)
    cv2.imshow('Binary Image', thresh)
    cv2.imshow('Opening Operation', opening)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
