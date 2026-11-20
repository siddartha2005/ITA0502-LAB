import cv2

img = cv2.imread("sample.jpg")

if img is None:
    print("Image not found")
    exit()

watermark = "COPYRIGHT"

position = (30, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)
thickness = 2

watermarked = img.copy()

cv2.putText(watermarked, watermark, position, font,
            font_scale, color, thickness, cv2.LINE_AA)

cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", watermarked)

cv2.imwrite("sample_watermarked.jpg", watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()
