import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("canaly", hostname = "192.168.18.139")
print( msg.payload.decode() )