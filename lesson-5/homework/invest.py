
def invest(amount, rate, years):
    for i in range(years):
        amount *= 1 + rate
        print(f"year {i + 1}: ${amount:.2f}")


amount = float(input("Input the initial amount: "))
rate = float(input("Input the annual percentage: "))
years = int(input("Input the number of years: "))
invest(amount, rate, years)