import random

n = 0

for i in range(1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 + dice2 == 5:
        n += 1
        

print ((n / 1000) * 100)