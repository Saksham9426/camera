import streamlit as st
from streamlit_webrtc import webrtc_streamer as wc
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC530c0ee59067abb9adf76f4cd45c6686'
auth_token = 'ceda7665bac1676818311da2c5a5c418
client = Client(account_sid, auth_token)

token = client.tokens.create()

print(token.username)

st.title('camera try')
wc(key='key',rtc_configuration={
      "iceServers": token.ice_servers
  })
