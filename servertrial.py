import socket
from functools import reduce
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6788

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

'''
creating 2 2d arrays that act as matrices ~ grid of 4 x 4   
each selects 2 spy spots
1st player to find all of other's spy location wins
'''

'''

SPY GRID :

assume nxn = 4x4 and k = 2
1. create a nxn grid 
2. let player 1 choose k spy spots which are marked as 1
    -> check if requested point in player 1's part of grid
    -> mark point as 1
3. let player 2 choose 2 spy spots which are marked as 2 
    -> check if requested point in player 2's part of grid
    -> mark point as 2
4. server sends a message to both players that the game is starting 
5. Player 1 is asked to choose 1st 
    -> if point is marked 2 , increment count1  & send msg of 1 spy spot found
    -> else send msg saying not found
6. Player 2 is asked to choose next
    -> if point is marked 1 , increment count2  & send msg of 1 spy spot found
    -> else send msg saying not found
7. Repeat 5 :
    -> if count1==2 , send msg to both saying Game over , Player 1 won !
   Repeat 6 :
    -> if count2==2, send msg to both saying Game over , Player 2 won !
   Repeat 7 till either condition satisfies
  
'''

#step 1
grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]




while True:
    data, addr = serverSock.recvfrom(1024)
    print ("Message: ", data)
    print("Addr: ",addr)
    print(addr[0])
    if(addr[0]=="127.0.0.1"): 
        print("received input from client 1")
        point = data.decode()
        coord=point.split(',')
        print(coord)
        x=int(coord[0])
        y=int(coord[1])
        
       # if(x in [0,1] and y in [0,1])
        # add condition for checking if point correct half of grid : 
        # for client 1 : 1st half of nxn grid -> rows 0 to n , cols 0 to n/2
        grid[x][y]=1  #fixing spy spot
    
    for i in grid :
        print(i)
    #modifiedMessage = data.decode().upper() 
    #serverSock.sendto(client1grid.encode(), addr) 
    