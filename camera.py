import streamlit as st
from streamlit_webrtc import webrtc_streamer as wc
st.title('camera try')
wc(key='key', rtc_configuration={  # Add this config
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}])
