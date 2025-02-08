from bs4 import BeautifulSoup
from pathlib import Path

current_dir = Path(__file__).resolve().parent



soup = None 
try:
    with open(current_dir/"weather.html", 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
except FileNotFoundError:
    print("No file found.")
    exit(0)

tags = soup.find_all('tr')

infos = []
headers = [elem.text for elem in tags[0].find_all('th')]

for i in range(1, len(tags)):
    info = dict()
    for head, elem in zip(headers, tags[i].find_all('td')):
        info[head] = elem.text
    infos.append(info)


for info in infos:
    print(", ".join(f"{key}: {elem}" for key, elem in info.items()))

day = max(infos, key = lambda x: int(x['Temperature'][:-2]))

print(f"Day with highest Temperature of {day['Temperature']} is {day['Day']}.")

sunnys = [info['Day'] for info in infos if info['Condition'] == 'Sunny']

if sunnys:
    print("Day(s) with Sunny condition: ", ", ".join(sunnys))

if len(infos):
    avg = sum(float(info['Temperature'][:-2]) for info in infos) / len(infos)
    print(f"Average temperature: {avg:.1f}°C")