from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global rep
    window.after_cancel(timer)
    rep = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rep
    rep += 1

    if rep % 8 == 0:
        label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif rep % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        work_sessions = math.floor(rep/2)
        marks = ""
        for i in range(work_sessions):
            marks += "✔️"
        check_marks.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width = 200, height = 224, bg= YELLOW, highlightthickness= 0)
tomato = PhotoImage(file= "tomato.png")
canvas.create_image(100,112,image = tomato)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

start_button = Button(text="Start", command = start_timer)
start_button.grid(column = 0, row = 2)

start_button = Button(text="Reset")
start_button.grid(column = 2, row = 2)

label = Label(text= "Timer", fg= GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(column = 1, row = 0)

check_marks = Label(bg=YELLOW, fg= GREEN, font=(FONT_NAME,20, "bold"))
check_marks.grid(column = 1, row =3)

window.mainloop()