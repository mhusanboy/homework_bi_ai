#1
def problem1():
    a = set(input("set1: ").split())
    b = set(input("set2: ").split())
    print(a | b)

#2
def problem2():
    a = set(input("set1: ").split())
    b = set(input("set2: ").split())
    print(a & b)

#3
def problem3():
    a = set(input("set1: ").split())
    b = set(input("set2: ").split())
    print(a - b)

#4
def problem4():
    a = set(input("set1: ").split())
    b = set(input("set2: ").split())
    print(a <= b or b <= a)

#5
def problem5():
    a = set(input("set: ").split())
    b = input("element: ")
    print(b in a)

#6
def problem6():
    a = set(input("set: ").split())
    print(len(a))

#7
def problem7():
    a = list(input("list: ").split())
    print(set(a))

#8
def problem8():
    a = set(input("set: ").split())
    b = input("element: ")
    a.discard(b)
    print(a)

#9
def problem9():
    a = set(input("set: ").split())
    a.clear()
    print(a)

#10
def problem10():
    a = set(input("set: ").split())
    print(not a)

#11
def problem11():
    a = set(input("set1: ").split())
    b = set(input("set2: ").split())
    print(a ^ b)

#12
def problem12():
    a = set(input("set: ").split())
    b = input("element: ")
    a.add(b)
    print(a)

#13
def problem13():
    a = set(input("set: ").split())
    print(a.pop(), a)

#14
def problem14():
    a = set(map(int, input("set: ").split()))
    print(max(a))

#15
def problem15():
    a = set(map(int, input("set: ").split()))
    print(min(a))

#16
def problem16():
    a = set(map(int, input("set: ").split()))
    print({x for x in a if x % 2 == 0})

#17
def problem17():
    a = set(map(int, input("set: ").split()))
    print({x for x in a if x % 2 != 0})

#18
def problem18():
    l, r = map(int, input("range: ").split())
    print(set(range(l, r + 1)))

#19
def problem19():
    a = list(input("list1: ").split())
    b = list(input("list2: ").split())
    print(set(a + b))

#20
def problem20():
    a = set(input("set1: ").split())
    b = set(input("set2: ").split())
    print(len(a&b) == 0)

#21
def problem21():
    a = list(input("list: ").split())
    print(list(set(a)))

#22
def problem22():
    a = list(input("list: ").split())
    print(len(set(a)))

#23
def problem23():
    import random
    n, l, r = map(int, input("count range_start range_end: ").split())
    print({random.randint(l, r) for _ in range(n)})


# problem20()