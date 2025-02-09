import numpy as np


#task1
@np.vectorize
def far_to_cel(f):
    return (f - 32) * 5 / 9
a = np.array([32, 68, 100, 212, 77])
ta = far_to_cel(a)


#task2
@np.vectorize
def power(a, n):
    return a**n 


a = np.array([2, 3, 4, 5])
b = np.array([1, 2, 3, 4])
print(power(a, b).tolist())


#task3

w = np.array([
    [4, 5, 6],
    [3, -1, -1],
    [2, 1, -2]
])
y = np.array([7, 4, 5])
print(np.linalg.solve(w, y).tolist())


#task4
w = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
y = np.array([12, -5, 15])
print(np.linalg.solve(w, y))