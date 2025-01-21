#1
def problem1():
    u = input("Username: ")
    p = input("Password: ")
    print("not empty" if bool(u) and bool(p) else "empty")



#2
def problem2():
    a = int(input("number1: "))
    b = int(input("number2: "))
    print(a == b)



#3
def problem3():
    a = int(input("input a number: "))
    print(a % 2 == 0 and a > 0)



#4
def problem4():
    a = int(input("number1: "))
    b = int(input("number2: "))
    c = int(input("number3: "))
    print(a != b and a != c and b != c)


#5
def problem5():
    a = input("string1: ")
    b = input("string2: ")
    print(len(a) == len(b))


#6
def problem6():
    a = int(input("number: "))
    print(a % 15 == 0)


#7
def problem7():
    a = int(input())
    b = int(input())
    print(a + b > 50.8)
