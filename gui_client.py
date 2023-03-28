import socket
import select
import tkinter as tk
from tkinter import messagebox as mb
global scores,marked,color,winner
global scores
scores={}

global marked
marked = [0]*16

global color
color = [0]*16

global winner
winner=0

global x
x=0

print("welcome")
UDP_IP='127.0.0.1'
UDP_PORT=6789

clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#clientSock.bind((UDP_IP,UDP_PORT))

name=input("Enter your name:")
clientSock.sendto(name.encode(), (UDP_IP, UDP_PORT))

server_conn=clientSock.recv(1024).decode()

opp_info = clientSock.recv(1024).decode().split(' ')
opp_info[1] = opp_info[1][2:-1]
print(opp_info)
print("You are playing against ", opp_info[1])


global my_spy
my_spy=input('Enter your choice of SPY grids(separater by ","): ').split(',')

def init(name, opp_info):
	global scores,marked,color,winner
	scores[name]=0
	scores[opp_info[1]]=0

def update(name, num):
	global scores,marked,color,winner
	int_num=int(num)
	button = buttons[int_num]
	marked[int_num] = 1
	print(" I am in UPDATE with value ",num)
	if(num in my_spy):
		color[int_num]='blue'
		button.config(bg="blue")
		scores[name] += 1
		scoremsg = "point scored for "+num
		print(scoremsg)

		print("I AM SENDING : ",scoremsg)
		clientSock.sendto(scoremsg.encode(), (opp_info[2], int(opp_info[3])))

	else:
		color[int_num]='red'
		button.config(bg="red")
		losemsg = "no point scored for "+num
		print(losemsg)
		aux_msg=True
		print("I AM SENDING : ",losemsg)
		clientSock.sendto(losemsg.encode(), (opp_info[2], int(opp_info[3])))
    
def no_winner(name, opp_name):
    global scores,marked,color,winner
    if(scores[name]==2 ):
        winner=1
        return False
    elif(scores[opp_name]==2):
        winner=2
        return False
    return True

def gameend():
    res=mb.askquestion('Game Over for '+name, 'Do you want to play another game ?')
    if res == 'yes' :
        print("----------------")
        print("Starting New Game")
        gameframe.pack_forget()
        gameframe.destroy()
        gameini.pack()
        print(my_spy)
    else :
        print("--------------")
        print("Quiting")
        quit()

# CORE!!!
init(name, opp_info)

def interact(send):

   
    print("you clicked ",send)

    if no_winner(name,opp_info[1]):
        if 'client1' in opp_info[0]:
            print("I AM SENDING : ",send)
            clientSock.sendto(send.encode(), (opp_info[2], int(opp_info[3])))
            rcvdata= clientSock.recv(1024)
            print("I AM RECEIVING from rcvdata: ",rcvdata)
            #below
            rcvdata=rcvdata.decode()
            if( not rcvdata.isdigit()):
                print("Recvd msg :",rcvdata)
                if("WON" in rcvdata):
                    print(rcvdata)
                    mb.showinfo("Game Status","You Won")
                    gameend()
                    return
                elif("no" not in rcvdata):
                    val=rcvdata[17:]
                    button = buttons[int(val)]
                    button.config(bg="green")
                else :
                    val=rcvdata[20:]
                    button = buttons[int(val)]
                    button.config(bg="red")				
                receive = clientSock.recv(1024).decode()
                print("I AM RECEIVING  from receive: ",receive)
                if(not receive.isdigit()):
                    print("Recvd msg :",receive)
                    if("WON" in receive):
                        print(receive)
                        mb.showinfo("Game Status","You Won")
                        gameend()
                        return
                    elif("no" not in receive):
                        val=receive[17:]
                        button = buttons[int(val)]
                        button.config(bg="green")
                    else :
                        val=receive[20:]
                        button = buttons[int(val)]
                        button.config(bg="red")

                else:
                    update(opp_info[1], receive)
            else:

                update(opp_info[1], rcvdata)
            
        else:
            rcvdata= clientSock.recv(1024)
            print("I AM RECEIVING from rcvdata: ",rcvdata)
            rcvdata=rcvdata.decode()
            if( not rcvdata.isdigit()):
                print("Recvd msg :",rcvdata)
                if("WON" in rcvdata):
                    print(rcvdata)
                    mb.showinfo("Game Status","You Won")
                    gameend()
                    return
                elif("no" not in rcvdata):
                    val=rcvdata[17:]
                    button = buttons[int(val)]
                    button.config(bg="green")
                else :
                    val=rcvdata[20:]
                    button = buttons[int(val)]
                    button.config(bg="red")				
                receive = clientSock.recv(1024).decode()
                print("I AM RECEIVING  from receive: ",receive)
                if(not receive.isdigit()):
                    print("Recvd msg :",receive)
                    if("WON" in receive):
                        print(receive)
                        mb.showinfo("Game Status","You Won")
                        gameend()
                        return
                    elif("no" not in receive):
                        val=receive[17:]
                        button = buttons[int(val)]
                        button.config(bg="green")
                    else :
                        val=receive[20:]
                        button = buttons[int(val)]
                        button.config(bg="red")
                else:
                    update(opp_info[1], receive)
            else:
                update(opp_info[1], rcvdata)
            print("I AM SENDING : ",send)
            clientSock.sendto(send.encode(), (opp_info[2], int(opp_info[3])))
            
        
    if not no_winner(name,opp_info[1]):
        
        winmsg="THE WINNER IS: " + opp_info[1]+" !! "
        print(winmsg)
        sendwin = "YOU WON"
        print("I AM SENDING : ",sendwin)
        print("YOU LOST")
        global x
        clientSock.sendto(sendwin.encode(), (opp_info[2], int(opp_info[3])))
        if(x==1):
            mb.showinfo("Game Status","You Lost")
            gameend()
        
        x=1
        return
        

root = tk.Tk()

root.title(name)


# GAME FRAME

# Set up a grid to hold the buttons
gameframe = tk.Frame(root, padx=10, pady=10)
gameframe.pack()

# Create and add the buttons to the grid
buttons = []
for i in range(16):
    button = tk.Button(gameframe, text=str(i))
    button.config(width=3, height=3, bg="white")
    button.grid(row=i//4, column=i%4)
    buttons.append(button)

    # Add button commands
    button.config(command=lambda i=i: interact(str(i)))


#GAME INITIALISE FRAME
gameini = tk.Frame(root,padx=10,pady=10)

# Run the GUI mainloop
root.mainloop()
