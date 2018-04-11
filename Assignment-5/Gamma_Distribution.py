import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

x = np.linspace(0, 50)
y1 = stats.gamma.pdf(x, a=1, scale=1)
y2 = stats.gamma.pdf(x, a=1, scale=5)
y3 = stats.gamma.pdf(x, a=1, scale=10)
y4 = stats.gamma.pdf(x, a=5, scale=1)
y5 = stats.gamma.pdf(x, a=10, scale=1)
y6 = stats.gamma.pdf(x, a=10, scale=2)

plt.plot(x, y1, c='black', label=r'$\alpha=1, \theta=1$')
plt.plot(x, y2, c='red', label=r'$\alpha=1, \theta=5$')
plt.plot(x, y3, c='blue', label=r'$\alpha=1, \theta=10$')
plt.plot(x, y4, c='yellow', label=r'$\alpha=5, \theta=1$')
plt.plot(x, y5, c='green', label=r'$\alpha=10, \theta=1$')
plt.plot(x, y6, c='purple', label=r'$\alpha=10, \theta=2$')

plt.legend()
plt.ylim(0,.5)
plt.xlim(0, 50)
plt.grid(True)
plt.title('Gamma Distributions')
plt.show()
