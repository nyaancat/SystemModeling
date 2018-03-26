import math
import pylab
import numpy
import matplotlib.pyplot
from matplotlib import mlab

def func (x, h, N):
    k = 0.01
    return (x + h * k * x * (N - x))

# Шаг
h = 0.01
a = 1
N = 100
x = a

tmin = 0.0
tmax = 100.0

t = tmin
tlist = [t]
xlist = [x]
while (x < 0.95 * N):
  x = func(x, h, N)
  xlist.append(x)
  t += h
  tlist.append(t)

pylab.plot (numpy.array(tlist), numpy.array(xlist))
pylab.show()