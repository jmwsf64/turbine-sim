import random
import numpy as np

# generate 24 random numbers between 1 and 255
# cannot use 0, 10, 13, 14 (possibly others)

vals = np.random.randint(1, high=255, size=(24, 1))
for i in range(24):
    print(i, '|', vals[i][0])
