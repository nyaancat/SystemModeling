from math import cos
from tkinter import *

t1 = 0.0
x0 = 0.7
y0 = 2
dt = float(0.01)
sc = 100
a1 = -3.0
a2 = -5.0

root = Tk()

canv = Canvas(root, width = 1000, height = 1000, bg = "white", cursor = "pencil")
canv.create_line(500,1000,500,0,width=2,arrow=LAST)
canv.create_line(0,500,1000,500,width=2,arrow=LAST)

while t1 <= 100:
    x2 = x0 + dt * (a1 * x0 + y0 * x0 * x0 + y0 * x0 * x0 * x0 + y0 * x0 * x0 * x0 * x0)
    y2 = y0 + dt * (a2 * y0 + x0 * y0 * y0 + x0 * y0 * y0 * y0 + x0 * y0 * y0 * y0 * y0)
    canv.create_line(500 + x0 * sc, 500 - y0 * sc, 500 + x2 * sc, 500 - y2 * sc, fill="black")
    x0 = x2
    y0 = y2
    t1 += dt

canv.pack()
root.mainloop()