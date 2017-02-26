from tkinter import *

master = Tk()

#master.attributes("-fullscreen", True)


screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

print(screen_width, ",", screen_height)

w = Canvas(master, width=1824, height=984)
w.pack()

w.configure(background='black')



mainloop()
