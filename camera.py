import streamlit as st
from streamlit_webrtc import webrtc_streamer as wc
import os
from twilio.rest import Client
import config
from streamlit_player import st_player
import eel
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config.TWILIO_ACCOUNT_SID
auth_token = config.TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

token = client.tokens.create()

print(token.username)

st.title('camera try')
wc(key='key',rtc_configuration={
      "iceServers": token.ice_servers
  })
@eel.expose
def song():
      time.sleep(20)
      return 1

eel.start('new.html')
