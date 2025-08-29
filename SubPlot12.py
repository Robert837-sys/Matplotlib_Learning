import matplotlib.pyplot as plt 
import numpy as np 

# plot1 
x=np.array([0, 1, 2, 3])
y=np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y,'r') # 'r' is color red
plt.title("SALES")

# plot2 
x=np.array([0, 1, 2, 3])
y=np.array([10, 20, 30, 40])

plt.subplot(1,2,2)
plt.plot(x,y,'b') # 'b' is color blue
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()
