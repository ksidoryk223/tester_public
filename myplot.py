import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,4*np.pi,100)
y = np.sin(x)

plt.plot(x,y)
plt.show()


