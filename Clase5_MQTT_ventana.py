import requests     #libreria para hacer peticiones a un http
from PyQt5.QtWidgets import QWidget,QApplication, QLabel, QPushButton, QProgressBar,QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import json         #para manerar el formato json  

#Para trabajar con MQTT
import paho.mqtt.client as mqtt


class App(QWidget):
    def __init__(self):   #constructor
        super().__init__()
        self.h = 400
        self.w = 600
        self.titulo = "UMAKER"
        self.a = 100
        self.b = 100
        self.initUI()

    def initUI(self):    #defino los metodos 
        self.setWindowTitle(self.titulo)
        self.setGeometry(self.a,self.b,self.w,self.h)

        self.font = QFont()    #formato para el label de titulo
        self.font.setPointSize(11)  # Tamaño de la letra
        self.font.setBold(True)    # Negrita

        self.labelt = QLabel("Monitoreo IOT con MQTT",self)   #label de titulo
        self.labelt.move(175,50)
        self.labelt.setFont(self.font)

        self.label1 = QLabel("Mensaje recibido: Ninguno",self)   #etiqueta
        self.label1.move(210,200)
       
        self.bar1 = QProgressBar(self)    #barra1 que indica el valor del sensor pot
        self.bar1.setGeometry(185, 250, 250, 30)
        self.bar2 = QProgressBar(self)    #barra2 que indica el valor del sensor ultrasónico
        self.bar2.setGeometry(185, 300, 250, 30)

        s1 = QSlider(Qt.Horizontal,self)
        s1.setGeometry(70,80,400, 30)
        s1.setMaximum(100)
        s1.setMinimum(0)
        #s1.valueChanged.connect(self.datos)
     
        self.show()


    def initMQTT(self):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)   #Instanciamos client para manejar MQTT
        
        
        self.client.on_connect = self.on_connect  #para conectar a un broker
        self.client.on_message = self.on_message  #para procesar mensajes

        self.client.connect("192.168.18.139", 1883)
        self.client.loop_start()

    
    def on_connect(self, client, userdata, flags, rc, p):
        print("Conectado al broker")
        self.client.subscribe("canalx")  #se subscribe con el topico
    

    def on_message(self, client, userdata, msg):
        mensaje = msg.payload.decode()
        print(mensaje)
        self.label1.setText("Mensaje recibido: "+mensaje)

if __name__ == "__main__":  #ejecuta la aplicación
    app = QApplication([]) 
    ex = App()
    app.exec_()


