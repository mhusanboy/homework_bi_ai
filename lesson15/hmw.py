import numpy as np

#1
def problem1():
    a = np.arange(10, 50)

#2
def problem2():
    a = np.arange(0, 9)
    a.resize((3, 3))
    print(a)

#3
def problem3():
    a = np.eye(3, 3)
    print(a)

#4
def problem4():
    a = np.random.randint(0, 100, (3, 3, 3))
    print(a)

#5 
def problem5():
    a = np.random.randint(0, 10**5, (10, 10))
    print(a.max(), a.min())

#6
def problem6():
    a = np.random.randint(0, 10**5, (30))
    print(a.sum()/len(a))

#7
def problem7():
    a = np.random.randint(0, 10**5, (5, 5))
    mn, mx = a.max(), a.min()
    na = (a - mn) / (mx - mn)
    print(a, na)

#8
def problem8():
    a = np.random.randint(0, 100, (5, 3))
    b = np.random.randint(0, 100, (3, 2))
    print(a @ b)

#9
def problem9():
    a = np.random.randint(0, 100, (3, 3))
    b = np.random.randint(0, 100, (3, 3))
    print(np.dot(a, b), a * b)

#10
def problem10():
    a = np.random.randint(0, 100, (4,4))
    print(a.T)

#11
def problem11():
    a = np.random.randint(0, 100, (3, 3))
    print(a, np.linalg.det(a))

#12
def problem12():
    a = np.random.randint(0, 100, (3, 4))
    b = np.random.randint(0, 100, (4, 3))
    print(np.dot(a, b))

#13
def problem13():
    a = np.random.randint(0, 100, (3, 3))
    b = np.random.randint(0, 100, (3, 1))
    print(a @ b)

#14
def problem14():
    a = np.random.randint(0, 100, (3, 3))
    b = np.random.randint(0, 100, (3, 1))
    print(np.linalg.inv(a) @ b)
    print(np.linalg.solve(a, b))

#15
def problem15():
    a = np.random.randint(0, 2, (5, 5))
    print("rowwise: ", a.sum(axis = 1))
    print("columnwise: ", a.sum(axis = 0))

