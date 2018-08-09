#import numpy as np
import matplotlib.pyplot as plt

import Module_PY33.teste_PyPI as epamod

#import simpy

#a = np.arange(1, 11)
#b = np.arange(10, 20)

x = epamod()
print(x)
y = list(range(0,259200,3600))
#x = np.arange(0, 100, 10)
#y = np.arange(0, 100, 10)

#print(a, b)

#print(np.polyfit(ax, by, 1))
#p = np.polyfit(x, y, 1)

#yfit = np.polyval(p, x)

#print(c)
plt.plot(x, y, label = 'dados')
#plt.plot(x, yfit, label = 'fit')
#plt.plot(x, yfit - y, label = 'var')

#plt.plot_date(a,b)
#plt.fill(a, b, 'b')
#plt.plot(ax, c[0]*ax + c[1])

plt.show()

#plt = simpy.
#plt.plotLine ([0, 0], [1, 1], [2, 4], [3, 9])
#plt.mainloop()

