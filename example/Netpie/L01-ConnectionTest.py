# ---Import Library---
from network import WLAN,STA_IF
from simple import MQTTClient

# Network Credential
ssid = ''     # change
password = '' # change

# Network Interface 
wlan = WLAN(STA_IF)
wlan.active(True)

# ---Start Network Connection---
print('Connecting...')
wlan.connect(ssid,password)
while not wlan.isconnected():
    pass

# Connection Config
print('Connected!')
print('IP:',wlan.ifconfig()[0],
      '\nSubnet Mask:',wlan.ifconfig()[1],
      '\nDefault Gateway:',wlan.ifconfig()[2],
      '\nDNS:',wlan.ifconfig()[3])

# Netpie MQTT Credential
# (Get all credential from Netpie)
client_ID = ''               # <== change
token = ''                   # <== change
secret = ''                  # <== change
broker = 'mqtt.netpie.io'

# Set MQTT Profile
client = MQTTClient(client_ID,broker,
                    user=token,
                    password=secret)

# ---Start MQTT Connection---
print('Broker Connecting...')
client.connect()
print('Broker Connected!')







