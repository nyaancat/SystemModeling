from math import cos
from tkinter import *
import random

random.seed()

root = Tk()
canv = Canvas(root, width = 1000, height = 1000, bg = "white", cursor = "pencil")
canv.create_line(500,1000,500,0,width=2,arrow=LAST)
canv.create_line(0,500,1000,500,width=2,arrow=LAST)

for i in range(30):
    t1 = 0.0
    x0 = random.uniform(-3.0, 3.0)
    y0 = random.uniform(-3.0, 3.0)
    dt = float(0.01)
    sc = 70
    a1 = random.uniform(-10, -0.01)
    a2 = random.uniform(a1, 0)
    while t1 <= 50:
        x2 = x0 + dt * (a1 * x0 + y0 * x0 * x0 + y0 * x0 * x0 * x0 + y0 * x0 * x0 * x0 * x0)
        y2 = y0 + dt * (a2 * y0 + x0 * y0 * y0 + x0 * y0 * y0 * y0 + x0 * y0 * y0 * y0 * y0)
        canv.create_line(500 + x0 * sc, 500 - y0 * sc, 500 + x2 * sc, 500 - y2 * sc, fill="black")
        x0 = x2
        y0 = y2
        t1 += dt

canv.pack()
root.mainloop()