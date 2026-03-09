from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

vehicle_classes = [2,3,5,7]
# car, motorcycle, bus, truck


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

    return detections