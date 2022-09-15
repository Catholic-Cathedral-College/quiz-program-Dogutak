import tkinter as tk
import buttonresponses
from PIL import ImageTk, Image

quizindicator = 0
#This function is the function that begins the quiz.
#This is the main window - you can see the tk window tab at the top
menuwindow = tk.Tk()
menuwindow.geometry("835x635")

#Asks the user if they are ready to begin the quiz, this code will stay looping here until they type YES, then it will move on.
# yeslist = ["YES", "YEs", "Yes", "yes", "yeS", "yES"]
# while quizindicator == 0:
#   askbegin = input("If you are ready to begin the quiz, type yes. \n")
#   if askbegin.lower() == "yes":
#     quizindicator = 1

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
#This is the Yesbutton canvas
yesbuttonplatform = tk.Canvas(menuwindow, width=50, height=50)
#This is the No button canvas
nobuttonplatform = tk.Canvas(menuwindow, width=50, height=50)

#<---------->


#ALL THE FUNCTIONS ARE UNDER HERE
#<------------------------>
def disclaimer():
    begin_button.destroy()
    menuplatform.create_image(415, 315, image=infopage_img)
    yesbtn.place(x=217, y=350)
    nobtn.place(x=487, y=350)


def firstques():
    yesbtn.destroy()
    nobtn.destroy()
    menuplatform.create_image(415, 315, image=firstques_img)
    btnsq1()


def btnsq1():
    fngbtn.place(x=217, y=250)
    snsbtn.place(x=487, y=250)
    qnsbtn.place(x=217, y=450)
    sncbtn.place(x=487, y=450)


def closequiz():
    menuwindow.destroy()


#<------------------------>

#FIRST QUESTION CODE
#<------------------------>
firstques_img = ImageTk.PhotoImage(
    file="imagescreens/question1.png")  #Directory file finder

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

#YES AND NO BUTTON CODE
#<-------------------->
yesbtn = tk.Button(text="Yes", command=firstques)
yesbtn.configure(width=10)
nobtn = tk.Button(text="No", command=closequiz)
nobtn.configure(width=10)
#<-------------------->

#BEGIN BUTTON CODE
#<------------------------>
#This finds the file for the image of the "BEGIN" button.
begin_image = ImageTk.PhotoImage(
    Image.open("imagescreens/button.png"))  #^Directory file finder
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


#QUESTION 1 CODE
#<------------------------>

#BUTTON CODE
#<------------------------>

#ANSWER 1 "Fast and Aggressive"
fngbtn = tk.Button(text="Fast and Aggressive", command=buttonresponses.fng)

#ANSWER 2 "Slow and Steady"
snsbtn = tk.Button(text="Slow and Steady", command=buttonresponses.sns)

#ANSWER 3 "Quiet and Stealthy"
qnsbtn = tk.Button(text="Quiet and Stealthy", command=buttonresponses.qns)

#ANSWER 4 "Safe and Cautious"
sncbtn = tk.Button(text="Safe and Cautious", command=buttonresponses.snc)

#<------------------------>

#<------------------------>
print("The Quiz has Begun, a GUI should show up!")
print(quizindicator)