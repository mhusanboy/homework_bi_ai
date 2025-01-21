#1
def problem1():
    a = tuple(input("tuple: ").split())
    b = input("element: ")
    print(a.count(b))

#2
def problem2():
    a = tuple(map(int, input("tuple: ").split()))
    print(max(a))

#3
def problem3():
    a = tuple(map(int, input("tuple: ").split()))
    print(min(a))

#4
def problem4():
    a = tuple(input("tuple: ").split())
    b = input("element: ")
    print(b in a)

#5
def problem5():
    a = tuple(input("tuple: ").split())
    print(a[0] if len(a) else "empty")

#6
def problem6():
    a = tuple(input("tuple: ").split())
    print(a[-1] if len(a) else "empty")

#7
def problem7():
    a = tuple(input("tuple: ").split())
    print(len(a))

#8
def problem8():
    a = tuple(input("tuple: ").split())
    print(a[:3])

#9
def problem9():
    a = tuple(input("tuple1: ").split())
    b = tuple(input("tuple2: ").split())
    print(a + b)

#10
def problem10():
    a = tuple(input("tuple: ").split())
    print(not a)

#11
def problem11():
    a = tuple(input("tuple: ").split())
    b = input("element: ")
    print(tuple(i for i in range(len(a)) if a[i] == b))

#12
def problem12():
    a = tuple(sorted(set(map(int, input("tuple: ").split()))))
    print(a[-2] if len(a) > 1 else "No second largest")

#13
def problem13():
    a = tuple(sorted(set(map(int, input("tuple: ").split()))))
    print(a[1] if len(a) > 1 else "No second smallest")

#14
def problem14():
    b = input("element: ")
    print((b,))

#15
def problem15():
    a = list(input("list: ").split())
    print(tuple(a))

#16
def problem16():
    a = tuple(map(int, input("tuple: ").split()))
    print(a == tuple(sorted(a)))

#17
def problem17():
    a = tuple(map(int, input("tuple: ").split()))
    b, c = map(int, input("range: ").split())
    print(max(a[b:c]))

#18
def problem18():
    a = tuple(map(int, input("tuple: ").split()))
    b, c = map(int, input("range: ").split())
    print(min(a[b:c]))

#19
def problem19():
    a = tuple(input("tuple: ").split())
    b = input("element: ")
    print(tuple(x for i, x in enumerate(a) if x != b or i != a.index(b)))

#20
def problem20():
    a = tuple(input("tuple: ").split())
    n = int(input("size: "))
    print(tuple(tuple(a[i:min(i + n, len(a))]) for i in range(0, len(a), n)))

#21
def problem21():
    a = tuple(input("tuple: ").split())
    n = int(input("number: "))
    print(tuple(x for x in a for _ in range(n)))

#22
def problem22():
    l, r = map(int, input("range: ").split())
    print(tuple(range(l, r + 1)))

#23
def problem23():
    a = tuple(input("tuple: ").split())
    print(a[::-1])

#24
def problem24():
    a = tuple(input("tuple: ").split())
    print(a == a[::-1])

#25
def problem25():
    a = tuple(input("tuple: ").split())
    b = []
    b.extend(x for x in a if x not in b)
    print(tuple(b))

problem20()