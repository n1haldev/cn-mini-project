import socket
import time

UDP_IP_ADDRESS = '192.168.43.26'
UDP_PORT_NO = 6789

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
	clients=[]
	names=[]

	while True:
		data, addr = serverSock.recvfrom(1024)
		clients.append(addr)
		names.append(data)
		serverSock.sendto(str.encode("connected to server"), addr)

		if len(clients)==2:
			break

	client1=clients.pop()
	name1=names.pop()
	client1_addr, client1_port=client1
	client2=clients.pop()
	name2=names.pop()
	client2_addr, client2_port=client2

	# serverSock.sendto(name1, client2)
	# serverSock.sendto('client1', client2)
	serverSock.sendto('"client1" {} {} {} {}'.format(name1, client1_addr, client1_port, UDP_PORT_NO).encode(), client2)
	# serverSock.sendto(name2, client1)
	serverSock.sendto('"client2" {} {} {} {}'.format(name2, client2_addr, client2_port, UDP_PORT_NO).encode(), client1)
