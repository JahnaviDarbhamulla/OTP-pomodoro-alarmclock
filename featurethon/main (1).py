from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)






window.mainloop()

# ticks
# check_mark = Label(text="✔", fg="#9fe6a0", bg="#ffffc7")
# check_mark.grid(column=1, row= 3)

# start_timer
def start_time():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# countdown
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        # check_marks.config(text=marks)


# title_pomodoro = canvas.create_text(300, 200, text="Work", fill="#003973", font=("Arial", 55, "bold"))
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start = Button(window, text='Start', width=30,
               height=2, bd='4', font=("Arial", 10, "bold"), bg="#b0dab9", command=start_time)
start.place(x=25, y=100)
stop = Button(window, text='Reset', width=30,
              height=2, bd='4', font=FONT, bg="#b0dab9")

stop.place(x=320, y=100)





















def alarm():



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
                print("Time to Wake up")
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                break


    def actual_time():
        set_alarm_timer = f"{hour.get()}:{minutes.get()}:{sec.get()}"
        alarm(set_alarm_timer)


    #clock = Tk()
    window.title("Alarm Clock")

    # clock.iconbitmap(r"dataflair-logo.ico")
    #clock.geometry("400x200")
    time_format = Label(window, text="Enter time in 24 hour format!", fg="red", bg="black", font="Arial").place(x=200, y=500)
    addTime = Label(window, text="Hour      Min     Sec", font=90).place(x=220, y=370)
    setYourAlarm = Label(window, text="When to wake you up", fg="blue", relief="solid",
                         font=("Helevetica", 10, "bold")).place(x=50, y=400)

    # The Variables we require to set the alarm(initialization):
    hour = StringVar()
    minutes = StringVar()
    sec = StringVar()

    # Time required to set the alarm clock:
    hourTime = Entry(window, textvariable=hour, bg="pink", width=11).place(x=200, y=400)
    minTime = Entry(window, textvariable=minutes, bg="pink", width=15).place(x=270, y=400)
    secTime = Entry(window, textvariable=sec, bg="pink", width=10).place(x=320, y=400)

    # To take the time input by user:
    submit = Button(window, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=270, y=450)







