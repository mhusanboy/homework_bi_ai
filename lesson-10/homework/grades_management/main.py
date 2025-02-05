import csv
from pathlib import Path

current_dir = Path(__file__).resolve().parent 



def getcontents(filename):
    # print(f'{filename}\n')
    try:
        with open(filename, 'rt') as f:
            reader = csv.DictReader(f)
            return list(reader)
        
    except:
        return []


def get_averages(lst):
    res = dict()
    cnt = dict()
    for record in lst:
        sub = record['Subject']
        if res.get(sub):
            res[sub] += int(record['Grade'])
            cnt[sub] += 1
            
        else:
            res[sub] = int(record['Grade'])
            cnt[sub] = 1 
    for sub, count in cnt.items():
        res[sub] /= count 
    avg = []
    for sub, aver in res.items():
        avg.append({'Subject' : sub, 'Average Grade' : aver})
    return avg

def write_file(filename, res):
    with open(filename, 'wt', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames=res[0].keys())
        writer.writeheader()
        writer.writerows(res)


def run():
    write_file(current_dir/'average_grades.csv', get_averages(getcontents(current_dir/'grades.csv')))


if __name__ == '__main__':
    run()