from matrix import Matrix


m = Matrix([[1, 2], [3, 4]])
# m = Matrix([1, 2, 3])
# m = Matrix([[1, 2], [3, 4], [5, 6]])

for val in m:
    for i in val:
        print(i)
