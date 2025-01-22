#1
def problem1():
    a = list(input("list: ").split())
    b = input("element: ")
    print(a.count(b))

#2
def problem2():
    print(sum(list(map(int, input("list: ").split()))))

#3
def problem3():
    print(max(list(map(int, input("list: ").split()))))

#4
def problem4():
    print(min(list(map(int, input("list: ").split()))))

#5
def problem5():
    a = input("list: ").split()
    b = input("element: ")
    print(b in a)

#6
def problem6():
    a = input("list: ").split()
    print(a[0] if len(a) else "empty")

#7
def problem7():
    a = input("list: ").split()
    print(a[-1] if len(a) else "empty")

#8
def problem8():
    print(input("list: ").split()[:3])

#9
def problem9():
    print(input("list: ").split()[::-1])

#10
def problem10():
    print(sorted(input("list: ").split(), key=int))

#11
def problem11():
    print(list(set(input("list: ").split())))

#12
def problem12():
    a = input("list: ").split()
    b = input("element: ")
    c = int(input("index: "))
    a.insert(c, b)
    print(a)

#13
def problem13():
    a = input("list: ").split()
    b = input("element: ")
    print(a.index(b) if b in a else -1)

#14
def problem14():
    print(not input("list: ").split())

#15
def problem15():
    print(sum(1 for x in map(int, input("list: ").split()) if x % 2 == 0))

#16
def problem16():
    print(sum(1 for x in map(int, input("list: ").split()) if x % 2 != 0))

#17
def problem17():
    a = input("list1: ").split()
    b = input("list2: ").split()
    print(a + b)

#18
def problem18():
    a = input("list: ").split()
    b = input("sublist: ").split()
    print(" ".join(b) in " ".join(a))

#19
def problem19():
    a = input("list: ").split()
    b = input("old element: ") 
    c = input("new element: ")
    if b in a: 
        a[a.index(b)] = c
    print(a)

#20
def problem20():
    a = sorted(set(map(int, input("list: ").split())))
    print(a[-2] if len(a) > 1 else "No second largest")

#21
def problem21():
    a = sorted(set(map(int, input("list: ").split())))
    print(a[1] if len(a) > 1 else "No second smallest")

#22
def problem22():
    print([x for x in map(int, input("list: ").split()) if x % 2 == 0])

#23
def problem23():
    print([x for x in map(int, input("list: ").split()) if x % 2 != 0])

#24
def problem24():
    print(len(input("list: ").split()))

#25
def problem25():
    print(input("list: ").split().copy())

#26
def problem26():
    a = input("list: ").split()
    l = len(a)
    print(a[l//2 - 1:l//2 + 1] if l % 2 == 0 else a[l//2])

#27
def problem27():
    a = list(map(int, input("list: ").split()))
    b, c = map(int, input("range: ").split())
    print(max(a[b:c]))

#28
def problem28():
    a = list(map(int, input("list: ").split()))
    b, c = map(int, input("range: ").split())
    print(min(a[b:c]))

#29
def problem29():
    a = input("list: ").split()
    b = int(input("index: "))
    if 0 <= b < len(a): 
        a.pop(b)
    print(a)

#30
def problem30():
    a = list(map(int, input("list: ").split()))
    print(a == sorted(a))

#31
def problem31():
    a = input("list: ").split()
    n = int(input("number: "))
    print([x for x in a for _ in range(n)])

#32
def problem32():
    a = list(map(int, input("list1: ").split()))
    b = list(map(int, input("list2: ").split()))
    print(sorted(a + b))

#33
def problem33():
    a = input("list: ").split()
    b = input("element: ")
    print(*[i for i in range(len(a)) if a[i] == b])

#34
def problem34():
    a = input("list: ").split()
    n = int(input("rotate by: ")) % len(a)
    print(a[-n:] + a[:-n])

#35
def problem35():
    l, r = map(int, input("range: ").split())
    print(list(range(l, r + 1)))

#36
def problem36():
    print(sum(x for x in map(int, input("list: ").split()) if x > 0))

#37
def problem37():
    print(sum(x for x in map(int, input("list: ").split()) if x < 0))

#38
def problem38():
    a = input("list: ").split()
    print(a == a[::-1])

#39
def problem39():
    a = input("list: ").split()
    n = int(input("size: "))
    print([a[i:mint(i + n, len(a))] for i in range(0, len(a), n)])

#40
def problem40():
    a = input("list: ").split()
    b = []
    b.extend(i for i in a if i not in b)
    print(b)


# problem40()