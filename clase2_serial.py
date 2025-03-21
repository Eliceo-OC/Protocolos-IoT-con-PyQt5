#libreria para usar la comunciacion serial
import serial
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QLabel, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

#creamos clase App para las ventanas, esta hereda métodos de QWidget
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "monitoreo"
        self.a = 200
        self.b = 200
        self.h = 600
        self.w = 300
        self.cont = 0
        self.initUI()
        self.initSerial()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.a,self.b,self.h,self.w)

        self.labelt = QLabel("Monitoreo con PyQt5 y ESP32",self)
        self.labelt.move(160,50)
        self.labelt.setFont( QFont("Tahoma", 11) )

        #labels
        self.label1 = QLabel("Temperatura",self)
        self.label1.move(140,100)
        self.label2 = QLabel("Humedad",self)
        self.label2.move(360,100)
        
        #Progressbar
        self.bar = QProgressBar(self)
        self.bar.setGeometry(90, 125, 200, 30)
        self.bar.setMaximum(100)
        self.bar.setMinimum(0)

        self.bar2 = QProgressBar(self)
        self.bar2.setGeometry(310, 125, 200, 30)
        self.bar2.setMaximum(100)
        self.bar2.setMinimum(0)

        #labels
        self.label3 = QLabel("Valor: 0",self)
        self.label3.move(150,160)
        self.label4 = QLabel("Valor: 0",self)
        self.label4.move(360,160)
        self.label5 = QLabel("Control de led",self)
        self.label5.move(225,190)

        #botones
        boton1 = QPushButton("Prender", self)
        boton1.move(175, 215)
        boton1.clicked.connect(self.prender)  #llama a evento prender al clickear
        
        boton2 = QPushButton("Apagar", self)
        boton2.move(275, 215)
        boton2.clicked.connect(self.apagar)   #llama a evento apagar al clickear

        #temporizador 
        timer = QTimer(self)
        timer.timeout.connect(self.read_datos) #llama a metodo
        timer.start(1000) #tiempo 

        #mostrar
        self.show()


    #metodos al presionar botones
    def prender(self):
        print("Led prendido")
        data = "a"
        self.esp.write(data.encode())

    def apagar(self):
        print("Led apagado")
        data = "b"
        self.esp.write(data.encode())

    #metodo del timer para leer datos y mostrar en la progressbar
    def read_datos(self):
        if self.esp.in_waiting>0 : #detecta si hay datos disponibles
            #lee el mensaje y le da formato para ser impreso
            msg1= int( self.esp.readline().decode().strip().split(",")[0] ) 
            msg2= int( self.esp.readline().decode().strip().split(",")[1] )
            
            print(msg1, msg2) 
            
            self.bar.setValue(int(msg1))  #imprime en la progress bar
            self.label3.setText(f"Valor: {msg1}") #imprime en la etiqueta
            self.label3.adjustSize()
            
            self.bar2.setValue(int(msg2))  #imprime en la progress bar
            self.label4.setText(f"Valor: {msg2}") #imprime en la etiqueta
            self.label4.adjustSize()

    #metodo para la comunicacion serial
    def initSerial(self):
        self.esp = serial.Serial("COM7", 9600)



#ejecuta la aplicación
if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    app.exec_()
    



"""""



#CODIGO PARA LEER Y ENVIAR MENSAJES CON LA ESP32

#creamos objeto con los parametros de la comunicación
PORT = "COM7"
esp32 = serial.Serial(PORT, 9600)

while True:
    msg = esp32.readline()  #guardamos lectura en msg
    print(msg.decode().strip().split(","))
    data = input("Ingrese un valor a o b: ") #variable string
    if data == "x":
        break

    esp32.write(data.encode()) #mandamos bytes con el metodo encode


"""""


    