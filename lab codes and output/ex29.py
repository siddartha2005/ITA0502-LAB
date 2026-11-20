
import cv2

img = cv2.imread("sample.jpg")

if img is None:
    print("Error: Image file not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

eyes = eye_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20, 20)
)

for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.putText(img, "Eye", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                (0, 255, 0), 2)

print("Number of eyes detected:", len(eyes))

cv2.imshow("Eye Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
