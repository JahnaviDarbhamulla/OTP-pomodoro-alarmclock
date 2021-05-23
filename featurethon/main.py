# ---------------------------------------------------Libraries-----------------------------------------

from tkinter import *
from tkinter import simpledialog
# Importing all the necessary libraries to form the alarm clock:
from time import sleep
import datetime
import time
import winsound
from os import system, name
import math

# -------------------------------------------------------Global variables-------------------------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

reps = 0
timer = None

FONT = ("Helevetica", 10, "bold")
ORANGE = "#f45c43"
REPS = 0
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')


# ------------------------------------------------------------WINDOW---------------------------------------------------------
# created a window
window = Tk()
window.title("On Time App")
window.minsize(width="550", height="550")

# created a canvas
canvas = Canvas(width="600", height="700", highlightthickness=0)
home_img = PhotoImage(file="home_page.png")

# Home page image
image_id = canvas.create_image(300, 300, image=home_img)
# images
work_img = PhotoImage(file="Work.png")
break_img = PhotoImage(file="break.png")
alarm_img = PhotoImage(file="alarm_clock.png")
image4 = PhotoImage(file="home_page.png")

canvas.grid(row="1", column="2")

# ------------------------------------------------------------WELCOME----------------------------------------------------------

# welcome text

welcome = canvas.create_text(300, 300, text="          Welcome to\n On Time Presence App!", fill="#003973",
                             font=("Arial", 25, "bold"))

USER_INP = simpledialog.askstring(title="Test", prompt="What's your Name ? ")
FOCUS_INP = simpledialog.askstring(title="Test", prompt="What is your main focus for today ? ")

# hiding welcome text to access home page
canvas.itemconfigure(welcome, state='hidden')


# ------------------------------------------------------------HOME PAGE---------------------------------------------------------

def on_click_pomodoro():
    canvas.itemconfigure(hello, fill="#003973")
    Pomodoro_button.place_forget()
    Alarm_button.place_forget()
    start_button.place(x=100, y=500)
    reset_button.place(x=350, y=500)
    home_btn.place(x=220, y=650)
    canvas.itemconfigure(real_time, state="hidden")
    canvas.itemconfigure(clock, state="normal")
    canvas.itemconfigure(image_id, image=work_img)


def home_page():
    check_marks.place_forget()

    canvas.itemconfigure(image_id, image=home_img)
    start_button.place_forget()
    reset_button.place_forget()
    home_btn.place_forget()
    canvas.itemconfigure(real_time, state="normal")
    canvas.itemconfigure(clock, state="hidden")
    Alarm_button.place(x=303, y=75)

    Pomodoro_button.place(x=25, y=75)
    canvas.itemconfig(title_pomo, title="")



# ---------------------------------------Real time clock-----------------------------------
real_time = canvas.create_text(300, 300, fill="#003973", font=("Arial", 55, "bold"))


def digitalclock():
    now = time.strftime("%H:%M:%S")
    canvas.itemconfig(real_time, text=now)
    canvas.after(200, digitalclock)


digitalclock()


# clock and hello for all pages


# --------------------------------------------------------POMODORO------------------------------------------------------
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(clock, text="00:00")

    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
clock = canvas.create_text(300, 300, text="00:00", fill="#003973", font=("Arial", 55, "bold"))
canvas.itemconfigure(clock, state="hidden")
hello = canvas.create_text(300, 360, text=f"Hello {USER_INP}", font=("Arial", 30, "bold"))
focus = canvas.create_text(300, 410, text=f"Your main focus for today is {FOCUS_INP}", font=("Arial", 15, "bold"))
title_pomo = canvas.create_text(300, 150, text="", fill="#003973",
                                font=("Arial", 25, "bold"))


def raise_above_all():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


def start_timer():
    global reps
    reps += 1
    canvas.itemconfigure(image_id, image=work_img)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        canvas.itemconfig(title_pomo, text="Break")
        canvas.itemconfigure(image_id, state='hidden')
        canvas.itemconfigure(image_id, image=break_img)
        raise_above_all()


    elif reps % 2 == 0:
        count_down(short_break_sec)
        canvas.itemconfig(title_pomo, text="Break")
        canvas.itemconfigure(image_id, image=break_img)
        raise_above_all()

    else:
        count_down(work_sec)
        canvas.itemconfigure(image_id, image=work_img)
        canvas.itemconfig(title_pomo, text="Work")
        raise_above_all()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(clock, text=f"{count_min}:{count_sec}", )
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


# title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
# title_label.place(x = 300,y= 300)


start_button = Button(text="Start", highlightthickness=0, command=start_timer, width=20,
                      height=1, bd='4', font=("Arial", 10, "bold"), bg="#b0dab9")
start_button.place_forget()

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, width=20,
                      height=1, bd='4', font=("Arial", 10, "bold"), bg="#b0dab9")
reset_button.place_forget()

check_marks = Label(fg=GREEN, bg="black")
check_marks.place(x=200, y=600)

# Pomodoro button
Pomodoro_button = Button(window, text='Pomodoro', width=33,
                         height=2, bd='4', font=("Arial", 10, "bold"), bg="#fbaccc", command=on_click_pomodoro)
Pomodoro_button.place(x=25, y=75)

home_btn = Button(text="Home Page", highlightthickness=0, width=20,
                  height=1, bd='4', font=("Arial", 10, "bold"), bg="#b0dab9", command=home_page)
home_btn.place_forget()


# -------------------------------------------------------------ALARM CLOCK----------------------------------------------


def On_click_alarm():
    check_marks.place_forget()

    real_time = canvas.create_text(300, 300, fill="#003973", font=("Arial", 55, "bold"))

    def digitalclock():
        now = time.strftime("%H:%M:%S")
        canvas.itemconfig(real_time, text=now)
        canvas.after(200, digitalclock)

    digitalclock()

    def raise_above_all():
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)

    def home_alarm():

        canvas.itemconfigure(image_id, image=home_img)
        start_button.place_forget()
        reset_button.place_forget()
        home_btn.place_forget()
        canvas.itemconfigure(real_time, state="normal")
        canvas.itemconfigure(clock, state="hidden")
        Alarm_button.place(x=303, y=75)

        Pomodoro_button.place(x=25, y=75)
        check_marks.config(text="")
        time_format.place_forget()
        addTime.place_forget()
        hourTime.place_forget()
        minTime.place_forget()
        secTime.place_forget()
        submit.place_forget()
        canvas.itemconfigure(clock, fill="Black")
        canvas.itemconfigure(hello, fill="Black")
        canvas.itemconfigure(focus, fill="Black")
        check_marks.place_forget()



        canvas.itemconfigure(real_time, state="hidden")
        canvas.itemconfig(title_pomo, text="", fill="black")
        home_alarm_btn.place_forget()

    Alarm_button.place_forget()
    Pomodoro_button.place_forget()
    home_alarm_btn = Button(text="Home Page", highlightthickness=0, width=20,
                            height=1, bd='4', font=("Arial", 10, "bold"), bg="#b0dab9", command=home_alarm)
    home_alarm_btn.place(x=220, y=650)

    canvas.itemconfig(image_id, image=alarm_img)

    canvas.itemconfigure(clock, fill="White")
    canvas.itemconfigure(real_time, fill="White")
    canvas.itemconfigure(hello, fill="White")
    canvas.itemconfigure(focus, fill="White")

    canvas.itemconfig(title_pomo, text="Alarm", fill="black")

    def alarm(set_alarm_timer):

        while True:
            time.sleep(1)
            clear()
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            date = current_time.strftime("%d/%m/%Y")
            print("The Set Date is:", date)
            print(now)
            if now == set_alarm_timer:
                raise_above_all()
                print("Time to Wake up")
                time_format.config(text="Time's Up!")
                time_format.place(x=250,y=200)
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

                break

    def actual_time():
        set_alarm_timer = f"{hour.get()}:{minutes.get()}:{sec.get()}"
        alarm(set_alarm_timer)

    # clock = Tk()
    window.title("Alarm Clock")

    # clock.iconbitmap(r"dataflair-logo.ico")
    # clock.geometry("400x200")

    time_format = Label(window, text="Enter time in 24 hour format", fg="black", bg="#f4cca4", font="Arial,30")

    time_format.place(x=170, y=200)

    addTime = Label(window, text="Hour       Min       Sec", font=70, fg="white", bg="#2c122f")
    addTime.place(x=200, y=450)
    # The Variables we require to set the alarm(initialization):
    hour = StringVar()
    minutes = StringVar()
    sec = StringVar()

    # Time required to set the alarm clock:
    hourTime = Entry(window, textvariable=hour, fg="white", bg="#2c122f", width=15)
    hourTime.place(x=200, y=500)
    minTime = Entry(window, textvariable=minutes, fg="white", bg="#2c122f", width=15)
    minTime.place(x=270, y=500)
    secTime = Entry(window, textvariable=sec, fg="white", bg="#2c122f", width=15)
    secTime.place(x=320, y=500)

    # To take the time input by user:
    submit = Button(window, text='Set Alarm', width=20,
                    height=1, bd='4', font=("Arial", 10, "bold"), bg="#b7657b", command=actual_time)
    submit.place(x=220, y=550)


# Alarm clock button
Alarm_button = Button(window, text='Alarm Clock', width=33,
                      height=2, bd='4', font=FONT, bg="#fbaccc", command=On_click_alarm)

Alarm_button.place(x=303, y=75)

window.mainloop()
