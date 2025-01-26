import random
numberOfRolls = int(input())

sumOfPoints = 0
for i in range(numberOfRolls):
    deckSize = 36
    draw = 0
    drawn = random.randint(1, deckSize)
    while (drawn != 1):
        deckSize -= 1
        drawn = random.randint(1,deckSize)
        draw += 1
    sumOfPoints += draw

print((sumOfPoints/numberOfRolls))