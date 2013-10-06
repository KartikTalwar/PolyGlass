from pprint import pprint as pp
import pylab
import scipy.fftpack
import scipy.interpolate
import numpy as np

x = open('dd', 'r').read()
d = eval(x)

a = []

for i in d:
  for j in i:
    a.append(j)

a = map(lambda x:x[1], a)
cut = a[61]
a = filter(lambda x: x>cut, a)

pylab.plot(np.arange(0, len(a)/2), map(lambda i:i*1.0/(10**8),a[::2]))
pylab.show()


