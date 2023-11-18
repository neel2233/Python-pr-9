import numpy as np

filename = input("Ведите название файла с матрицей")
matrix = []
with open(filename, "r") as file:
    for row in file:
        row = list(map(int, row[:-1].split(",")))
        matrix.append(row)
matrix = np.array(matrix)
print(f"max:{matrix.max()} min:{matrix.min()} sum:{matrix.sum()}")
