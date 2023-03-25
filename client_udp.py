import socket
import time

global scores
scores={}

global marked
marked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

global color
color = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

global winner
winner=0

print("nihal is good".split())
UDP_IP='192.168.43.26'
UDP_PORT=6789

clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# clientSock.bind((UDP_IP,UDP_PORT))

name=input("Enter your name:")
clientSock.sendto(name.encode(), (UDP_IP, UDP_PORT))

server_conn=clientSock.recv(1024).decode()

opp_info = clientSock.recv(1024).decode().split(' ')

print("You are playing against ", opp_info[1])
global my_spy
my_spy=input('Enter your choice of SPY grids(separater by ","): ').split(',')

def init(name, opp_info):
    scores[name]=0
    scores[opp_info[1]]=0

def update(name, num):
    int_num=int(num)
    marked[int_num] = 1
    if(num in my_spy):
        color[int_num]='green'
        scores[name] += 1
        print("someone scored a point ", name)
    else:
        color[int_num]='red'

def no_winner(name, opp_name):
    if(scores[name]==2):
        winner=1
        return False
    elif(scores[opp_name]==2):
        winner=2
        return False
    return True

# CORE!!!
init(name, opp_info)

print(opp_info)         # put code in while loop in a function called on button click(interact(send))
while no_winner(name,opp_info[1]):     # replace while with if
    send = input("Guess opponents SPY GRID(separated by ','): ")    # this send will come as argument in func interact(send)
    if 'client1' in opp_info[0]:
        if(int(send) < 8):
            # alert("You cannot select a grid from your own space!")
            continue

        clientSock.sendto(send.encode(), (opp_info[2], int(opp_info[3])))
        update(name, send)
        receive = clientSock.recv(1024).decode()
        update(opp_info[1], receive)
    else:
        receive = clientSock.recv(1024).decode()
        update(opp_info[1], receive)
        if(int(send) >= 8):
            # alert("You cannot select a grid from your own space!")
            continue
        clientSock.sendto(send.encode(), (opp_info[2], int(opp_info[3])))
        update(name, send)

# So we do have a winner which is why the loop broke!
if winner==1:
    print("Congrats You won!")
    clientSock.sendto(str.encode("loss"), (opp_info[2], int(opp_info[3])))
    exit()
    # alert("Congrats you won!")
    
elif winner==2:
    print("You lost :(")
    clientSock.sendto(str.encode("win"), (opp_info[2], int(opp_info[3])))
    exit()
    #alert("Your opponent won!")

# while True:
#     server_conn=clientSock.recv(1024).decode()

#     oppo_name=clientSock.recv(1024).decode()
#     oppo_info=clientSock.recv(1024).decode().split(' ')

#     my_spy=input('Enter your choice of SPY grids(separater by ","): ').split(',')

