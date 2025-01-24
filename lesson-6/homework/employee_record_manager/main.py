from pathlib import Path

current_dir = Path(__file__).resolve().parent

filename = current_dir / "employees.txt"
try:
    with open(filename, "x") as f:
        pass
except FileExistsError:
    pass


menu = [
    'Add new employee record',
    'View all employee records',
    'Search for an employee by Employee ID',
    "Update an employee's information",
    "Delete an employee record",
    "Exit",
]




def print_menu():
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")



def add_employee(value):
    with open(filename, "a") as f:
        f.write(", ".join(str(i) for i in value) + '\n')
    

def view_employees():
    br = "*" * 20
    print(br)

    with open(filename, 'r') as f:
        for line in f.readlines():
            print(line)
    
    print(br)

def search(id):
    value = ()
    with open(filename, 'r') as f:
        for line in f.readlines():
            value = tuple(line.split(", "))
            if value[0] == id:
                print("Employee found: ", *value)
                return
    
    print("Employee not found!")


def update(id, value):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        if lines[i].split(", ")[0] == id:
            lines[i] = ", ".join(str(i) for i in value)
            break 
    
    with open(filename, 'w') as f:
        for i in lines:
            f.write(lines[i])
    

def delete(id):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        if lines[i].split(", ")[0] == id:
            lines.pop(i)
            break 
    
    with open(filename, 'w') as f:
        for i in lines:
            f.write(lines[i])


def finish():
    exit()



print("Welcome to the employee management app!\n")
while True:
    print("What are you gonna do? Choose one option below.")
    print_menu()
    opt = int(input())
    while opt < 1 or opt > 6:
        opt = int(input("Invalid option, it should be between 1 and 6: "))
    print(opt)
    if opt == 1:
        print("Input the information for the new employee!")
        id = input("ID: ")
        name = input("Name: ")
        pos = input("Position: ")
        sal = int(input("Salary: "))
        add_employee((id, name, pos, sal))
    elif opt == 2:
        view_employees()
    elif opt == 3:
        id = input("Enter the id of the employee to search for: ")
        search(id)
    elif opt == 4:
        id = input("Enter the id of the employee to update: ")
        print("Input the new information for this employee!")
        name = input("Name: ")
        pos = input("Position: ")
        sal = int(input("Salary: "))
        update(id, (id, name, pos, sal))
    elif opt == 5:
        id = input("Enter the id of the employee to delete: ")
        delete(id)
    else:
        finish()
    
    print("\nDone! \n")