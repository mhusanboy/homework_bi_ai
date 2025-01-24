

def check():
    def wrapper(func):
        try:
            print("output:", func())
        except ZeroDivisionError:
            print("Denominator can't be zero")

@check

def div(a, b):
    return a / b 

