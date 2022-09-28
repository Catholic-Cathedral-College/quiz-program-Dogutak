import tkinter as tk
import prevques_analyser
from PIL import ImageTk, Image

questionnumber = 0
agentscore = 0

#These are the scores for all the general questions
choice1 = 1
choice2 = 2
choice3 = 3
choice4 = 4

#This function is the function that begins the quiz.
#This is the main window - you can see the tk window tab at the top
menuwindow = tk.Tk()
menuwindow.geometry("835x635")

#TEMPLATE CODE
#<------------------------>

#<------------------------>

#These are canvases, these are where the information of each page will sit depending on which one.
#Under this is all the image screen canvases
#<---------->
#This is the menu screen canvas
menuplatform = tk.Canvas(menuwindow, width=835, height=635)
#This is the info page canvas
infopageplatform = tk.Canvas(menuwindow, width=835, height=635)
#<---------->

#Under this is all the button canvases
#<---------->
#This is the BEGIN button canvas
beginbuttonplatform = tk.Canvas(menuwindow, width=50, height=50)

#<---------->


#ALL THE FUNCTIONS ARE UNDER HERE
#<------------------------>
def analyser():
    global agentscore
    print("agent score is", agentscore)
    nextques()


def nextques():
    global questionnumber
    questionnumber = questionnumber + 1
    questioncheck()


def prevques():
    global questionnumber
    global agentscore
    questionnumber = questionnumber - 1
    questioncheck()
    if questionnumber > 1:
      agentscore = agentscore - prevques_analyser.quizscore
    print("agent score is", agentscore)

    

def questioncheck():
    global agentscore
    firstquestion = 0
    for number in range(questionnumber):
        if questionnumber == 1:
            agentscore = firstquestion
            firstques()
            hideq1()
        if questionnumber == 2:
            secondques()
        if questionnumber == 3:
            thirdques()
        if questionnumber == 4:
            fourthques()
        if questionnumber == 5:
            fifthques()
        if questionnumber == 6:
            sixthques()
        if questionnumber == 7:
            seventhques()
        if questionnumber == 8:
            eighthques()
        if questionnumber == 9:
            ninthques()
        if questionnumber == 10:
            tenthques()
        if questionnumber == 11:
            eleventhques()

def disclaimer():
    begin_button.destroy()
    menuplatform.create_image(415, 315, image=infopage_img)
    yesbtn.place(x=217, y=350)
    nobtn.place(x=487, y=350)


#QUESTION 1 FUNCTIONS
#<------------------------>
def firstques():
    yesbtn.destroy()
    nobtn.destroy()
    #THIS HIDES ALL THE OTHER QUESTION BUTTONS
    hideq1()
    menuplatform.create_image(415, 315, image=firstques_img)
    fngbtn.place(x=27, y=175)
    snsbtn.place(x=487, y=175)
    qnsbtn.place(x=27, y=425)
    sncbtn.place(x=487, y=425)


# RESPONSES
def choice1():
    choicescore = 0
    choicescore = choicescore + 1
    global agentscore
    agentscore = agentscore + choicescore
    analyser()
    prevques_analyser.prevchoice1()

def choice2():
    global agentscore
    choicescore = 0
    choicescore = choicescore + 2
    agentscore = agentscore + choicescore
    analyser()
    prevques_analyser.prevchoice2()

def choice3():
    global agentscore
    choicescore = 0
    choicescore = choicescore + 3
    agentscore = agentscore + choicescore
    analyser()
    prevques_analyser.prevchoice3()

def choice4():
    global agentscore
    choicescore = 0
    choicescore = choicescore + 4
    agentscore = agentscore + choicescore
    analyser()
    prevques_analyser.prevchoice4()


#<------------------------>
#QUESTION 2 FUNCTIONS

  
#<------------------------>
def secondques():
  #THIS HIDES ALL THE OTHER BUTTONS
    hideq2()
    menuplatform.create_image(415, 315, image=secondques_img)
    newbtn.place(x=5, y=175)
    okbtn.place(x=457, y=175)
    decentbtn.place(x=5, y=425)
    skilledbtn.place(x=457, y=425)
    backbtn.place(x=320, y=560)


#<------------------------>
#QUESTION 3 FUNCTIONS
#<------------------------>
def thirdques():
    hideq3()
    menuplatform.create_image(415, 315, image=thirdques_img)
    vandalbtn.place(x=30, y=275)
    phantombtn.place(x=520, y=275)


#<------------------------>
#QUESTION 4 FUNCTIONS
#<------------------------>
def fourthques():
    hideq4()
    menuplatform.create_image(415, 315, image=fourthques_img)
    attackbtn.place(x=100, y=175)
    defendbtn.place(x=100, y=375)


#<------------------------>
#QUESTION 5 FUNCTIONS
#<------------------------>
def fifthques():
    menuplatform.create_image(415, 315, image=fifthques_img)
    hideq5()
    marshopbtn.place(x=5, y=175)
    stingspecbtn.place(x=510, y=175)
    aresodinbtn.place(x=5, y=425)
    buckjudbtn.place(x=510, y=425)
    backbtn.place(x=320, y=560)

#<------------------------>
#QUESTION 6 FUNCTIONS
#<------------------------>
def sixthques():
  menuplatform.create_image(415, 315, image=sixthques_img)
  hideq6()
  hiderbtn.place(x=5, y=125)
  holderbtn.place(x=450, y=125)
  stealthbtn.place(x=5, y=375)
  plannerbtn.place(x=450, y=375)
  backbtn.place(x=320, y=325)

  
#<------------------------>
#QUESTION 7 FUNCTIONS
#<------------------------>
def seventhques():
  menuplatform.create_image(415, 315, image=seventhques_img)
  hideq7()
  abilitybothbtn.place(x=100, y=175)
  gunplaybothbtn.place(x=100, y=375)
  backbtn.place(x=320, y=560)

  
#<------------------------>
#QUESTION 8 FUNCTIONS
#<------------------------>
def eighthques():
  menuplatform.create_image(415, 315, image=eighthques_img)
  hideq8()
  intelbtn.place(x=75, y=175)
  firepowerbtn.place(x=425, y=175)
  controlbtn.place(x=250, y=375)

  
#<------------------------>
#QUESTION 9 FUNCTIONS
#<------------------------>
def ninthques():
  menuplatform.create_image(415, 315, image=ninthques_img)
  hideq9()
  srangebtn.place(x=25, y=175)
  mrangebtn.place(x=435, y=175)
  lrangebtn.place(x=225, y=375)

  
#<------------------------>
#QUESTION 10 FUNCTIONS
#<------------------------>
def tenthques():
  menuplatform.create_image(415, 315, image=tenthques_img)
  hideq10()
  overwatchbtn.place(x=20, y=375)
  csgobtn.place(x=465, y=150)

  
#<------------------------>  
#QUESTION 11 FUNCTIONS
#<------------------------>
def eleventhques():
  hideq11()
  menuplatform.create_image(415, 315, image=eleventhques_img)
  strategiesbtn.place(x=250, y=175)
  adaptingbtn.place(x=250, y=375)

  
#<------------------------> 



  
def closequiz():
    menuwindow.destroy()


#<------------------------>

#FIRST QUESTION CODE
#<------------------------>
#BUTTON CODE
#ANSWER 1 "Fast and Aggressive"
fngimg = ImageTk.PhotoImage(Image.open("buttonimages/question1/FNG.png"))
fngbtn = tk.Button(image=fngimg, command=choice1)

#ANSWER 2 "Slow and Steady"
snsimg = ImageTk.PhotoImage(Image.open("buttonimages/question1/SNS.png"))
snsbtn = tk.Button(image=snsimg, command=choice2)

#ANSWER 3 "Quiet and Stealthy"
qnsimg = ImageTk.PhotoImage(Image.open("buttonimages/question1/QNS.png"))
qnsbtn = tk.Button(image=qnsimg, command=choice3)

#ANSWER 4 "Safe and Cautious"
sncimg = ImageTk.PhotoImage(Image.open("buttonimages/question1/SNC.png"))
sncbtn = tk.Button(image=sncimg, command=choice4)
#IMAGE CODE
firstques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question1.png")  #Directory file finder

#<------------------------>
#SECOND QUESTION CODE
#<------------------------>
#BUTTON CODE
#ANSWER 1 "New"
newimg = ImageTk.PhotoImage(Image.open("buttonimages/question2/new.png"))
newbtn = tk.Button(image=newimg, command=choice1)

#ANSWER 2 "Okay"
okimg = ImageTk.PhotoImage(Image.open("buttonimages/question2/ok.png"))
okbtn = tk.Button(image=okimg, command=choice2)

#ANSWER 3 "Decent"
decentimg = ImageTk.PhotoImage(Image.open("buttonimages/question2/decent.png"))
decentbtn = tk.Button(image=decentimg, command=choice3)

#ANSWER 4 "Skilled"
skilledimg = ImageTk.PhotoImage(
    Image.open("buttonimages/question2/skilled.png"))
skilledbtn = tk.Button(image=skilledimg, command=choice4)

secondques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question2.png")

#<------------------------>
#THIRD QUESTION CODE
#<------------------------>
#BUTTON CODE
#ANSWER 1 "Vandal"
vandalimg = ImageTk.PhotoImage(Image.open("buttonimages/question3/vandal.png"))
vandalbtn = tk.Button(image=vandalimg, command=choice1)
#ANSWER 1 "Phantom"
phantomimg = ImageTk.PhotoImage(Image.open("buttonimages/question3/phantom.png"))
phantombtn = tk.Button(image=phantomimg, command=choice4)

thirdques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question3.png")

#<------------------------>
#FOURTH QUESTION CODE
#<------------------------>
fourthques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question4.png")
#BUTTON CODE
#ANSWER 1 "ATTACKING"
attackimg = ImageTk.PhotoImage(Image.open("buttonimages/question4/attacking.png"))
attackbtn = tk.Button(image=attackimg, command=choice2)
#ANSWER 2 "DEFENDING"
defendimg = ImageTk.PhotoImage(Image.open("buttonimages/question4/defending.png"))
defendbtn = tk.Button(image=defendimg, command=choice3)
#<------------------------>
#FIFTH QUESTION CODE
#<------------------------>
fifthques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question5.png")
#BUTTON CODE
#ANSWER 1 "Marshal/Operator"
marshopimg = ImageTk.PhotoImage(Image.open("buttonimages/question5/marshop.png"))
marshopbtn = tk.Button(image=marshopimg, command=choice1)

#ANSWER 2 "Stinger/Spectre"
stingspecimg = ImageTk.PhotoImage(Image.open("buttonimages/question5/stingspec.png"))
stingspecbtn = tk.Button(image=stingspecimg, command=choice2)

#ANSWER 3 "Ares/Odin"
aresodinimg = ImageTk.PhotoImage(Image.open("buttonimages/question5/aresodin.png"))
aresodinbtn = tk.Button(image=aresodinimg, command=choice3)

#ANSWER 4 "Bucky/Judge"
buckjudimg = ImageTk.PhotoImage(Image.open("buttonimages/question5/buckjud.png"))
buckjudbtn = tk.Button(image=buckjudimg, command=choice4)
#<------------------------>
#SIXTH QUESTION CODE
#<------------------------>
sixthques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question6.png")
#BUTTON CODE
#ANSWER 1 "Hiding Back"
hiderimg = ImageTk.PhotoImage(Image.open("buttonimages/question6/scen1.png"))
hiderbtn = tk.Button(image= hiderimg, command=choice1)
#ANSWER 2 "Holding an Angle"
holderimg = ImageTk.PhotoImage(Image.open("buttonimages/question6/scen2.png"))
holderbtn = tk.Button(image=holderimg, command=choice2)
#ANSWER 3 "Stealth Way"
stealthimg = ImageTk.PhotoImage(Image.open("buttonimages/question6/scen3.png"))
stealthbtn = tk.Button(image=stealthimg, command=choice3)
#ANSWER 4 "Defence Planner"
plannerimg = ImageTk.PhotoImage(Image.open("buttonimages/question6/scen4.png"))
plannerbtn = tk.Button(image=plannerimg, command=choice4)
#<------------------------>

#SEVENTH QUESTION CODE
#<------------------------>
seventhques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question7.png")
#BUTTON CODE
#ANSWER 1 "Hiding Back"
abilitybothimg = ImageTk.PhotoImage(Image.open("buttonimages/question7/abilityboth.png"))
abilitybothbtn = tk.Button(image= abilitybothimg, command=choice1)
#ANSWER 2 "Holding an Angle"
gunplaybothimg = ImageTk.PhotoImage(Image.open("buttonimages/question7/gunplayboth.png"))
gunplaybothbtn = tk.Button(image= gunplaybothimg, command=choice2)

#<------------------------>

#EIGHTH QUESTION CODE
#<------------------------>
eighthques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question8.png")
#ANSWER 1 "Intel"
intelimg = ImageTk.PhotoImage(Image.open("buttonimages/question8/intel.png"))
intelbtn = tk.Button(image= intelimg, command=choice1)
#ANSWER 2 "Firepower"
firepowerimg = ImageTk.PhotoImage(Image.open("buttonimages/question8/firepower.png"))
firepowerbtn = tk.Button(image= firepowerimg, command=choice2)
#ANSWER 3 "Control"
controlimg = ImageTk.PhotoImage(Image.open("buttonimages/question8/control.png"))
controlbtn = tk.Button(image= controlimg, command=choice3)
#<------------------------>

#NINTH QUESTION CODE
#<------------------------>
ninthques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question9.png")
#ANSWER 1 "Short Range"
srangeimg = ImageTk.PhotoImage(Image.open("buttonimages/question9/srange.png"))
srangebtn = tk.Button(image= srangeimg, command=choice1)
#ANSWER 2 "Mid Range"
mrangeimg = ImageTk.PhotoImage(Image.open("buttonimages/question9/mrange.png"))
mrangebtn = tk.Button(image= mrangeimg, command=choice2)
#ANSWER 3 "Long Range"
lrangeimg = ImageTk.PhotoImage(Image.open("buttonimages/question9/lrange.png"))
lrangebtn = tk.Button(image= lrangeimg, command=choice2)

#<------------------------>
#TENTH QUESTION CODE
#<------------------------>
tenthques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question10.png")
#ANSWER 1 "Overwatch"
overwatchimg = ImageTk.PhotoImage(Image.open("buttonimages/question10/overwatch.png"))
overwatchbtn = tk.Button(image= overwatchimg, command=choice1)
#ANSWER 2 "CS:GO"
csgoimg = ImageTk.PhotoImage(Image.open("buttonimages/question10/csgo.png"))
csgobtn = tk.Button(image= csgoimg, command=choice2)
#<---------------------->


#ELEVENTH QUESTION CODE
#<------------------------>
eleventhques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question11.png")
#ANSWER 1 "Strategies"
strategiesimg = ImageTk.PhotoImage(Image.open("buttonimages/question11/strategies.png"))
strategiesbtn = tk.Button(image= strategiesimg, command=choice1)
#ANSWER 2 "Adapting"
adaptingimg = ImageTk.PhotoImage(Image.open("buttonimages/question11/adapting.png"))
adaptingbtn = tk.Button(image= adaptingimg, command=choice4)
#<------------------------>



#MENU SCREEN IMAGE CODE
#<--------------------->
valorant_img = ImageTk.PhotoImage(
    file="imagescreens/val.png")  #Directory file finder
#This is to actually show the canvas
menuplatform.pack()
#This is the code to call the image
menu = ImageTk.PhotoImage(Image.open("imagescreens/val.png"))
menuimage = tk.Label(menuwindow, image=menu)
#This is to actually show the image
menuimage.pack()

menuplatform.create_image(415, 315, image=valorant_img)
#<--------------------->

#BEGIN BUTTON CODE
#<------------------------>
#This finds the file for the image of the "BEGIN" button.
begin_image = ImageTk.PhotoImage(
    Image.open(
        "buttonimages/menuscreen/beginbutton.png"))  #^Directory file finder
#This creates the area for the BEGIN button to actually work.
begin_button = tk.Button(text="Start the Test",
                         image=begin_image,
                         command=disclaimer)
begin_button.configure(width=227)
begin_button_window = beginbuttonplatform.create_window(30, 40)
#This places the "BEGIN" button where I want it to be - note the coordinates.
infopage_img = ImageTk.PhotoImage(
    file="imagescreens/info page.png")  #Directory file finder

begin_button.place(x=287, y=350)
#<------------------------>

#YES AND NO BUTTON CODE
#<-------------------->
yesimg = ImageTk.PhotoImage(Image.open("buttonimages/disclaimer/yes.png"))
yesbtn = tk.Button(text="Yes", image=yesimg, command=nextques)
yesbtn.configure(width=110)

noimg = ImageTk.PhotoImage(Image.open("buttonimages/disclaimer/no.png"))
nobtn = tk.Button(text="No", image=noimg, command=closequiz)
nobtn.configure(width=110)
#<-------------------->

#BACK BUTTON CODE
#<-------------------->
backbtnimg = ImageTk.PhotoImage(
    Image.open("buttonimages/overall/backbutton.png"))
backbtn = tk.Button(image=backbtnimg, command=prevques)
#<-------------------->

#ALL THESE FUNCTIONS HIDE ALL THE BUTTONS DEPENDING ON WHICH QUESTION
def hideq1():
    newbtn.place(x=1115, y=175)
    okbtn.place(x=11457, y=175)
    decentbtn.place(x=1115, y=425)
    skilledbtn.place(x=11457, y=425)
    backbtn.place(x=11320, y=560)
def hideq2():
    fngbtn.place(x=11127, y=175)
    snsbtn.place(x=11487, y=175)
    qnsbtn.place(x=11127, y=425)
    sncbtn.place(x=11487, y=425)
    vandalbtn.place(x=1111,y=1111)
    phantombtn.place(x=1111,y=1111)
def hideq3():
    newbtn.place(x=1115, y=175)
    okbtn.place(x=11457, y=175)
    decentbtn.place(x=1115, y=425)
    skilledbtn.place(x=11457, y=425)
    attackbtn.place(x=11100, y=175)
    defendbtn.place(x=11100, y=375)
def hideq4():
    vandalbtn.place(x=1111,y=1111)
    phantombtn.place(x=1111,y=1111)
    marshopbtn.place(x=1115, y=175)
    stingspecbtn.place(x=11510, y=175)
    aresodinbtn.place(x=1115, y=425)
    buckjudbtn.place(x=11510, y=425)
def hideq5():
    attackbtn.place(x=11100, y=175)
    defendbtn.place(x=11100, y=375)
    hiderbtn.place(x=1115, y=125)
    holderbtn.place(x=111450, y=125)
    stealthbtn.place(x=1115, y=375)
    plannerbtn.place(x=11450, y=375)
def hideq6():
    marshopbtn.place(x=1115, y=175)
    stingspecbtn.place(x=11510, y=175)
    aresodinbtn.place(x=1115, y=425)
    buckjudbtn.place(x=11510, y=425)
    hiderbtn.place(x=1115, y=125)
    holderbtn.place(x=111450, y=125)
    stealthbtn.place(x=1115, y=375)
    plannerbtn.place(x=11450, y=375)
    abilitybothbtn.place(x=11100, y=175)
    gunplaybothbtn.place(x=11100, y=375)
def hideq7():
    hiderbtn.place(x=1115, y=125)
    holderbtn.place(x=111450, y=125)
    stealthbtn.place(x=1115, y=375)
    plannerbtn.place(x=11450, y=375)
    abilitybothbtn.place(x=11100, y=175)
    gunplaybothbtn.place(x=11100, y=375)
    intelbtn.place(x=111175, y=175)
    firepowerbtn.place(x=111425, y=175)
    controlbtn.place(x=111250, y=375)
def hideq8():
    abilitybothbtn.place(x=11100, y=175)
    gunplaybothbtn.place(x=11100, y=375)
    srangebtn.place(x=1115, y=175)
    mrangebtn.place(x=111510, y=175)
    lrangebtn.place(x=11510, y=175)
    intelbtn.place(x=11175, y=175)
    firepowerbtn.place(x=11425, y=175)
    controlbtn.place(x=111250, y=375)
def hideq9():  
    intelbtn.place(x=1115, y=175)
    firepowerbtn.place(x=111510, y=175)
    controlbtn.place(x=111510, y=425)
    overwatchbtn.place(x=111510, y=175) 
    csgobtn.place(x=111510, y=425)
def hideq10():
    srangebtn.place(x=1115, y=175)
    mrangebtn.place(x=111510, y=175)
    lrangebtn.place(x=11510, y=175)
    overwatchbtn.place(x=111510, y=175) 
    csgobtn.place(x=111510, y=425)
    strategiesbtn.place(x=11100, y=175)
    adaptingbtn.place(x=11100, y=375)
def hideq11():
    overwatchbtn.place(x=11120, y=375)
    csgobtn.place(x=111465, y=150)
print("The Quiz has Begun, a GUI should show up!")
print(questionnumber)
