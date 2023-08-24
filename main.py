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
reps = 1
checkmarks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global checkmarks
    reps = 1
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks = ""
    check_mark.config(text=checkmarks)
    canvas.itemconfig(timer_text,text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    if reps % 8 == 0:
        timer_label.config(fg=RED, text="Break")
        count_down(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        timer_label.config(fg=PINK, text="Break")
        count_down(SHORT_BREAK_MIN * 60)

    else:
        timer_label.config(fg=GREEN, text="WORK")
        count_down(WORK_MIN * 60)



def count_down(count):
    global reps
    global checkmarks
    if count < 0:
        reps +=1
        start_timer()
        if reps % 2==0:
            checkmarks +="✔"
            check_mark.config(text=checkmarks)

    else:
        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"
        canvas.itemconfig( timer_text,text=f"{minutes}:{seconds}")
        print(count)
        global timer
        timer = window.after(1000, count_down, count - 1)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)
timer_label = Label(text="Timer", fg= GREEN, font = (FONT_NAME, 45, 'normal'), bg = YELLOW, pady = 10)
timer_label.grid(column = 2, row= 1)
canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font = (FONT_NAME, 35, 'bold'))
canvas.grid(row = 2, column =2)
button_start = Button(text="Start", highlightbackground=YELLOW, command = start_timer)
button_start.grid(column=1, row=3)
button_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(row=3, column = 3)
check_mark = Label(text="", font=("Arial", 15, 'normal'), fg=GREEN, bg=YELLOW)
check_mark.grid(row=4, column=2)
mainloop()
