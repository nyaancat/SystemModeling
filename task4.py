import random

random.seed()
mu = 0
o = 1

isOk = 0
for k in range(1000):
    discrepancy = 0
    for i in range(7):
        rand = 0
        for j in range(12):
            rand += random.random()
        rand -= 6
        rand *= o
        rand += mu
        discrepancy += rand
    if discrepancy > 2:
        isOk += 1

print(isOk / 1000)




