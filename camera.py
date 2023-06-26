import streamlit as st
from streamlit_webrtc import webrtc_streamer as wc
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

token = client.tokens.create()

print(token.username)

st.title('camera try')
wc(key='key',rtc_configuration={
      "iceServers": token.ice_servers
  })
