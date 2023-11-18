import numpy as np

a = [0, 1, 2, 0, 0, 4, 0, 6, 9]
indexes = np.nonzero(a)[0]
print(indexes)
