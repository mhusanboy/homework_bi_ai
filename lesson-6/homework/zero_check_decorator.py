

def check(func):
    def wrapper(a, b):
        if b == 0:
            raise ValueError("Denominator can't be zero")
        return func(a, b)
    return wrapper

@check

def div(a, b):
    return a / b 

a, b = map(int,input("input a and b (a b): ").split())
try:
    print(div(a, b))
except ValueError as e:
    print(e)