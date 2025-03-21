import socket

while True:
    #creamos el cliente que se conectara al wifi
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(("192.168.18.211", 8000)) #nos conectamos a la ip de la esp32

    #envio y recepcion de datos
    msg = input("Ingrese x o y: ")
    if msg == "a":
        break
    cliente_socket.sendall(msg.encode())  #envio
    data = cliente_socket.recv(1024) #recepcion
    print("El valor recibido es ", data.decode()) #decode pasa de bytes a bits 
cliente_socket.close()