
import cv2

cap = cv2.VideoCapture("sample.mp4")

if not cap.isOpened():
    print("Error: Video file not found")
    exit()

backSub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    fgMask = backSub.apply(frame)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, kernel)

    contours, hierarchy = cv2.findContours(
        fgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    vehicle_count = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.putText(frame, "Vehicle", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)

            vehicle_count += 1

    cv2.putText(frame, "Vehicles: " + str(vehicle_count),
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

    cv2.imshow("Vehicle Detection", frame)
    cv2.imshow("Foreground Mask", fgMask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
