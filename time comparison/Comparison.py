import numpy as np
import matplotlib.pyplot as plt

# x axis values
x = [15,16,17,18,19,20,21,22,23]
# corresponding y axis values
#y = [89,64,89,100,81,90,84,81,83]
y=[360503.64,242936.7,384372.7,370310.02,390499.86,438347.37,508325.63,432653.74,556781.71]
z=[360503.64,242936.7,384372.7,360471.88,390499.86,438347.37,508325.63,423825.65,556781.71]
a=[360503.64,256574.88,384372.7,406534.09,401983.13,438266.94,402797.31,399702.35,514573.03]
b=[404469.24,398443.36,434193.06,406534.09,497464.22,486855.98,549965.01,495460.96,617190.61]


#plt.figure(dpi=250)
plt.plot(x, y, linestyle = 'dashed', marker='o', color='blue') # kmeans
plt.plot(x, z, linestyle = 'dashed', marker='o', color='orange') #kmedoids
plt.plot(x, a, linestyle = 'dashed', marker='o', color='green') # similarity
plt.plot(x, b, linestyle = 'dashed', marker='o', color='red') # optimal

plt.xlabel('Number of agents')
plt.ylabel('V(CS) value')
plt.text(-5, 60, 'Parabola $Y = x^2$', fontsize = 22)
#plt.legend(loc='upper left')
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
plt.savefig("comparison",dpi=300)
plt.show()

