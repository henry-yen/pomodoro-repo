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
    global count
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global rep
    rep = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    if rep % 8 == 0:
        count_down(60 * LONG_BREAK_MIN)
        timer_label.config(text="Break", fg=RED)
    elif rep % 2 == 0:
        count_down(60 * SHORT_BREAK_MIN)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(60 * WORK_MIN)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(rep / 2)
        for _ in range (work_session):
            marks += "✔"
            check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("🍅Pomodoro")
window.config(width=400, height=400, padx=50, pady=20, bg=YELLOW)

#Canvas
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=3, row=2)
#Start_Button
start_btn = Button(
    text="Start",
    highlightthickness=0,
    command=start_timer
)
start_btn.grid(column=0, row=3)

#Reset_Button
reset_btn = Button(
    text="Reset",
    highlightthickness=0,
    command=reset_timer
)
reset_btn.grid(column=4, row=3)

#check_label
check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=3, row=3)

#timer_label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=3, row=0)


window.mainloop()