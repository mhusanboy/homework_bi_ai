import json
import csv
from pathlib import Path

current_dir = Path(__file__).resolve().parent 



def getcontents(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
        
    except:
        return []


def display(data):
    for row in data:
        for key,value in row.items():
            print(f"{key} : {value}")
        print('')


def write_file(filename, data):
    with open(filename, 'w', newline = '') as f:
        json.dump(data, f, indent=4)


def json_to_csv(filename):
    with open(current_dir/filename, 'r') as f:
        data = json.load(f)
        fcsv = open(current_dir/(filename[:-5]+'.csv'), 'wt', newline='')
        writer = csv.DictWriter(fcsv, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        fcsv.close()

def run():
    data = getcontents(current_dir / 'tasks.json')
    total_tasks = len(data)
    completed_tasks = sum([1 for row in data if row['completed']])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(row['priority'] for row in data)/total_tasks
    print(f'total tasks: {total_tasks}, completed tasks: {completed_tasks}, pending tasks: {pending_tasks}, average priority: {avg_priority}')

    print(data)
    display(data)
    write_file(current_dir/'tasks.json', data)
    json_to_csv('tasks.json')

run()