import cv2
import json

from detection.detect_vehicles import detect
from counting.vehicle_counter import count_vehicles
from traffic_logic.signal_controller import decide_signal

cap = cv2.VideoCapture("videos/traffic.mp4")

while True:

    ret,frame = cap.read()

    if not ret:
        break

    detections = detect(frame)

    frame_width = frame.shape[1]

    A,B,C,D = count_vehicles(detections,frame_width)

    green_lane = decide_signal(A,B,C,D)

    traffic_data = {
        "lane_A":A,
        "lane_B":B,
        "lane_C":C,
        "lane_D":D,
        "green_lane":green_lane
    }

    with open("data/traffic_data.json","w") as f:
        json.dump(traffic_data,f)

    cv2.imshow("Traffic Monitoring",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()