import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,6*np.pi,0.01)
y = np.sin(x)
z = np.tan(x)
t = np.cos(x)
plt.plot(x,y,x,z,x,t)
plt.title("sin vs cos vs tan")
plt.xlabel("time")
plt.ylabel('graph')
plt.show()

