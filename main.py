from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps=0
timer=None
duration=1

def reset_timer():
    window.after_cancel(timer)
    label.config(text = "Timer")
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps=0

def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60*duration
    short_brk_sec = SHORT_BREAK_MIN * 60 * duration
    long_brk_sec = LONG_BREAK_MIN * 60 * duration
    if reps%2==0:
        if reps%8==0:
            label.config(text="Break", fg=RED)
            countdown(long_brk_sec)
        else:
            label.config(text="Break", fg=PINK)
            countdown(short_brk_sec)
    elif reps%2==1:
        label.config(text="Work", fg=GREEN)
        countdown(work_sec)

def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec==0:
        count_sec = "00"
    elif count_sec<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count-1)
    if count==0:
        start_timer()
        marks=""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks+="✔"
        checkmark_label.config(text = marks)

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg = YELLOW)

def radio_used():
    global duration
    duration=radio_state.get()
radio_state = IntVar()
radiobutton1 = Radiobutton(text="25 min", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="50 min", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1,row=4)
radiobutton2.grid(column=1,row=5)

canvas = Canvas(width=200, height = 224, bg = YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_image)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME,36,"bold"))
canvas.grid(column=1, row = 1)

label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME,36,"bold"))
label.grid(column = 1, row = 0)

start_button = Button(text = "Start", command = start_timer)
start_button.grid(column=0, row = 2)

reset_button = Button(text = "Reset",command = reset_timer)
reset_button.grid(column=2, row = 2)

checkmark_label = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME,20,"bold"))
checkmark_label.grid(column = 1, row = 3)

window.mainloop()