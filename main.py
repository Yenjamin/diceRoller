from io import BytesIO
from tkinter import *
from PIL import Image, ImageTk
import random


def roll():
    img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    numberRolled.configure(image=img)
    numberRolled.image = img

window = Tk()
window.geometry("400x400")
window.title("Dice Roller")
blank = Label(window, text="")
blank.pack()
heading = Label(window, text="Roll the Dice!!!!", fg = "light green", bg = "dark green", font = "Helvetica 16 bold italic")
heading.pack()
dice = ["die1.png", "die2.png", "die3.png", "die4.png", "die5.png", "die6.png"]
img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
numberRolled = Label(window, image=img)
numberRolled.image = img
numberRolled.pack( expand=True)
button = Button(window, text="   Roll!!!   ", fg="blue", command=roll)
button.pack( expand=True)
window.mainloop()