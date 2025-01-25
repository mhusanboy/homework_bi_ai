import json
import csv
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path 

current_folder = Path(__file__).resolve().parent 
    




def is_valid_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class Task:
    def __init__(self, taskId, title, description, due = None, status = "Pending"):
        self.task_id = taskId
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due
    
    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        return {
            "Task ID" : self.task_id,
            "Title" : self.title,
            "Description" : self.description,
            "Due Date" : self.due_date,
            "Status" : self.status
        }

    @classmethod
    def from_dict(cls, t_dict):
        return cls(
            t_dict["Task ID"],
            t_dict["Title"],
            t_dict["Description"],
            t_dict["Due Date"],
            t_dict["Status"]
        )


class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks, file_path):
        pass

    @abstractmethod
    def load(self, file_path):
        pass
    
    @property
    @abstractmethod
    def extension(self):
        pass

class JSONStorageStrategy(StorageStrategy):
    def save(self, tasks, file_path):
        with open(file_path, 'w') as f:
            json.dump([x.to_dict() for x in tasks], f, indent=4)
        
    def load(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return [Task.from_dict(x) for x in json.load(f)]
        except FileNotFoundError:
            return []  
    
    @property
    def extension(self):
        return ".json"


class CSVStorageStrategy(StorageStrategy):
    def save(self, tasks, file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Task ID", "Title", "Description", "Due Date", "Status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self, file_path):
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                return [Task.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []
    
    @property
    def extension(self):
        return ".csv"
    

class ToDoApp:
    def __init__(self, storage_stategy, file_path):
        self.storage_strategy = storage_stategy
        self.file_path = current_folder / (file_path + storage_stategy.extension)
        self.load_tasks()

    def load_tasks(self):
        self.tasks = self.storage_strategy.load(self.file_path)
    
    def save_tasks(self):
        self.storage_strategy.save(self.tasks, self.file_path)

    def add_task(self):
        task_id = input("Enter Task ID: ").strip()
        for task in self.tasks:
            if task.task_id == task_id:
                print(f"Task with ID {task_id} already exists.")
                return

        title = input("Enter task title: ").strip()
        description = input("Enter description: ").strip()
        due_date = input("Enter due date (YYYY-MM-DD), or leave a blank to skip: ").strip() or None
        if due_date and not is_valid_date(due_date):
            due_date = None
        status = input("Enter Status (Pending/In Proggress/Completed/whatever): ").strip() or "Pending"

        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!\n")
    
    def view_all_tasks(self):
        if not self.tasks:
            print("No task records found.\n")
            return
        print("Tasks: ")
        for task in self.tasks:
            print(task)
    
    def update_task(self):
        task_id = input("Enter Task ID to update: ").strip()
        updated = False
        i = 0
        for task in self.tasks:
            if task.task_id == task_id:
                print("Enter the new details (leave a blank to keep current): ")
                title = input(f"Title ({task.title}): ").strip() or task.title
                description = input(f"Description: ({task.description}): ").strip() or task.description
                due_date = input(f"Due Date ({task.due_date}): ").strip() or None
                if due_date and not is_valid_date(due_date):
                    due_date = None 
                if not due_date:
                    due_date = task.due_date
                status = input(f"Status ({task.status}): ").strip() or task.status 
                self.tasks[i] = Task(task_id, title, description, due_date, status)
                updated = True
                break 
            i += 1
        
        if updated:
            print("Task updated successfully.\n")
        else:
            print("No task found.\n")
    
    def delete_task(self):
        task_id = input("Enter Task ID to delete: ").strip()
        deleted = False 

        for i in range(len(self.tasks)):
            if self.tasks[i].task_id == task_id:
                self.tasks.pop(i)
                deleted = True 
                break 
            
        if deleted:
            print("Task deleted successfully.\n")
        else:
            print("No task found.\n")

    def filter_by_status(self):
        status = input("Enter the status to filter: ").strip().lower()
        found = False
        for task in self.tasks:
            if(task.status.lower() == status):
                if not found:
                    print(f"All taks under '{status}':")
                print(task)
                found = True 
        
        if not found:
            print(f"No task found under {status} status\n")
    
    def run(self):
        print("Welcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save Tasks")
        print("7. Load tasks")
        print("8. Exit")
        while True:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_by_status()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.load_tasks()
            elif choice == "8":
                print("Goodbye!")
                return
            else:
                print("Invalid option! Try again.")
        

storage = None
print("Choose the storage format:\n1. JSON\n2. CSV")
choice = input("Enter your choice: ").strip()


if choice == "1":
    storage = JSONStorageStrategy()
elif choice == "2":
    storage = CSVStorageStrategy()
else:
    print("Invalid option")
    exit(0)


app = ToDoApp(storage, "tasks")

app.run()
