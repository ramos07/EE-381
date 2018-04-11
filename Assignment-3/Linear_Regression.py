import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import  LinearRegression

#x and y values are inserted into two arrays
x = np.array([0,1,2,3,4,5,6,7,8])
y = np.array([0,0.8,0.9,0.1,-0.8,-1,-1.2,-1.6,-1.9])

#model variable set to hold the linear regression estimation
model = LinearRegression(fit_intercept=True)

#fit the x data into the modle variable
model.fit(x[:,  np.newaxis], y)

#set the spacing for the chart to plot the data for x and y values
xfit = np.linspace(0, 8, 1000)
yfit = model.predict(xfit[:,    np.newaxis])


plt.scatter(x, y, color='black')
plt.title('One Order Equation y=ax+b')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.plot(xfit, yfit)    #plot the x and y fitted data
print("a coefficient: ", model.coef_[0]) #calculate the a coefficient
print("b coefficient: ", model.intercept_)  #calculate the b coefficient
plt.show()
