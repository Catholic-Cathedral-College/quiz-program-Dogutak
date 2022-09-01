import tkinter as tk
from PIL import ImageTk, Image

#This is the main window - you can see the tk window tab at the top
root = tk.Tk()
root.geometry("835x635")

#This is a canvas, this is where the image will belong
# - This is the code to make the canvas exist and where it will be (position, size etc)
canvas = tk.Canvas(root, width=835, height=635)
tk_img = ImageTk.PhotoImage(file = "val.png")
canvas.create_image(415, 315, image=tk_img)
#This is to actually show the canvas
canvas.pack()


#This is the code to call the image
menu = ImageTk.PhotoImage(Image.open("val.png"))
menuimage = tk.Label(root,image = menu)
#This is to actually show the image
menuimage.pack()

canvas1 = tk.Canvas(root, width=50, height=50)
play_button = tk.Button(text = "Start the Test")
play_button.configure(width=50)
play_button_window = canvas1.create_window(30,40)
play_button.pack()

play_button.place(x=200, y=340)

