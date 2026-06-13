from tkinter import *




def paint(canvas, x, y, colour):
    x1, y1 = x/1000000000, y/1000000000
    canvas.create_oval(x1-0.001+500, y1-0.001+500, x1+0.001+500, y1+0.001+500, fill=colour)