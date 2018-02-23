import matplotlib.pyplot as plt

boy_height = [65,67,72.5,71,82,59,62,63.4,66,65,73,71,72]
girl_height = [58,56.5,54,60,62,59,60.5,61,63,65,66,61.5,62.5]

plt.hist(boy_height, bins=5, rwidth=0.5, color='r', normed=True, label='Boys')
plt.hist(girl_height, bins=5, rwidth=0.8 ,color='b', normed=True, alpha=0.5, label='Girls')

plt.title("STUDENT HEIGHTS’")
plt.xlabel("Height (inches)")
plt.ylabel("Frequency")
plt.legend()
plt.show()
