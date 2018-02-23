import random

counter = 0
for x in range(1, 11):
    z = random.randint(1, 6)
    print(z)
    if (z == 1):
        counter = counter + 1

print("The probability of rolling a 1 after 10 times rolling a die is :", counter / 10)
