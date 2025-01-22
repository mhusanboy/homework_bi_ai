#1
def problem1():
    d = eval(input("dict: "))
    k = input("key: ")
    print(d.get(k, "Key not found"))

#2
def problem2():
    d = eval(input("dict: "))
    k = input("key: ")
    print(k in d)

#3
def problem3():
    d = eval(input("dict: "))
    print(len(d))

#4
def problem4():
    d = eval(input("dict: "))
    print(list(d.keys()))

#5
def problem5():
    d = eval(input("dict: "))
    print(list(d.values()))

#6
def problem6():
    d1 = eval(input("dict1: "))
    d2 = eval(input("dict2: "))
    print({**d1, **d2})

#7
def problem7():
    d = eval(input("dict: "))
    k = input("key: ")
    d.pop(k, None)
    print(d)

#8
def problem8():
    d = eval(input("dict: "))
    d.clear()
    print(d)

#9
def problem9():
    d = eval(input("dict: "))
    print(not bool(d))

#10
def problem10():
    d = eval(input("dict: "))
    k = input("key: ")
    print((k, d[k]) if k in d else "Key not found")

#11
def problem11():
    d = eval(input("dict: "))
    k = input("key: ")
    v = input("value: ")
    d[k] = v
    print(d)

#12
def problem12():
    d = eval(input("dict: "))
    v = input("value: ")
    print(list(d.values()).count(v))

#13
def problem13():
    d = eval(input("dict: "))
    print({v: k for k, v in d.items()})

#14
def problem14():
    d = eval(input("dict: "))
    v = input("value: ")
    print([k for k, val in d.items() if val == v])

#15
def problem15():
    keys = eval(input("keys: "))
    values = eval(input("values: "))
    print(dict(zip(keys, values)))

#16
def problem16():
    d = eval(input("dict: "))
    print(any(isinstance(v, dict) for v in d.values()))

#17
def problem17():
    d = eval(input("dict: "))
    k1 = input("outer key: ")
    k2 = input("inner key: ")
    print(d.get(k1, {}).get(k2, "Key not found"))

#18
def problem18():
    from collections import defaultdict
    default_val = input("default value: ")
    d = defaultdict(lambda: default_val)
    print(d)

#19
def problem19():
    d = eval(input("dict: "))
    print(len(set(d.values())))

#20
def problem20():
    d = eval(input("dict: "))
    print(dict(sorted(d.items())))

#21
def problem21():
    d = eval(input("dict: "))
    print(dict(sorted(d.items(), key=lambda x: x[1])))

#22
def problem22():
    d = eval(input("dict: "))
    condition = int(input("value > condition: "))
    print({k: v for k, v in d.items() if v > condition})

#23
def problem23():
    d1 = eval(input("dict1: "))
    d2 = eval(input("dict2: "))
    print(bool(set(d1.keys()) & set(d2.keys())))

#24
def problem24():
    t = eval(input("tuple of key-value pairs: "))
    print(dict(t))

#25
def problem25():
    d = eval(input("dict: "))
    print(next(iter(d.items()), "Empty dictionary"))
