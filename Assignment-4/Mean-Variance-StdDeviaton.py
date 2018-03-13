from random import *
import numpy as np
import matplotlib.pyplot as plt


#Creat the list with random values
myList = [(uniform(-1, 1),) for k in range(2000)]
rList = np.round(myList, 3)

#Calculate the variance of the values
variance = np.var(myList)
rVar = round(variance,3)

#Calculate the mean of the values
avg = np.mean(myList)
rAvg = round(avg, 3)

#Calculate the standard deviation of the values
stdDev= np.std(myList, dtype=np.float64)
rstdDev = round(stdDev, 3)

#Print all elements
print('Mean: ', rAvg)
print('Variance: ', rVar)
print('Standard Deviation: ', rstdDev)

# Creating the  histogram
n, bins, patches = plt.hist(rList, bins='auto', density=1, facecolor='green', alpha=0.75)

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram for 2000 Random Values')
plt.show()


