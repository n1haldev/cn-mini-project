from socket import * 

TCP_IP='192.168.18.171'
serverPort = 12000 
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind((TCP_IP,serverPort))
serverSocket.listen(1) 
print ('The server is ready to receive')

while True:
     clients=[]
     while True: 
          connectionSocket, addr = serverSocket.accept()
          clients.append(addr)
          
          if len(clients)==2:
               break
     
     clinet1=clients
     
connectionSocket.close()