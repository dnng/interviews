# ================================================================================
# O(n) processing complexity
# O(n) memory complexity
# ================================================================================
from math import sqrt

data1 = open('dataset1.csv', 'r')
data2 = open('dataset2.csv', 'r')

d1 = {}
fast_dinos = {}

# Hash table to index unordered dataset
for line in data1:
    i1 = line.strip().split(',')
    d1[i1[0]] = i1[1]

for line in data2:
    i2 = line.strip().split(',')
    if i2[2] == 'bipedal':
        leg = d1[i2[0]]
        speed = ((float(i2[1]) / float(leg)) -1) * sqrt(float(leg) * 9.8)
        # save i2 giving speed as key
        # we save the name as key because its unique in the dataset
        fast_dinos[i2[0]] = speed

for dino in reversed(sorted(fast_dinos, key=fast_dinos.get)):
        print dino, fast_dinos[dino],
