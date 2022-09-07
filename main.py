import tkinter as tk
from PIL import ImageTk, Image

#This is the main window - you can see the tk window tab at the top
menuwindow = tk.Tk()
menuwindow.geometry("835x635")

#These are canvases, these are where the information of each page will sit depending on which one.
#This is the menu screen canvas
menuplatform = tk.Canvas(menuwindow, width=835, height=635)
#This is the BEGIN button canvas
playbuttonplatform= tk.Canvas(menuwindow, width=50, height=50)
#This is the info page canvas
firstpageplatform = tk.Canvas(menuwindow, width=835, height = 635)
def start():
  play_button.destroy()
  menuplatform.create_image(415, 315, image=infopage_img)


valorant_img = ImageTk.PhotoImage(file="val.png")
menuplatform.create_image(415, 315, image=valorant_img)
#This is to actually show the canvas
menuplatform.pack()

#This is the code to call the image
menu = ImageTk.PhotoImage(Image.open("val.png"))
menuimage = tk.Label(menuwindow, image=menu)
#This is to actually show the image
menuimage.pack()

#This finds the file for the image of the "BEGIN" button.
begin_image = ImageTk.PhotoImage(Image.open("button.png"))

#This creates the area for the BEGIN button to actually work.

play_button = tk.Button(text="Start the Test", image=begin_image, command = start)
play_button.configure(width=227)
play_button_window = playbuttonplatform.create_window(30, 40)

#This places the "BEGIN" button where I want it to be - note the coordinates.
play_button.place(x=287, y=350)
infopage_img = ImageTk.PhotoImage(file="info page.png")



print("Running")
