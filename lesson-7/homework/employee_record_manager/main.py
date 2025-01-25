from pathlib import Path
import os

current_dir = Path(__file__).resolve().parent



class Employee:
    def __init__(self, empid, name, pos, sal):
        self.employee_id = empid 
        self.name = name 
        self.position = pos 
        self.salary = sal

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    filename = current_dir / "employees.txt"

    def __init__(self):
        if not os.path.isfile(self.filename):
            open(self.filename, 'w').close()

        self.__menu = [
            'Add new employee record',
            'View all employee records',
            'Search for an employee by Employee ID',
            "Update an employee's information",
            "Delete an employee record",
            "Exit",
        ]
    
    def print_menu(self):
        for i in range(len(self.__menu)):
            print(f"{i+1}. {self.__menu[i]}")

    def add_employee(self):
        employee_id = input("Enter Employee ID: ").strip()
        with open(self.filename, 'r') as f:
            for line in f:
                if line.startswith(employee_id + ','):
                    print('Employee with ID {employee_id} already exists!\n')
                    return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        with open(self.filename, 'a') as file:
            file.write(f"{employee_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully!\n")


    def view_employees(self):
        lines = []
        with open(self.filename, 'r') as f:
            for line in f:
                employee_id, name, position, _sal = line.strip().split(', ')
                lines.append(Employee(employee_id, name, position, int(_sal)))
        if not lines:
            print("No employee records found.")
            return

        print("Display the records sorted by which row?")
        print("1. By Employee ID", "2. By name", "3. By position name", "4. By salary", sep = '\n')
        choice = input("Enter your option for the field: ").strip()
        if choice == "1":
            lines.sort(key=lambda x:x.employee_id)
        elif choice == "2":
            lines.sort(key=lambda x:x.name)
        elif choice == "3":
            lines.sort(key=lambda x:x.position)
        elif choice == "4":
            lines.sort(key=lambda x:x.salary)
        else:
            print("Invalid option!")
            return
        
        print("Employee records: ")
        for emp in lines:
            print(emp)
        print('')

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ").strip()
        with open(self.filename, 'r') as f:
            for line in f:
                if line.startswith(employee_id + ","):
                    print("Employee Found: ")
                    print(line.strip()+'\n')
                    return
        
        print("Employee not found.\n")
    
    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ").strip()
        updated = False
        lines = []
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        
        with open(self.filename, 'w') as f:
            for line in lines:
                if not updated and line.startswith(employee_id + ','):
                    print("Enter the new details (leave a blank to keep current): ")
                    _, name, position, salary = line.strip().split(', ')
                    n_name = input(f"Name ({name}): ").strip() or name 
                    n_position = input(f"Position ({position}): ").strip() or position
                    n_salary = input(f"Salary ({salary}): ").strip() or salary
                    line = f"{employee_id}, {name}, {position}, {salary}\n"
                    updated = True
                f.write(line)
        
        if updated:
            print("Employee information updated successfully!\n")
        else:
            print("Employee not found.\n")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ").strip()
        deleted = False 
        lines = []
        with open(self.filename, 'r') as file:
            lines = file.readlines() 

        with open(self.filename, 'w') as f:
            for line in lines:
                if not deleted and line.startswith(employee_id + ','): deleted = True
                else:f.write(line)
        
        if deleted:
            print('Employee record deleted successfully.\n')
        else:
            print('Employee not found.\n')
    
    def run(self):
        print("Welcome to the Employee Record Manager!")
        self.print_menu()
        while True:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("Goodbye!")
                break 
            else:
                print("Invalid choice! Try again.")


manager = EmployeeManager()
manager.run()
