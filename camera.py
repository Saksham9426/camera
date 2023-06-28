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


st.components.v1.html(
      """<html> 
<body> 

<audio id="audio" autoplay>
    <source src="https://drive.google.com/file/d/1H7yXAC1BNPAq7MEmdYLXrRkFq9vhOwiO/preview?usp=sharing">
    
</audio>
<script> 
let audio = document.getElementById("audio"); 
let playlist = [
    'https://drive.google.com/file/d/1jrV4cd9nZETOE9htso-xfFrpZEzLzkkh/preview?usp=sharing',
    'https://drive.google.com/file/d/1cAqTnZ-gHXeJ5tOvY3Wai_ORr3uAZKln/view?usp=sharing',
];
async function getTime() {
                let value = await eel.song()();
                if (value == 1)
                audio.src = playlist[1];
                if (value == 2)
                audio.src = playlist[0];
                audio.play()
            }
</script> 

</body> 
</html>
"""
)
