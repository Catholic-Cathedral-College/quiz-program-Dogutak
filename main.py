import tkinter as tk
from PIL import ImageTk, Image

#TEMPLATE CODE
#<------------------------>

#<------------------------>

#This is the main window - you can see the tk window tab at the top
menuwindow = tk.Tk()
menuwindow.geometry("835x635")

#These are canvases, these are where the information of each page will sit depending on which one.
#Under this is all the image screen canvases
#<---------->
#This is the menu screen canvas
menuplatform = tk.Canvas(menuwindow, width=835, height=635)
#This is the info page canvas
infopageplatform = tk.Canvas(menuwindow, width=835, height = 635)

#Under this is all the button canvases
#<---------->
#This is the BEGIN button canvas
beginbuttonplatform= tk.Canvas(menuwindow, width=50, height=50)
#This is the Yesbutton canvas
yesbuttonplatform= tk.Canvas(menuwindow, width=50, height=50)
#This is the No button canvas
nobuttonplatform= tk.Canvas(menuwindow, width=50, height=50)

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



  
def closequiz():
  menuwindow.destroy()
#<------------------------>


#FIRST QUESTION CODE
#<------------------------>
firstques_img = ImageTk.PhotoImage(file="question1.jpeg") #Directory file finder


#<------------------------>

#MENU SCREEN IMAGE CODE
#<--------------------->
valorant_img = ImageTk.PhotoImage(file="val.png") #Directory file finder
#This is to actually show the canvas
menuplatform.pack()
#This is the code to call the image
menu = ImageTk.PhotoImage(Image.open("val.png"))
menuimage = tk.Label(menuwindow, image=menu)
#This is to actually show the image
menuimage.pack()

menuplatform.create_image(415, 315, image=valorant_img)
#<--------------------->

#YES AND NO BUTTON CODE
#<-------------------->
yesbtn = tk.Button(text="Yes", command = firstques)
yesbtn.configure(width=10)
nobtn = tk.Button(text="No", command = closequiz)
nobtn.configure(width=10)
#<-------------------->

#BEGIN BUTTON CODE
#<------------------------>
#This finds the file for the image of the "BEGIN" button.
begin_image = ImageTk.PhotoImage(Image.open("button.png")) #^Directory file finder
#This creates the area for the BEGIN button to actually work.
begin_button = tk.Button(text="Start the Test", image=begin_image, command = disclaimer)
begin_button.configure(width=227)
begin_button_window = beginbuttonplatform.create_window(30, 40)
#This places the "BEGIN" button where I want it to be - note the coordinates.
infopage_img = ImageTk.PhotoImage(file="info page.png") #Directory file finder

begin_button.place(x=287, y=350)
#<------------------------>


print("Running")
