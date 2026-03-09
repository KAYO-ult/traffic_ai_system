import streamlit as st
import json
import time

st.title("AI Smart Traffic Control Dashboard")

placeholder = st.empty()

while True:

    with open("data/traffic_data.json") as f:
        data = json.load(f)

    with placeholder.container():

        col1,col2 = st.columns(2)

        with col1:
            st.metric("Lane A",data["lane_A"])
            st.metric("Lane B",data["lane_B"])

        with col2:
            st.metric("Lane C",data["lane_C"])
            st.metric("Lane D",data["lane_D"])

        st.success(f"Green Signal → Lane {data['green_lane']}")

    time.sleep(1)