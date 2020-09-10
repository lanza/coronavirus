import matplotlib
import numpy


a = [1,2,3,4]

c, b = zip(*enumerate(a))
print(b, c)