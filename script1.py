import cv2
from ultralytics import YOLO

# Load pretrained YOLOv8 model on COCO
model = YOLO("yolov8n.pt")

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Detection variables
consec_phone_frames = 0
N = 10 # Threshold: consecutive frames with phone to trigger disqualification
PHONE_CLASS_ID = 67  # COCO class ID for 'cell phone'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection with confidence filter
    results = model(frame, conf=0.5)
    boxes = results[0].boxes
    class_ids = boxes.cls

    # Filter only phones
    phone_boxes = [box for i, box in enumerate(boxes) if int(class_ids[i]) == PHONE_CLASS_ID]
    phone_detected = len(phone_boxes) > 0

    if phone_detected:
        consec_phone_frames += 1
        print(f"Phone detected! Count: {consec_phone_frames}")
    else:
        consec_phone_frames = 0

    # Draw only phone bounding boxes on the frame
    annotated_frame = frame.copy()
    for box in phone_boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(annotated_frame, "Phone", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Phone Detection", annotated_frame)

    # Trigger disqualification
    if consec_phone_frames >= N:
        print("Disqualified! Phone detected.")
        break

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

