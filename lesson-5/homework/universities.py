

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(lst):
    return [x[1] for x in lst],[x[2] for x in lst]

def mean(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

def median(lst):
    if len(lst) == 0:
        return 1
    return sorted(lst)[len(lst) // 2]

br = "******************************"

print(br)
students, fees = enrollment_stats(universities)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: ${sum(fees):,}\n")

print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,}\n")

print(f"Tuition mean: ${mean(fees):,.2f}")
print(f"Tuition median: ${median(fees):,}")
print(br)