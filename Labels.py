import numpy as np 
import matplotlib.pyplot as plt 

x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data", fontsize=20, color="blue")
plt.xlabel("Average Pulse", fontsize=14, color="red")
plt.ylabel("Calorie Burnage", fontsize=14, color="red")

plt.show()