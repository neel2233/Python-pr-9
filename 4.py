import numpy as np

x = np.array(list(map(int, input().split())))
indices = np.where(x != np.where(x == 0, np.nan, x))[0]
parts = np.split(x, indices)[1:]
for i in range(len(parts)):
    parts[i] = np.concatenate((parts[i], np.zeros(1)))
    parts[i] = parts[i][1]
print(max(parts))
