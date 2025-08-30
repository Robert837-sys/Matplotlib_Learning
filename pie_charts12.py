import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([35, 25, 25, 15])
mylabels=["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors=["black", "hotpink", "b", "#4CAF50"]

plt.pie(x,labels=mylabels,explode=myexplode,shadow=True,colors=mycolors)
plt.legend()
plt.show()