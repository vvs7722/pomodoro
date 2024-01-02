from tkinter import *
from tkinter import messagebox
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
brk='✅'
star=""
reps=0
work_count=0
start_time=time.time()
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    win.after_cancel(timer)
    global reps
    reps=0
    can.itemconfig(timer_text,text="00:00")
    lab.config(text="Timer")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    global WORK_MIN 
    global SHORT_BREAK_MIN 
    global LONG_BREAK_MIN 
    global star
    global work_count
    reps+=1
    if reps%8==0:
        work_count+=1
        lab.config(text="LONG BREAK /n{work_count}",fg=RED)
        ct(LONG_BREAK_MIN*60)
        #class tkinter.messagebox.Message(master=None,**options)
        messagebox.showwarning("showwarning","LONG BREAK")
        
    elif reps%2!=0:
        work_count+=1
        lab.config(text=f"WORK {work_count}",fg=GREEN)
        ct(WORK_MIN*60)
        messagebox.showwarning("showwarning","WORK")
        
        
    else:
        ct(SHORT_BREAK_MIN*60)
        lab.config(text=f"BREAK {work_count}",fg=RED)
        messagebox.showwarning("showwarning","BREAK")

    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def ct(count):
    c_min=int(count/60)
    c_sec=count%60
    if c_sec<10:
        c_sec="0"+str(c_sec)
    can.itemconfig(timer_text,text=f"{c_min}:{c_sec}")
    if count>0:
        global timer
        timer=win.after(1000,ct,count-1)
    else:
        start()
# ---------------------------- UI SETUP ------------------------------- #
win=Tk()
win.config(padx=50,pady=50,bg=YELLOW)

win.title("timer")
lab=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,25,'bold'),pady=15)
lab.grid(column=1,row=0)
can=Canvas(width=230,height=230,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
can.create_image(100,112,image=img)
timer_text=can.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
can.grid(column=1,row=1)
but=Button(text="Start",highlightthickness=0,command=start)
but.grid(column=0,row=2)
but1=Button(text="Reset",highlightthickness=0,command=reset)
but1.grid(column=3,row=2)
win.mainloop()
