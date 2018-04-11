import random
import matplotlib.pyplot as plt

dollar_per_person = []
for _ in range(50):
    dollar_per_person.append(50)

for _ in range(50):
    for i in range(50):
        dollar_per_person[i] = dollar_per_person[i]-1
        random_person = random.randint(0,49)
        dollar_per_person[random_person]=dollar_per_person[random_person]+1

plt.plot(dollar_per_person)
plt.axis([0, 50, 0, 100])
plt.title('Who could be rich?')
plt.xlabel('Number of people')
plt.ylabel('Money amount')
plt.show()

print(sorted(dollar_per_person, reverse=True))
