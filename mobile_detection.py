import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

phone_detection_count = 0  
N = 3  #  disqualification
PHONE_CLASS_ID = 67 

phone_currently_detected = False
frames_without_phone = 0
COOLDOWN_FRAMES = 15  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.5)
    boxes = results[0].boxes
    class_ids = boxes.cls

    phone_boxes = [box for i, box in enumerate(boxes) if int(class_ids[i]) == PHONE_CLASS_ID]
    phone_detected_this_frame = len(phone_boxes) > 0

    if phone_detected_this_frame:
        if not phone_currently_detected and frames_without_phone >= COOLDOWN_FRAMES:
            phone_detection_count += 1
            phone_currently_detected = True
            frames_without_phone = 0
            print(f"New phone detection! Total count: {phone_detection_count}/{N}")
        elif not phone_currently_detected:
            frames_without_phone = 0
    else:
        if phone_currently_detected:
            phone_currently_detected = False
            frames_without_phone = 0
        else:
            frames_without_phone += 1

    annotated_frame = frame.copy()
    for box in phone_boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(annotated_frame, "Phone", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.putText(annotated_frame, f"Phone detections: {phone_detection_count}/{N}", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(annotated_frame, f"Cooldown: {max(0, COOLDOWN_FRAMES - frames_without_phone)}", 
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Phone Detection", annotated_frame)

    if phone_detection_count >= N:
        print(f"DISQUALIFIED! Phone appeared {phone_detection_count} times.")
        cv2.putText(annotated_frame, "DISQUALIFIED!", (200, 240),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
        cv2.imshow("Phone Detection", annotated_frame)
        cv2.waitKey(3000)
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
