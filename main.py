import tkinter as tk
from PIL import ImageTk, Image

questionnumber = 0
agentscore = 0

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
  print(agentscore)
  nextques()

def nextques():
    global questionnumber
    questionnumber = questionnumber + 1
    questioncheck()


def questioncheck():
    for number in range(questionnumber):
        if questionnumber == 1:
            firstques()
        if questionnumber == 2:
            secondques()
        if questionnumber == 3:
            thirdques()
        # if questionnumber == 4:
        # if questionnumber == 5:
        # if questionnumber == 6:
        # if questionnumber == 7:
        # if questionnumber == 8:
        # if questionnumber == 9:


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
    menuplatform.create_image(415, 315, image=firstques_img)
    fngbtn.place(x=27, y=175)
    snsbtn.place(x=487, y=175)
    qnsbtn.place(x=27, y=425)
    sncbtn.place(x=487, y=425)

#QUESTION 1 RESPONSES

def fng():
    global agentscore
    agentscore = agentscore + 1
    analyser()
    
def sns():
    global agentscore
    agentscore = agentscore + 2
    analyser()

def qns():
    global agentscore
    agentscore = agentscore + 3
    analyser()

def snc():
    global agentscore
    agentscore = agentscore + 4
    analyser()
#<------------------------>
#QUESTION 2 FUNCTIONS
#<------------------------>
def secondques():
  fngbtn.destroy()  
  snsbtn.destroy()
  qnsbtn.destroy()
  sncbtn.destroy()
  menuplatform.create_image(415,315, image=secondques_img)
  newbtn.place(x=5, y=175)
  okbtn.place(x=457, y=175)
  decentbtn.place(x=5, y=425)
  skilledbtn.place(x=457, y=425)
#<------------------------>
#QUESTION 3 FUNCTIONS
#<------------------------>
def thirdques():
  newbtn.place(x=1115, y=175)
  okbtn.place(x=111457, y=175)
  decentbtn.place(x=1115, y=425)
  skilledbtn.place(x=111457, y=425)
  menuplatform.create_image(415,315, image=thirdques_img)
#<------------------------>
#QUESTION 4 FUNCTIONS
#<------------------------>
def fourthques():
  menuplatform.create_image(415,315, image=fourthques_img)
#<------------------------>
#QUESTION 5 FUNCTIONS
#<------------------------>
def fifthques():
  menuplatform.create_image(415,315, image=fifthques_img)
#<------------------------>


def closequiz():
    menuwindow.destroy()


#<------------------------>

#FIRST QUESTION CODE
#<------------------------>
#BUTTON CODE
#ANSWER 1 "Fast and Aggressive"
fngimg = ImageTk.PhotoImage(Image.open("buttonimages/question1/FNG.png"))
fngbtn = tk.Button(text="Fast and Aggressive",
                   image=fngimg,
                   command=fng)

#ANSWER 2 "Slow and Steady"
snsimg = ImageTk.PhotoImage(Image.open("buttonimages/question1/SNS.png"))
snsbtn = tk.Button(text="Slow and Steady",
                   image=snsimg,
                   command=sns)

#ANSWER 3 "Quiet and Stealthy"
qnsimg = ImageTk.PhotoImage(Image.open("buttonimages/question1/QNS.png"))
qnsbtn = tk.Button(text="Quiet and Stealthy",
                   image=qnsimg,
                   command=qns)

#ANSWER 4 "Safe and Cautious"
sncimg = ImageTk.PhotoImage(Image.open("buttonimages/question1/SNC.png"))
sncbtn = tk.Button(text="Safe and Cautious",
                   image=sncimg,
                   command=snc)
#IMAGE CODE
firstques_img = ImageTk.PhotoImage(
    file="imagescreens/questionimages/question1.png")  #Directory file finder

#<------------------------>  
#SECOND QUESTION CODE
#<------------------------>
#BUTTON CODE
#ANSWER 1 "New"
newimg = ImageTk.PhotoImage(Image.open("buttonimages/question2/new.png"))
newbtn = tk.Button(
                   image=newimg,
                   command=fng)

#ANSWER 2 "Okay"
okimg = ImageTk.PhotoImage(Image.open("buttonimages/question2/ok.png"))
okbtn = tk.Button(
                   image=okimg,
                   command=fng)

#ANSWER 3 "Decent"
decentimg = ImageTk.PhotoImage(Image.open("buttonimages/question2/decent.png"))
decentbtn = tk.Button(
                   image=decentimg,
                   command=fng)

#ANSWER 4 "Skilled"
skilledimg = ImageTk.PhotoImage(Image.open("buttonimages/question2/skilled.png"))
skilledbtn = tk.Button(
                   image=skilledimg,
                   command=fng)

secondques_img = ImageTk.PhotoImage(file="imagescreens/questionimages/question2.png")

#<------------------------>
#THIRD QUESTION CODE
#<------------------------>
thirdques_img = ImageTk.PhotoImage(file="imagescreens/questionimages/question3.png")

#<------------------------>
#FOURTH QUESTION CODE
#<------------------------>
fourthques_img = ImageTk.PhotoImage(file="imagescreens/questionimages/question4.png")

#<------------------------>
#FIFTH QUESTION CODE
#<------------------------>
fifthques_img = ImageTk.PhotoImage(file="imagescreens/questionimages/question5.png")
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


print("The Quiz has Begun, a GUI should show up!")
print(questionnumber)
