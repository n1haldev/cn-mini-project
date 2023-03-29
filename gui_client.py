import socket
from tkinter import *
from tkinter.messagebox import showinfo, askquestion
from tkinter.simpledialog import askstring

global scores, marked, color, winner

scores={}
marked=[0]*16
color=[0]*16
winner=0

global x
x=0

UDP_IP='127.0.0.1'
UDP_PORT=6789

def initiate(entry):
    global name, opp_info
    name=entry
    global clientSock
    clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    clientSock.sendto(name.encode(), (UDP_IP, UDP_PORT))

    server_conn=clientSock.recv(1024).decode()

    opp_info = clientSock.recv(1024).decode().split(',')
    opp_info[1] = opp_info[1][2:-1]
    print(opp_info)

    showinfo("Player Found", "You are playing against %s" % opp_info[1])

    global my_spy
    my_spy=askstring("Enter your choice", 'Enter your choice of SPY grids(separater by ","): ').split(',')
    showinfo("Your choice", "{} and {}".format(my_spy[0], my_spy[1]))

    scores[name]=0
    scores[opp_info[1]]=0

    welcome_frame_to_gameframe()


def welcome_frame_to_gameframe():
    welcome_frame.pack_forget()

    # Create and add the buttons to the grid
    global buttons
    buttons = []
    for i in range(16):
        button = Button(gameframe, text=str(i))
        button.config(width=3, height=3, bg="white")
        button.grid(row=i//4, column=i%4)
        buttons.append(button)

        # Add button commands
        button.config(command=lambda i=i: interact(str(i)))

    gameframe.pack()

def no_winner(name, opp_name):
    global scores,marked,color,winner
    if(scores[name]==2 and scores[opp_name]==2):
        winner=3
        return False
    elif(scores[name]==2 ):
        winner=1
        return False
    elif(scores[opp_name]==2):
        winner=2
        return False
    return True

def interact(send):
  
    print("you clicked ",send)

    if no_winner(name,opp_info[1]):
        if 'client1' in opp_info[0]:
            print("I AM SENDING : ",send)
            clientSock.sendto(send.encode(), (opp_info[2], int(opp_info[3])))
            onreceive()
            
        else:
            onreceive()
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
            showinfo("Game Status","You Lost")
            gameend()
     
        x=1
        return


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


def onreceive():
    rcvdata= clientSock.recv(1024)
    print("I AM RECEIVING from rcvdata: ",rcvdata)
    #below
    rcvdata=rcvdata.decode()
    if( not rcvdata.isdigit()):
        print("Recvd msg :",rcvdata)
        if("WON" in rcvdata):
            print(rcvdata)
            showinfo("Game Status","You Won")
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
                showinfo("Game Status","You Won")
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

def gameend():
    res=askquestion('Game Over for '+name, 'Do you want to play another game ?')
    if res == 'yes' :
        print("----------------")
        print("Starting New Game")
        gameframe.pack_forget()
        #gameframe.destroy()
        clientSock.close()
        initiate(name)

    else :
        print("--------------")
        print("Quiting")
        quit()


# GUI
window=Tk()
window.title("SPY GRID")
window.geometry("1500x1000")

welcome_frame=Frame(window)
gameframe=Frame(window, padx=100, pady=200)

welcome_l=Label(welcome_frame, text="Welcome to spy grid!\n How would you like to be known as?")
welcome_l.pack()

name_entry=Entry(welcome_frame, width=40)
name_entry.pack()

submit_b=Button(welcome_frame, text="Submit", width=10, height=2, command=lambda:initiate(name_entry.get()))
submit_b.pack()

welcome_frame.pack()

window.mainloop()
