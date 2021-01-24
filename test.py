import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(1,10,100)
y = np.exp(x)
plt.plot(x,y,ls=':',c='r',label='exp')
plt.legend()
plt.show()