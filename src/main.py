from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("best.pt")   # Replace with your trained model

# Open video
cap = cv2.VideoCapture("road_video.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Detect potholes
    results = model(frame)

    # Draw detections
    annotated_frame = results[0].plot()

    cv2.imshow("Pothole Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
