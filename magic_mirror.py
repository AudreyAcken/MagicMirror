from tkinter import *
import time
import urllib.request
from bs4 import BeautifulSoup 

master = Tk()

master.attributes("-fullscreen", True)


screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

master.geometry(str(screen_width) + 'x' + str(screen_height))

w = master
#w = Canvas(master, width=1824, height=984, bg='black', highlightthickness=0)
#w.pack()

master.configure(background='black')

def functionQuit(event):
    sys.exit(0)
    


master.bind("<space>", functionQuit)
    

time1 = ''

clock = Label(w, font=('sans-serif', 90), fg = 'white', bg='black', width=20, height=1, anchor=NW, justify=LEFT)

clock.grid(row=0, column=0, sticky=W)


#clock.pack()
date1 = ''
clock2 = Label(w, font=('sans-serif', 40), width=44, fg='white', bg='black', anchor=W, justify=LEFT)

clock2.grid(row=1, column=0, sticky=W)               
def tick():
    global time1, clock, date1
    # get the current local time from the PC
    time2 = time.strftime('%I:%M')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
 

    # get the current local time from the PC
    date2 = time.strftime('%A, %B %e, %G')
    # if time string has changed, update it
    if date2 != date1:
        date1 = date2
        clock2.config(text=date2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock2.after(200, tick)

tick()



#Weather

city = "MountainView"
state = "CA"
zip_code = "94040"
country = "US"

ten_day = "https://weather.com/weather/tenday/l/" + city + "+" + state + "+" + zip_code + ":4:" + country

right_now = "https://weather.com/weather/today/l/" + city + "+" + state + "+" + zip_code + ":4:" + country

page = urllib.request.urlopen(ten_day)

soup = BeautifulSoup(page, "html.parser")

main_container = soup.find_all('td', {"class" : "description"})
second_container = main_container[0].find_all('span')
print(second_container)
weather_string = str(second_container[0])
print(weather_string)
print(type(weather_string))
weather_re= re.match(r'(.*>)(.*)(<.*>)', weather_string)
weather_re1 = weather_re.group(2)

weather_text = Label(w, font=('sans-serif', 40), width=44, fg='white', bg="black", anchor=W, justify=LEFT)
weather_text.grid(row=3, column=0, sticky=W)
weather_text.config(text=weather_re1)
#weather_text.pack()

flagClock = True
def toggleTime(event):
    global flagClock
    if flagClock:
        clock.grid_forget()
        clock2.grid_forget()
        flagClock = False
    else:
        clock.grid(row=0,column=0,sticky='w')
        clock2.grid(row=1,column=0,sticky='w')
        flagClock = True
        

flagWeather = True
def toggleWeather(event):
    global flagWeather
    if flagWeather:
        weather_text.grid_forget()
        flagWeather = False
    else:
        weather_text.grid(row=2,column=0,sticky='w')
        flagWeather = True



master.bind('1', toggleTime)
master.bind('2', toggleWeather)

mainloop()
