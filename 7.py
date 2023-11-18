import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
parts, counter = np.unique(iris, return_counts=True)
print(parts)
print(counter)
