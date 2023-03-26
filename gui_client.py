import socket
import tkinter as tk
global scores,marked,color,winner
global scores
scores={}

global marked
marked = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

global color
color = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

global winner
winner=0

print("welcome")
UDP_IP='127.0.0.1'
UDP_PORT=6789

clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# clientSock.bind((UDP_IP,UDP_PORT))

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
    if(num in my_spy):
        color[int_num]='green'
        button.config(bg="green")
        scores[name] += 1
        print(name+" scores a point ")
    else:
        color[int_num]='red'
        button.config(bg="red")
    
def no_winner(name, opp_name):
    global scores,marked,color,winner
    if(scores[name]==2):
        winner=1
        return False
    elif(scores[opp_name]==2):
        winner=2
        return False
    return True

# CORE!!!
init(name, opp_info)

def interact(send):
    print("you clicked ",send)
    if no_winner(name,opp_info[1]):
        if 'client1' in opp_info[0]:

            clientSock.sendto(send.encode(), (opp_info[2], int(opp_info[3])))
            update(name, send)
            receive = clientSock.recv(1024).decode()
            if(int(send) < 8):
                update(opp_info[1], receive)
        else:
            
            receive = clientSock.recv(1024).decode()
            update(opp_info[1], receive)
            
            clientSock.sendto(send.encode(), (opp_info[2], int(opp_info[3])))
            if(int(send) >= 8):
                update(name, send)
        
    if not no_winner(name,opp_info[1]):
       print("THE WINNER IS: "+opp_info[1])
       quit()
        # Set up the Tkinter GUI
root = tk.Tk()

root.title(name)

# Set up a grid to hold the buttons
grid = tk.Frame(root, padx=10, pady=10)
grid.pack()

# Create and add the buttons to the grid
buttons = []
for i in range(16):
    button = tk.Button(grid, text=str(i))
    button.config(width=3, height=3, bg="white")
    button.grid(row=i//4, column=i%4)
    buttons.append(button)

    # Add button commands
    button.config(command=lambda i=i: interact(str(i)))

# Run the GUI mainloop
root.mainloop()
