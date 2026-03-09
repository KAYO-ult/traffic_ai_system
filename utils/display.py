import cv2
import numpy as np

def fix_frame(frame, w=640, h=480):

    if frame is None:
        frame = np.zeros((h, w, 3), dtype=np.uint8)

    if len(frame.shape) == 2:
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    frame = cv2.resize(frame, (w, h))

    return frame


def add_label(frame, text):

    cv2.putText(
        frame,
        text,
        (20, 40),                       # position
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),                  # yellow text
        2,
        cv2.LINE_AA
    )

    return frame


def display_four(f1, f2, f3, f4):

    f1 = fix_frame(f1)
    f2 = fix_frame(f2)
    f3 = fix_frame(f3)
    f4 = fix_frame(f4)

    # Label lanes
    f1 = add_label(f1, "Lane 1 - North")
    f2 = add_label(f2, "Lane 2 - East")
    f3 = add_label(f3, "Lane 3 - South")
    f4 = add_label(f4, "Lane 4 - West")

    top = cv2.hconcat([f1, f2])
    bottom = cv2.hconcat([f3, f4])

    screen = cv2.vconcat([top, bottom])

    return screen