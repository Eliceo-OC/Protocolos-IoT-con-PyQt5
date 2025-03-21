import requests     #libreria para hacer peticiones a un http
from PyQt5.QtWidgets import QWidget,QApplication, QLabel, QPushButton, QProgressBar
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
import json         #para manerar el formato json  

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

        self.labelt = QLabel("Monitoreo IOT con HTTP",self)   #label de titulo
        self.labelt.move(175,50)
        self.labelt.setFont(self.font)

        boton1 = QPushButton("Realizar petición: ", self)   #boton
        boton1.move(225,125)
        #boton1.clicked.connect(self.on_click)

        self.label1 = QLabel("Informacion de sensores",self)   #etiqueta
        self.label1.move(210,200)
       
        self.bar1 = QProgressBar(self)    #barra1 que indica el valor del sensor pot
        self.bar1.setGeometry(185, 250, 250, 30)
        self.bar2 = QProgressBar(self)    #barra2 que indica el valor del sensor ultrasónico
        self.bar2.setGeometry(185, 300, 250, 30)

        #temporizador 
        timer = QTimer(self)
        timer.timeout.connect(self.read_datos) #llama a metodo
        timer.start(3000) #tiempo 

        
        self.show()

    def read_datos(self):       #evento al presionar boton
        r = requests.get("http://192.168.18.211:8080/IOT")
        
        if r.status_code == 200:     #hacemos la peticion al http
            print("Respuesta exitosa")
            print(r.text)             #imprimimos json convertido a string

            data = json.loads(r.text)  #convertimos el String a diccionario

            self.label1.setText(r.text)  
            self.label1.adjustSize()  #para ajustar el texto de la etiqueta
            self.label1.move(170,200)
            self.bar1.setValue(int(data['POT1']))  #colocamos el POT1 del 
            self.bar2.setValue(int(data['DISTANCIA']))  #colocamos el POT1 del diccionario


if __name__ == "__main__":  #ejecuta la aplicación
    app = QApplication([]) 
    ex = App()
    app.exec_()


