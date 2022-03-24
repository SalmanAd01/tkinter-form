from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("800x600")

frame = Frame(win)
frame.pack()
frame.place(anchor='center', x=400, y=200)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(
    "C:/Users/salman/OneDrive/Desktop/Form/static/values-1.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.pack()

win.mainloop()
