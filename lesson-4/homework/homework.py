#1
def problem1():
    import bisect
    a = list(map(int, input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()

    def find(lst, item):
        ind = bisect.bisect_left(lst, item)
        return ind < len(lst) and lst[ind] == item
    ans = []

    for x in a:
        if not find(b, x):
            ans.append(x)

    for x in b:
        if not find(a, x):
            ans.append(x)

    print(ans)

#2
def problem2():
    n = int(input("number: "))
    for i in range(1, n): print(i*i)

#3
def problem3():
    txt = input("text: ")
    res = ""
    cnt = 0
    done = set()
    for i in range(len(txt)):
        res += txt[i]
        cnt += 1
        if i != len(txt) - 1 and cnt >= 3 and txt[i] not in "aeoiu" and txt[i] not in done:
            res += '_'
            done.add(txt[i])
            cnt = 0
    print(res)

#4
def problem4():

    import random

    def isnum(x):
        if x == "-":
            return 0
        if(x[0] == '-'): x = x[1:]
        return all(c.isdigit() for c in x)
    
    def validate(l, r):
        x = input()
        while True:
            if not isnum(x):
                x = input("Input an integer!: ")
            elif int(x) < l or int(x) > r:
                x = input(f"number must be inside the range [{l},{r}]: ")
            else:
                break
        return int(x)

    num = random.randint(1, 100)
    while True:
        cnt = 0
        found = 0
        print("Guess the number [1,100] within 10 trials: ", end = '')
        while cnt < 10:
            cnt += 1
            x = validate(1, 100)
            if x > num:
                print("Too high! Try lower: ", end = '')
            elif x < num:
                print("Too low! Try higher: ", end = '')
            else:
                found = 1
                break

        if found:
            print("You guessed it right!")
            break
        
        yes = input("You lost! Want to play again? ")
        if yes.lower() not in ["y", "yes", "ok"]:
            break 

#5 
def problem5():
    p = input("Input a password: ")
    if len(p) < 8:
        print("Password is too short!")
    elif any(c.upper() == c for c in p):
        print("Password is strong!")
    else:
        print("Password must contain an uppercase letter!")

#6 
def problem6():
    n = 100
    sieve = [0] * (n + 1)
    for j in range(2, n + 1):
        if sieve[j]:
            continue
        print(j, end = ' ')
        for i in range(j * j, n + 1, j):
            sieve[i] = 1

#bonus
def bonusproblem():
    import random 
    comp_score, user_score = 0, 0
    choices = ["rock", "paper", "scissors"]
    win = {
        "rock" : "scissors",
        "paper" : "rock",
        "scissors": "paper"
    }
    while comp_score < 5 and user_score < 5:
        comp = random.choice(choices)
        user = input("Choose one of them (rock, paper, scissors): ")
        user = user.lower()
        while user not in  choices:
            user = input("Input only one of the three: ")
        print(f"Computer's choice: {comp}")
        if user == comp:
            print("Draw!")
        elif win[user] == comp:
            print("Point to you")
            user_score += 1
        else:
            print("Point to comp")
            comp_score += 1
    if user_score == 5:
        print("You won!")
    else:
        print("You lost, Computer won!")
    
