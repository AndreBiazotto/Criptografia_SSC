import numpy as np

m2 = np.array([[8, 5, 10],
                   [21, 8, 21],
                   [21, 12, 8]])


m1 = np.array([[6, 24, 1],
                   [13, 16, 10],
                   [20, 17, 15]])

print(np.linalg.inv(m1) % 26)
print(m2 % 26)