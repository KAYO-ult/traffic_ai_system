from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")

# vehicle classes from COCO dataset
vehicle_classes = [2,3,5,7]

def detect(frame):

    results = model(frame)

    detections = []

    for r in results:

        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])

            if cls in vehicle_classes and conf > 0.4:

                x1,y1,x2,y2 = map(int,box.xyxy[0])

                detections.append([x1,y1,x2,y2])

                # get vehicle name
                name = model.names[cls]

                label = f"{name} {conf:.2f}"

                # draw bounding box
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

                # draw label
                cv2.putText(frame,
                            label,
                            (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0,255,0),
                            2)

    return detections