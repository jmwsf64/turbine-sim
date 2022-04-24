import random
import numpy as np

# generate 24 random numbers between 1 and 255
# cannot use 0, 10, 13, 14 (possibly others)
# vals = np.random.randint(1, high=255, size=(24, 1))
# for i in range(24):
#     print(i, '|', vals[i][0])
val = np.random.randint(1, high=255)
print(val)


# generate random data to use in readWrite-test.py
# x = np.array([[[0, 1, 2, 3, 4],
#                [5, 6, 7, 8, 9]],
#               [[10, 11, 12, 13, 14],
#                [15, 16, 17, 18, 19]],
#               [[20, 21, 22, 23, 24],
#                [25, 26, 27, 28, 29]]])
# dims = x.shape

# u = np.random.normal(loc=0.0, scale=1.0, size=dims)
# u = np.random.random(dims)*10
# print(u)
