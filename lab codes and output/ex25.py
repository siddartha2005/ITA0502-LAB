import cv2

img = cv2.imread('sample.jpg')

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 50, 150)

    contours, hierarchy = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    result = img.copy()

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(result, (x, y), (x + w, y + h),
                          (0, 255, 0), 2)

    cv2.imshow('Original Image', img)
    cv2.imshow('Recognized Object', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
