n = int(input("Enter a positive integer: "))

i = 1
f = []
while i * i <= n:
    if n % i: continue
    f.append(i)
    if i * i != n:
        f.append(n // i)
    i += 1

f.sort()
for i in f:
    print(f"{i} is a factor of {n}")

