import random

random.seed()
for i in range(10):
    pointsSum = 0
    for j in range(500):
        point = random.randint(1, 6)
        pointsSum += point
    print(pointsSum / 500)



