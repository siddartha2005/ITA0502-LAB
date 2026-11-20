import cv2

img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
    exit()

h, w = img.shape[:2]

roi = img[50:148, 50:220]

copied_roi = roi.copy()

result = img.copy()

rh, rw = copied_roi.shape[:2]

x = w - rw
y = h - rh

result[y:y+rh, x:x+rw] = copied_roi

cv2.imshow("Original Image", img)
cv2.imshow("Cropped ROI", roi)
cv2.imshow("Copied ROI", copied_roi)
cv2.imshow("Pasted Image", result)

cv2.imwrite("sample_roi.jpg", roi)
cv2.imwrite("sample_pasted.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
