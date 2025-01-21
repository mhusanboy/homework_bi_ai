#1
def problem1():
    a = float(input())
    print(round(a, 2))

#2
def problem2():
    a = int(input("number1: "))
    b = int(input("number2: "))
    c = int(input("number3: "))
    print(max(a, b, c), min(a, b, c))

#3
def problem3():
    km = float(input("kilometers: "))
    print(int(km * 1000), int(km * 100000))

#4
def problem4():
    a = int(input("number1: "))
    b = int(input("number2: "))
    print(a // b, a % b)

#5
def problem5():
    c = float(input("celsius: "))
    print(c * 9 / 5 + 32)

#6
def problem6():
    a = int(input("number: "))
    print(a % 10)

#7
def problem7():
    a = int(input("number: "))
    print(a % 2 == 0)

problem1()