import numpy as np

rng = np.random.normal(size=(10, 4))

minRng = rng.min()
maxRng = rng.max()
avgRng = rng.mean()
stdRng = rng.std()
print(f"Минимум:{minRng} Максимум:{maxRng}, Среднее значение:{avgRng}, Стандартное отклонение:{stdRng}")
rngf5 = rng.copy()[:5]

