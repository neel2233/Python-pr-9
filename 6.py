import numpy as np

a = np.arange(16).reshape(4, 4)
print(a)
a0 = a[0].copy()
a2 = a[2].copy()
a[0], a[2] = a2, a0
print(a)
