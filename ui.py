from tkinter import *
from tkinter.messagebox import showinfo,askyesno
from tkinter.simpledialog import askstring
from PIL import *
import random
import time

window=Tk()
window.title("SPYGRID")
window.geometry("1500x1000")

def interact(send):
    print("you clicked ",send)

frame1=Frame(window)    # welcome page while we check if internet is there
frame2=Frame(window)    # main page
frame3=Frame(window)    # game page

bgIMG=PhotoImage("socket_bg.jpg")
bglabel=Label(frame1,image=bgIMG)
bglabel.place(x=0,y=0,relwidth=1,relheight=1)

buttons=[]

# b1=Button(frame1, text="button0", width=10, height=5, )

for i in range(16):
    num=str(i)
    buttons.append(Button(frame1, text=num, width=10, height=5, command=lambda x=num: interact(x)))

col=0

# count=0
# for i in range(4):
#     for j in range(4):
#         buttons[count].grid(row=j, column=i)
#         count += 1

for i in range(16):
    if i<4 :
        buttons[i].grid(row=i%4, column=0)
    elif i<8:
        buttons[i].grid(row=i%4, column=1)
    elif i<12:
        buttons[i].grid(row=i%4, column=3)
    else:
        buttons[i].grid(row=i%4, column=4)

empty_buttons=[]
for i in range(4):
    num=str(i)
    empty_buttons.append(Button(frame1, width=5, height=5))

for i in range(4):
    empty_buttons[i].grid(row=i, column=2)


frame1.pack()

window.mainloop()
# selectlabel=Label(frame2,)
