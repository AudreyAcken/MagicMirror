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
weather_text.config(text=weather_re1)#weather_text.pack()

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
        
#STEM FAIR STUFF

StemTitle = Label(w, font=('sans-serif, 50'), fg='white', bg="black", anchor=W, justify=LEFT, text="STEM Fair Roster")
StemTitle.grid(row=4, column=0, sticky='w', ipadx=5, ipady=15)

StemFirstTitle = Label(w, font=('sans-serif', 28), width=44, fg='white', bg="black", anchor=W, justify=LEFT, text="Exhibits starting at 1:30 on the Third Floor:")
StemFirstTitle.grid(row=5, column=0, sticky='w', ipadx=5, ipady=5)

StemFirstOne = Label(w, text=" - Sequenced Genomes to Cell Model by Peter Karp (PhD, SRI International)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemFirstOne.grid(row=6, column=0, sticky='w', ipadx=5, ipady=5)

StemSecondOne = Label(w, text=" - Computer Animation by Gabor Nagy (Equinox 3D)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemSecondOne.grid(row=7, column=0, sticky='w', ipadx=5, ipady=5)

StemThirdOne = Label(w, text=" - Marine Microbiology by Chris Francis (PhD, Stanford)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemThirdOne.grid(row=8, column=0, sticky='w', ipadx=5, ipady=5)

StemFourthOne = Label(w, text=" - Science Rap Academy by Tom Mc Fadden (Nueva)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemFourthOne.grid(row=9, column=0, sticky='w', ipadx=5, ipady=5)

#space

stemSpaceOne = Label(w, text=" ", fg='black', bg='black')
stemSpaceOne.grid(row=10, column=0, stick='w', ipadx=5, ipady=5)

#2:30

StemSecondTitle = Label(w, font=('sans-serif', 28), width=44, fg='white', bg="black", anchor=W, justify=LEFT, text="Exhibits starting at 2:30 on the Third Floor:")
StemSecondTitle.grid(row=11, column=0, sticky='w', ipadx=5, ipady=5)

StemFirstOne = Label(w, text=" - Structure Guided Drug Design by Zach Newby (PhD, Gilead)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemFirstOne.grid(row=12, column=0, sticky='w', ipadx=5, ipady=5)

StemSecondOne = Label(w, text=" - Cryptocurrency and Blockchain by Thor Muller (Off Grid Electric)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemSecondOne.grid(row=13, column=0, sticky='w', ipadx=5, ipady=5)

StemThirdOne = Label(w, text=" - Computer Animation by Gabor Nagy (Equinox 3D)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemThirdOne.grid(row=14, column=0, sticky='w', ipadx=5, ipady=5)

StemFourthOne = Label(w, text=" - Turning HIV into Genetic Medicine by Trip Sweeney (MD, Nueva)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemFourthOne.grid(row=15, column=0, sticky='w', ipadx=5, ipady=5)


#space

stemSpaceTwo = Label(w, text=" ", fg='black', bg='black')
stemSpaceTwo.grid(row=16, column=0, stick='w', ipadx=5, ipady=5)

#Speakers

StemSpeakerTitle = Label(w, font=('sans-serif', 28), width=44, fg='white', bg="black", anchor=W, justify=LEFT, text="STEMcast Lectures:")
StemSpeakerTitle.grid(row=17, column=0, sticky='w', ipadx=5, ipady=5)

StemSpeakerOne = Label(w, text="12:10     Pandora's Music Genome Project- A Marriage of Math and Music", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemSpeakerOne.grid(row=18, column=0, sticky='w', ipadx=5, ipady=5)

StemSpeakerNameOne = Label(w, text="                  Tim Westergren, Co-founder and CEO of Pandora", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))
StemSpeakerNameOne.grid(row=19, column=0, sticky='w')

StemSpeakerTwo = Label(w, text="12:30     Study and structure-activity relationship of salicylate analogs as antimicrobials", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemSpeakerTwo.grid(row=20, column=0, sticky='w', ipadx=5, ipady=5)

StemSpeakerNameTwo = Label(w, text="                  Yoni L; Will C; Chris C; Daniel P; Marc Y; Zubin A; Francine F; Nueva Drug Design Class", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))
StemSpeakerNameTwo.grid(row=21, column=0, sticky='w')

StemSpeakerThree = Label(w, text="12:50     Drug Development- Making a Safer Treatment for People with HIV", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemSpeakerThree.grid(row=22, column=0, sticky='w', ipadx=5, ipady=5)

StemSpeakerNameThree = Label(w, text="                  Marshal Fordyce, MD, CEO, CDF Therapeutics", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))
StemSpeakerNameThree.grid(row=23, column=0, sticky='w')

StemSpeakerFour = Label(w, text="01:10     23 and Me- Research Powered by the People", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemSpeakerFour.grid(row=24, column=0, sticky='w', ipadx=5, ipady=5)

StemSpeakerNameFour = Label(w, text="                  Joyce Tung, PhD, VP of Research, 23andMe", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))
StemSpeakerNameFour.grid(row=25, column=0, sticky='w')

StemSpeakerFive = Label(w, text="01:30     Planets in Our Solar System and Beyond", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemSpeakerFive.grid(row=25, column=0, sticky='w', ipadx=5, ipady=5)

StemSpeakerNameFive = Label(w, text="                  Vanessa Bailey, PhD, Post doc, Stanford Gemini Planet Imager", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))
StemSpeakerNameFive.grid(row=26, column=0, sticky='w')

StemSpeakerSix = Label(w, text="01:50     MyCareerStory.org- an approach to scale and normalize diversity in the workforce", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemSpeakerSix.grid(row=27, column=0, sticky='w', ipadx=5, ipady=5)

StemSpeakerNameSix = Label(w, text="                  Rowan Chapman, PhD, Head of Johnson & Johnson Innovation", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))
StemSpeakerNameSix.grid(row=28, column=0, sticky='w')

StemSpeakerSeven = Label(w, text="02:45     \"Science With Tom\" Raps about Your Favorite Scientific Topics", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemSpeakerSeven.grid(row=29, column=0, sticky='w', ipadx=5, ipady=5)

StemSpeakerNameSeven = Label(w, text="                  Tom Mc Fadden, Nueva Faculty", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))
StemSpeakerNameSeven.grid(row=30, column=0, sticky='w')

#space

stemSpaceThree = Label(w, text=" ", fg='black', bg='black')
stemSpaceThree.grid(row=31, column=0, stick='w', ipadx=5, ipady=5)

#ms exhibits

StemMSTitle = Label(w, font=('sans-serif', 28), width=44, fg='white', bg="black", anchor=W, justify=LEFT, text="MS Exhibits:")
StemMSTitle.grid(row=32, column=0, sticky='w', ipadx=5, ipady=5)

StemMSOne = Label(w, text=" - ARC Furnace by Clayton M., John C., and Nolan S.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemMSOne.grid(row=33, column=0, sticky='w', ipadx=5, ipady=5)

StemMSTwo = Label(w, text=" - Aspartame by Anya P.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemMSTwo.grid(row=34, column=0, sticky='w', ipadx=5, ipady=5)

StemMSThree = Label(w, text=" - Modeling Global Warming with Python by Enerson P.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemMSThree.grid(row=35, column=0, sticky='w', ipadx=5, ipady=5)

StemMSFour = Label(w, text=" - Molecular Gastronomy by Emy Y., Anouschka B., Molly C., and Alyssa H.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemMSFour.grid(row=36, column=0, sticky='w', ipadx=5, ipady=5)

StemMSFive = Label(w, text=" - Markers and Chromatography by Riyani S.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemMSFive.grid(row=37, column=0, sticky='w', ipadx=5, ipady=5)

StemMSSix = Label(w, text=" - Bullywatch by Yash N.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemMSSix.grid(row=38, column=0, sticky='w', ipadx=5, ipady=5)

StemMSSeven = Label(w, text=" - Tornato & Vortex Simulator by Giulia K.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemMSSeven.grid(row=39, column=0, sticky='w', ipadx=5, ipady=5)

StemMSEight = Label(w, text=" - Smart Mirror by Audrey A.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemMSEight.grid(row=40, column=0, sticky='w', ipadx=5, ipady=5)

StemMSTwo = Label(w, text=" - Indoor Sports Machine by Alex K. and Isabgella Y.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)
StemMSTwo.grid(row=41, column=0, sticky='w', ipadx=5, ipady=5)
master.bind('1', toggleTime)
master.bind('2', toggleWeather)

mainloop()
