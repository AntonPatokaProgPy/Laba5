import numpy as np



a1 = np.arange(1,11)
print(*a1)
print('----------------------------')
a2 = np.random.randint(-100,100,9).reshape(3,3)
print(a2)
print('----------------------------')
a3 = np.array([0 for i in range(10)])
a3[2] = 5
print(*a3)
print('----------------------------')
a4 = np.arange(1,13).reshape(3,4)
print(a4)
print('----------------------------')
a5 = np.random.randint(0,10,25).reshape(5,5)
print(a5)
print(sum(sum(a5)))
print('----------------------------')
a6 = np.random.randint(1,11,16).reshape(4,4)
print(a6)
print([max(i) for i in a6])
print('----------------------------')
a7 = np.random.randint(-10,10,9).reshape(3,3)
print(a7)
a7 *= 2
print(a7)
print('----------------------------')
a8_1 = np.random.randint(-10,0,9).reshape(3,3)
a8_2 = np.random.randint(0,11,9).reshape(3,3)
print("Матрица А")
print(a8_1)
print("Матрица Б")
print(a8_2)
print("Произведение матрицы А и матрицы Б")
result = np.dot(a8_1,a8_2)
print(result)
print('----------------------------')
a9 = np.random.randint(0,6,9).reshape(3,3)
det = np.linalg.det(a9)
print(a9)
print(round(det))
