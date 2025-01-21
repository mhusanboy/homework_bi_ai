#1
def problem1():
    name = input("name: ")
    year = int(input("year of birth: "))
    print(2025 - year)

#2
def problem2():
    txt = 'LMaasleitbtui'
    print(txt[0] + txt[2:5] + txt[7:9] + txt[-2:])

#3
def problem3():
    s = input("string: ")
    print(len(s))
    print(s.upper())
    print(s.lower())

#4
def problem4():
    s = input("string: ")
    print(s == s[::-1])

#5
def problem5():
    s = input("string: ")
    vowels = "aeiouAEIOU"
    v = sum(1 for c in s if c in vowels)
    print(v, len(s) - v)

#6
def problem6():
    a = input("string1: ")
    b = input("string2: ")
    print(b in a)

#7
def problem7():
    s = input("sentence: ")
    old = input("replace: ")
    new = input("with: ")
    print(s.replace(old, new))

#8
def problem8():
    s = input("string: ")
    print(s[0], s[-1])

#9
def problem9():
    s = input("string: ")
    print(s[::-1])

#10
def problem10():
    s = input("sentence: ")
    print(len(s.split()))

#11
def problem11():
    s = input("string: ")
    print(any(c.isdigit() for c in s))

#12
def problem12():
    words = input("list of words (comma-separated): ").split(',')
    sep = input("separator: ")
    print(sep.join(words))

#13
def problem13():
    s = input("string: ")
    print(s.replace(" ", ""))

#14
def problem14():
    a = input("string1: ")
    b = input("string2: ")
    print(a == b)

#15
def problem15():
    s = input("sentence: ")
    print("".join(word[0].upper() for word in s.split()))

#16
def problem16():
    s = input("string: ")
    c = input("char: ")
    print(s.replace(c, ""))

#17
def problem17():
    s = input("string: ")
    print(''.join('*' if c in "aeiouAEIOU" else c for c in s))

#18
def problem18():
    s = input("sentence: ").split()
    print("Starts with: " + s[0], "Ends with: " + s[-1], sep = '\n')

problem18()