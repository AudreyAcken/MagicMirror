from tkinter import *
import time
import urllib.request
from bs4 import BeautifulSoup
from subprocess import call
from PIL import ImageTk, Image
import threading

master = Tk()

master.attributes("-fullscreen", True)


screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

master.geometry(str(screen_width) + 'x' + str(screen_height))

n = 0

w = master
#w = Canvas(master, width=1824, height=984, bg='black', highlightthickness=0)
#w.pack()

master.configure(background='black')

def functionQuit(event):
    sys.exit(0)

    


master.bind("<space>", functionQuit)
    

time1 = ''

clock = Label(w, font=('sans-serif', 90), fg = 'white', bg='black', width=20, height=1, anchor=NW, justify=LEFT)



#clock.pack()
date1 = ''
clock2 = Label(w, font=('sans-serif', 40), width=44, fg='white', bg='black', anchor=W, justify=LEFT)

      
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


weather_text = Label(w, font=('sans-serif', 40), width=44, fg='white', bg="black", anchor=W, justify=LEFT)

flagClock = False
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
        

flagWeather = False
def toggleWeather(event):
    global flagWeather
    if flagWeather:
        weather_text.grid_forget()
        flagWeather = False
    else:
        
        city = "MountainView"
        state = "CA"
        zip_code = "94040"
        country = "US"

        ten_day = "https://weather.com/weather/tenday/l/" + city + "+" + state + "+" + zip_code + ":4:" + country

        right_now = "https://weather.com/weather/today/l/" + city + "+" + state + "+" + zip_code + ":4:" + country

        page = urllib.request.urlopen(ten_day)

        soup = BeautifulSoup(page, "html.parser")

        main_container = soup.find_all('td', {"class" : "description"})
        if (len(main_container)<1):
            weather_re1 = "Sorry, the weather can not be found at this moment"

        else: 
        
            second_container = main_container[0].find_all('span')
            if (len(second_container)<1):
                weather_re1 = "error 404"
            else:
            
                weather_string = str(second_container[0])
            
                weather_re= re.match(r'(.*>)(.*)(<.*>)', weather_string)
                weather_re1 = weather_re.group(2)
                
        weather_text.config(text=weather_re1)
        
        weather_text.grid(row=2,column=0,sticky='w')
        flagWeather = True
        
#STEM FAIR STUFF

StemTitle = Label(w, font=('sans-serif, 50'), fg='white', bg="black", anchor=W, justify=LEFT, text="STEM Fair Roster")

StemFirstTitle = Label(w, font=('sans-serif', 28), width=44, fg='white', bg="black", anchor=W, justify=LEFT, text="Exhibits starting at 1:30 on the Third Floor:")

StemFirstOne = Label(w, text=" - Sequenced Genomes to Cell Model by Peter Karp (PhD, SRI International)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemSecondOne = Label(w, text=" - Computer Animation by Gabor Nagy (Equinox 3D)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemThirdOne = Label(w, text=" - Marine Microbiology by Chris Francis (PhD, Stanford)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemFourthOne = Label(w, text=" - Science Rap Academy by Tom Mc Fadden (Nueva)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

#space

stemSpaceOne = Label(w, text=" ", fg='black', bg='black')


#2:30

StemSecondTitle = Label(w, font=('sans-serif', 28), width=44, fg='white', bg="black", anchor=W, justify=LEFT, text="Exhibits starting at 2:30 on the Third Floor:")

StemFirstTwo= Label(w, text=" - Structure Guided Drug Design by Zach Newby (PhD, Gilead)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemSecondTwo = Label(w, text=" - Cryptocurrency and Blockchain by Thor Muller (Off Grid Electric)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemThirdTwo = Label(w, text=" - Computer Animation by Gabor Nagy (Equinox 3D)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemFourthTwo = Label(w, text=" - Turning HIV into Genetic Medicine by Trip Sweeney (MD, Nueva)", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)


#space

stemSpaceTwo = Label(w, text=" ", fg='black', bg='black')


#Speakers

StemSpeakerTitle = Label(w, font=('sans-serif', 28), width=44, fg='white', bg="black", anchor=W, justify=LEFT, text="STEMcast Lectures:")

StemSpeakerOne = Label(w, text="12:10     Pandora's Music Genome Project- A Marriage of Math and Music", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemSpeakerNameOne = Label(w, text="                  Tim Westergren, Co-founder and CEO of Pandora", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))

StemSpeakerTwo = Label(w, text="12:30     Study and structure-activity relationship of salicylate analogs as antimicrobials", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemSpeakerNameTwo = Label(w, text="                  Yoni L; Will C; Chris C; Daniel P; Marc Y; Zubin A; Francine F; Nueva Drug Design Class", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))

StemSpeakerThree = Label(w, text="12:50     Drug Development- Making a Safer Treatment for People with HIV", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemSpeakerNameThree = Label(w, text="                  Marshal Fordyce, MD, CEO, CDF Therapeutics", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))

StemSpeakerFour = Label(w, text="01:10     23 and Me- Research Powered by the People", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemSpeakerNameFour = Label(w, text="                  Joyce Tung, PhD, VP of Research, 23andMe", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))

StemSpeakerFive = Label(w, text="01:30     Planets in Our Solar System and Beyond", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemSpeakerNameFive = Label(w, text="                  Vanessa Bailey, PhD, Post doc, Stanford Gemini Planet Imager", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))

StemSpeakerSix = Label(w, text="01:50     MyCareerStory.org- an approach to scale and normalize diversity in the workforce", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemSpeakerNameSix = Label(w, text="                  Rowan Chapman, PhD, Head of Johnson & Johnson Innovation", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))

StemSpeakerSeven = Label(w, text="02:45     \"Science With Tom\" Raps about Your Favorite Scientific Topics", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemSpeakerNameSeven = Label(w, text="                  Tom Mc Fadden, Nueva Faculty", width=100, fg='white', bg='black', anchor=W, justify=LEFT, font=('sans-serif', 15, "italic"))

#space

stemSpaceThree = Label(w, text=" ", fg='black', bg='black')


#ms exhibits

StemMSTitle = Label(w, font=('sans-serif', 28), width=44, fg='white', bg="black", anchor=W, justify=LEFT, text="MS Exhibits:")

StemMSOne = Label(w, text=" - ARC Furnace by Clayton M., John C., and Nolan S.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemMSTwo = Label(w, text=" - Aspartame by Anya P.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemMSThree = Label(w, text=" - Modeling Global Warming with Python by Enerson P.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemMSFour = Label(w, text=" - Molecular Gastronomy by Emy Y., Anouschka B., Molly C., and Alyssa H.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemMSFive = Label(w, text=" - Markers and Chromatography by Riyani S.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemMSSix = Label(w, text=" - Bullywatch by Yash N.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemMSSeven = Label(w, text=" - Tornato & Vortex Simulator by Giulia K.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemMSEight = Label(w, text=" - Smart Mirror by Audrey A.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

StemMSNine = Label(w, text=" - Indoor Sports Machine by Alex K. and Isabgella Y.", font=('sans-serif', 18), width=100, fg='white', bg="black", anchor=W, justify=LEFT)

photo = PhotoImage(file="stemfair.gif")
photo1 = Label(image=photo)


flagSTEM = False
def toggleStem(event):
    global flagSTEM
    if flagSTEM:
        StemTitle.grid_forget()
        
        StemFirstTitle.grid_forget()
        StemFirstOne.grid_forget()
        StemSecondOne.grid_forget()
        StemThirdOne.grid_forget()
        StemFourthOne.grid_forget()
        
        stemSpaceOne.grid_forget()

        StemSecondTitle.grid_forget()
        StemFirstTwo.grid_forget()
        StemSecondTwo.grid_forget()
        StemThirdTwo.grid_forget()
        StemFourthTwo.grid_forget()

        stemSpaceTwo.grid_forget()

        StemSpeakerTitle.grid_forget()
        StemSpeakerOne.grid_forget()
        StemSpeakerNameOne.grid_forget()
        StemSpeakerTwo.grid_forget()
        StemSpeakerNameTwo.grid_forget()
        StemSpeakerThree.grid_forget()
        StemSpeakerNameThree.grid_forget()
        StemSpeakerFour.grid_forget()
        StemSpeakerNameFour.grid_forget()
        StemSpeakerFive.grid_forget()
        StemSpeakerNameFive.grid_forget()
        StemSpeakerSix.grid_forget()
        StemSpeakerNameSix.grid_forget()
        StemSpeakerSeven.grid_forget()
        StemSpeakerNameSeven.grid_forget()

        stemSpaceThree.grid_forget()

        StemMSTitle.grid_forget()
        StemMSOne.grid_forget()
        StemMSTwo.grid_forget()
        StemMSThree.grid_forget()
        StemMSFour.grid_forget()
        StemMSFive.grid_forget()
        StemMSSix.grid_forget()
        StemMSSeven.grid_forget()
        StemMSEight.grid_forget()
        StemMSNine.grid_forget()

        photo1.grid_forget()

        
        flagSTEM = False
    else:
        StemTitle.grid(row=4, column=0, sticky='w', ipadx=5, ipady=15)

        StemFirstTitle.grid(row=5, column=0, sticky='w', ipadx=5, ipady=5)
        StemFirstOne.grid(row=6, column=0, sticky='w', ipadx=5, ipady=5)
        StemSecondOne.grid(row=7, column=0, sticky='w', ipadx=5, ipady=5)
        StemThirdOne.grid(row=8, column=0, sticky='w', ipadx=5, ipady=5)
        StemFourthOne.grid(row=9, column=0, sticky='w', ipadx=5, ipady=5)

        stemSpaceOne.grid(row=10, column=0, stick='w', ipadx=5, ipady=5)

        StemSecondTitle.grid(row=11, column=0, sticky='w', ipadx=5, ipady=5)
        StemFirstTwo.grid(row=12, column=0, sticky='w', ipadx=5, ipady=5)
        StemSecondTwo.grid(row=13, column=0, sticky='w', ipadx=5, ipady=5)
        StemThirdTwo.grid(row=14, column=0, sticky='w', ipadx=5, ipady=5)
        StemFourthTwo.grid(row=15, column=0, sticky='w', ipadx=5, ipady=5)

        stemSpaceTwo.grid(row=16, column=0, stick='w', ipadx=5, ipady=5)

        StemSpeakerTitle.grid(row=17, column=0, sticky='w', ipadx=5, ipady=5)
        StemSpeakerOne.grid(row=18, column=0, sticky='w', ipadx=5, ipady=5)
        StemSpeakerNameOne.grid(row=19, column=0, sticky='w')
        StemSpeakerTwo.grid(row=20, column=0, sticky='w', ipadx=5, ipady=5)
        StemSpeakerNameTwo.grid(row=21, column=0, sticky='w')
        StemSpeakerThree.grid(row=22, column=0, sticky='w', ipadx=5, ipady=5)
        StemSpeakerNameThree.grid(row=23, column=0, sticky='w')
        StemSpeakerFour.grid(row=24, column=0, sticky='w', ipadx=5, ipady=5)
        StemSpeakerNameFour.grid(row=25, column=0, sticky='w')
        StemSpeakerFive.grid(row=25, column=0, sticky='w', ipadx=5, ipady=5)
        StemSpeakerNameFive.grid(row=26, column=0, sticky='w')
        StemSpeakerSix.grid(row=27, column=0, sticky='w', ipadx=5, ipady=5)
        StemSpeakerNameSix.grid(row=28, column=0, sticky='w')
        StemSpeakerSeven.grid(row=29, column=0, sticky='w', ipadx=5, ipady=5)
        StemSpeakerNameSeven.grid(row=30, column=0, sticky='w')

        stemSpaceThree.grid(row=31, column=0, stick='w', ipadx=5, ipady=5)

        StemMSTitle.grid(row=32, column=0, sticky='w', ipadx=5, ipady=5)
        StemMSOne.grid(row=33, column=0, sticky='w', ipadx=5, ipady=5)
        StemMSTwo.grid(row=34, column=0, sticky='w', ipadx=5, ipady=5)
        StemMSThree.grid(row=35, column=0, sticky='w', ipadx=5, ipady=5)
        StemMSFour.grid(row=36, column=0, sticky='w', ipadx=5, ipady=5)
        StemMSFive.grid(row=37, column=0, sticky='w', ipadx=5, ipady=5)
        StemMSSix.grid(row=38, column=0, sticky='w', ipadx=5, ipady=5)
        StemMSSeven.grid(row=39, column=0, sticky='w', ipadx=5, ipady=5)
        StemMSEight.grid(row=40, column=0, sticky='w', ipadx=5, ipady=5)
        StemMSNine.grid(row=41, column=0, sticky='w', ipadx=5, ipady=5)

        photo1.grid(row=42, column=0, sticky='w', ipadx=5, ipady=5)

        flagSTEM = True

#Image taking picture

picturegap = Label(text="                                                         ", fg="black", bg="black")

picture1 = None        
picture = None

pictureFlag = False
def pictureoff():
    global picture, picture1, pictureFlag
    picture1.grid_forget()
    pictureFlag = False

def togglePicture(event):
    global picture, picture1, pictureFlag
    if pictureFlag:
        pictureoff()

    else:
        picturegap.grid(row=43, column=0, ipadx=5, ipady=5)
        takepic = call(["fswebcam", "-p", "YUYV", "-d", "/dev/video0", "--no-banner", "-r", "640x480", "image.jpg"])
        picture = ImageTk.PhotoImage(Image.open("image.jpg"))
        picture1 = Label(image=picture)
        picture1.grid(row=43, column=1, ipadx=5, ipady=5)
        pictureFlag = True
        threading.Timer(5.0, pictureoff).start()


master.bind('1', toggleTime)
master.bind('2', toggleWeather)
master.bind('3', toggleStem)
master.bind('4', togglePicture)
mainloop()
