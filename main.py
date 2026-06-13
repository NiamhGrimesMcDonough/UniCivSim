import tkinter as tk
from tkinter import *
from Galaxy import GenerateStars
import random as rn

canvas_width = 500
canvas_height = 500

master = Tk()
master.title("Points")
w = Canvas(master,
    width=canvas_width,
    height=canvas_height,
    bg="black")
w.pack(expand=YES, fill=BOTH)
master.after(100, lambda: GenerateStars(w, rn.randrange(100000000000, 400000000000)))
mainloop()

print("Generating Stars")