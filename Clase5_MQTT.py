import paho.mqtt.publish as publish

#Publicador
publish.single("canaly", "Hola", hostname = "192.168.18.139")  #topico, payload, IPBroker


