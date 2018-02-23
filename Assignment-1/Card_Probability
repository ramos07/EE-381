import random

suit = ["D", "S", "C", "H"]
rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "K", "Q", "J"]
counter1 = 0
counter2 = 0

for x in range(200):
    a = str(random.choice(suit))
    b = str(random.choice(rank))
    card = a + b
    if "Q" in card:
        counter1 = counter1 + 1
        print(card)

print("Probablility of drawing one Queen from 200 drawn cards is", counter1 / 200)

for x in range(200):
    x  = str(random.choice(suit))
    y = str(random.choice(rank))
    x_2  = str(random.choice(suit))
    y_2 = str(random.choice(rank) )
    card1 = x+y
    card2 = x_2+y_2
    if (("Q" in card1) and ("D" in  card2)):
        print(card1, card2)
        counter2 = counter2 + 1
    elif (("D" in card1)and ("Q" in card2)):
        print(card1, card2)
        counter2 = counter2 + 1

print("Probablility of drawing one Queen and one Diamond from 200 drawn pairs is", counter2/200)

