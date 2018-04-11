import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8])
y = np.array([0,0.8,0.9,0.1,-0.8,-1,-1.2,-1.6,-1.9])

xfit = np.linspace(-2, 10, 1000)
p3 = np.polyfit(x, y, 3)
yfit = np.polyval(p3, xfit)
plt.plot(x, y, 'o', label='data set')
plt.plot(xfit, yfit, '.', label='Third Order Fit')
plt.xlabel('x')
plt.ylabel('y')


p1 = np.polyfit(x, y, 1)
yfit = np.polyval(p1, xfit)
plt.plot(xfit, yfit, '_', label='One Order Fit')
plt.xlabel('x')
plt.ylabel('y')
print(" Coefficients for thirder order fitting: ", p3)
print(" Coefficients for one order fitting", p1)

plt.title('One & Third Order Fittings')
plt.show()
