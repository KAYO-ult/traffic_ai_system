lane_A = 0
lane_B = 0
lane_C = 0
lane_D = 0

def count_vehicles(detections, frame_width):

    global lane_A,lane_B,lane_C,lane_D

    lane_A = lane_B = lane_C = lane_D = 0

    for box in detections:

        x1,y1,x2,y2 = box
        center_x = int((x1+x2)/2)

        if center_x < frame_width*0.25:
            lane_A += 1

        elif center_x < frame_width*0.5:
            lane_B += 1

        elif center_x < frame_width*0.75:
            lane_C += 1

        else:
            lane_D += 1

    return lane_A,lane_B,lane_C,lane_D