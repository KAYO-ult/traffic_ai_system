import cv2
import json

from detection.detect_vehicles import detect
from counting.vehicle_counter import count
from traffic_logic.signal_controller import decide_signal
from utils.display import display_four

cap1 = cv2.VideoCapture("videos/lane1.mp4")
cap2 = cv2.VideoCapture("videos/lane2.mp4")
cap3 = cv2.VideoCapture("videos/lane3.mp4")
cap4 = cv2.VideoCapture("videos/lane4.mp4")

while True:

    r1,f1 = cap1.read()
    r2,f2 = cap2.read()
    r3,f3 = cap3.read()
    r4,f4 = cap4.read()

    if not r1 or not r2 or not r3 or not r4:
        break

    det1 = detect(f1)
    det2 = detect(f2)
    det3 = detect(f3)
    det4 = detect(f4)

    A = count(det1)
    B = count(det2)
    C = count(det3)
    D = count(det4)

    green = decide_signal(A,B,C,D)

    traffic_data = {
        "lane_A":A,
        "lane_B":B,
        "lane_C":C,
        "lane_D":D,
        "green_lane":green
    }

    with open("data/traffic_data.json","w") as f:
        json.dump(traffic_data,f)

    screen = display_four(f1,f2,f3,f4)

    cv2.putText(screen,f"A:{A}  B:{B}  C:{C}  D:{D}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,255),
                2)

    cv2.putText(screen,f"Green Lane: {green}",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2)

    cv2.imshow("AI Traffic Monitoring",screen)

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()