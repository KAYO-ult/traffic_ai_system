def decide_signal(A,B,C,D):

    lanes = {
        "A":A,
        "B":B,
        "C":C,
        "D":D
    }

    green_lane = max(lanes,key=lanes.get)

    return green_lane