import numpy as np

x = np.array(list(map(int, input().split())))
indices = np.where(x[:-1] != x[1:])[0]
indices = np.concatenate((indices, [len(x) - 1]))
parts = np.split(x, indices + 1)[:-1]
values = np.array([])
counts = np.array([])
for part in parts:
    value, count = np.unique(part, return_counts=True)
    values = np.concatenate((values, value))
    counts = np.concatenate((counts, count))

print(values, counts)


