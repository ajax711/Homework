n=int(input("How many vertices in the polygon"))
xpoints=[]
ypoints=[]
for i in range(n):
    xpoints[i]=int(input("x"+str(i)))
    ypoints[i]=int(input("y"+str(i)))

import matplotlib.pyplot as plt
plt.plot(xpoints,ypoints) 
plt.show()
