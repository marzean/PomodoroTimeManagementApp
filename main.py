from tkinter import *
import math

"""the variables and font color font name"""
TITLE_COLOR = "#FF7B54"
BG_COLOR = "#FFB26B"
FONT_NAME = "Fira Sans"
ACTIVITY_TIME = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 20
stages = 0
initial_time = 0


"""function to reset timer"""


def reset():
    window.after_cancel(initial_time)
    canvas.itemconfig(clock_text, text="00:00")
    main_label.config(text="Pomodoro Timer")
    tick.config(text="")
    global stages
    stages = 0


"""function for starting the clock"""


def begin_clock():
    global stages
    stages += 1
    if stages % 8 == 0:
        timer_countdown(LONG_BREAK_TIME * 60)
        main_label.config(text="Power Nap!!!", bg=BG_COLOR, fg="#A75D5D")
    elif stages % 2 == 0:
        main_label.config(text="Coffee break!", bg=BG_COLOR, fg="#A75D5D")
        timer_countdown(SHORT_BREAK_TIME * 60)
    else:
        timer_countdown(ACTIVITY_TIME * 60)
        main_label.config(text="Time for activity", bg=BG_COLOR, fg=TITLE_COLOR)


"""Function to track Timer countdown"""


def timer_countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(clock_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global initial_time
        initial_time = window.after(1000, timer_countdown, count - 1)
    else:
        begin_clock()
        tick_mark = ""
        a_full_activity = math.floor(stages/2)
        for t in range(a_full_activity):
            tick_mark += "✔️"
        tick.config(text=tick_mark)


"""User interface for the users"""
window = Tk()
window.title("Pomodoro a time management app")
window.config(padx=100, pady=50, bg=BG_COLOR)

"""Canvas for creating the background image and the clock"""
canvas = Canvas(width=210, height=234, bg=BG_COLOR, highlightthickness=0)
main_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=main_image)
clock_text = canvas.create_text(100, 130, text="00:00", fill="Black", font=("Orbitron", "25", "bold"))
canvas.grid(column=2, row=2)

"""the app title"""
main_label = Label(text="Pomodoro Timer", bg=BG_COLOR, font=(FONT_NAME, "35", "bold"), fg=TITLE_COLOR, highlightthickness=0)
main_label.grid(column=2, row=0)

"""buttons"""
start_button = Button(text="Start", bg="coral", highlightthickness=0, command=begin_clock)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", bg="coral", highlightthickness=0, command=reset)
reset_button.grid(column=3, row=3)

"""Tick marks to track the timer"""
tick = Label(bg=BG_COLOR, font=("", "15", "bold"), fg="#3CCF4E")
tick.grid(column=2, row=3)
window.mainloop()
