from tkinter import *
import time

master = Tk()

#master.attributes("-fullscreen", True)


screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

master.geometry(str(screen_width) + 'x' + str(screen_height))

w = Canvas(master, width=1824, height=984, bg='black', highlightthickness=0)
w.pack()

master.configure(background='black')

time1 = ''
clock = Label(w, font=('sans-serif', 90), fg = 'white', bg='black', width=20, height=2, anchor=SW, justify=LEFT)
clock.pack()

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%I:%M')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

tick()

# date under the time
date1 = ''
clock2 = Label(w, font=('sans-serif', 40), width=44, fg='white', bg='black', anchor=W, justify=LEFT)
clock2.pack()
def tick1():
    global date1
    # get the current local time from the PC
    date2 = time.strftime('%A, %B %e, %G')
    # if time string has changed, update it
    if date2 != date1:
        date1 = date2
        clock2.config(text=date2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock2.after(200, tick1)
tick1()






mainloop()
