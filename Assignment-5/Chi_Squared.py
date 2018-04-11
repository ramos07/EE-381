from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 25, 1000)
fig,ax = plt.subplots(1,1)

linestyles = ['--','-']
deg_of_freedom = [1, 10]
for df, ls in zip(deg_of_freedom, linestyles):
  ax.plot(x, stats.chi2.pdf(x, df), linestyle=ls, label=r'$df=%i$' % df)

plt.xlim(0, 25)
plt.ylim(0, 0.5)
plt.title(r'$\chi^2\ \mathrm{Distribution}$')

plt.legend()
plt.show()
