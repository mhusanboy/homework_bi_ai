from pathlib import Path
import requests
import csv
import sqlite3
from bs4 import BeautifulSoup

current_dir = Path(__file__).resolve().parent 

url = 'https://realpython.github.io/fake-jobs'

def get_desc(link):
    res = requests.get(link)
    if not res:
        print("Unsuccessful request")
        exit(0)
    content =  BeautifulSoup(res.content, 'html.parser')
    return content.find('div', class_ = 'content').find('p').text

def scrape_infos():
    res = requests.get(url)
    
    if not res:
        print("Unsuccessful request")
        exit(0)
    content = BeautifulSoup(res.content, 'html.parser')
    jobs = []
    infos = content.find_all(class_ = 'card-content')
    for info in infos:
        job_title = info.find(class_ = 'title is-5').text.strip()
        company = info.find(class_ = 'subtitle is-6 company').text.strip()
        location = info.find(class_ = 'location').text.strip()
        apply_link = info.find_all(class_ = 'card-footer-item')[1]['href']
        jobs.append((job_title, company, location, apply_link))
    return jobs




with sqlite3.connect(current_dir/'jobs.db') as con:
    cursor = con.cursor()
    cursor.execute("""
        create table if not exists jobs(
                   Job_title text,
                   Company_name text, 
                   Location text,
                   Description text,
                   application_link text
                   );    
    """)



jobs = scrape_infos()


with sqlite3.connect(current_dir/'jobs.db') as con:
    cursor = con.cursor()
    job_ids = cursor.execute('select job_title, company_name, location from jobs;').fetchall()
    for job in jobs:
        if job[:3] in job_ids:
            info = cursor.execute('select application_link from jobs where job_title = ? and company_name = ? and location = ?', job[:3]).fetchone()
            if info[0] != job[3]:
                description = get_desc(job[3])
                cursor.execute('update jobs set description = ?, application_link = ? where job_title = ? and company_name = ? and location = ?', (description, job[3], job[0], job[1], job[2]))
        else:
            description = get_desc(job[3])
            cursor.execute("insert into jobs values(?, ?, ?, ?, ?);", (job[0], job[1], job[2], description, job[3]))


def filter_by(search_key, column):
    if column.lower() not in ['company_name', 'location']:
        print('Cannot be filtered with these columns')
        return 
    values = []
    try:
        with sqlite3.connect(current_dir / 'jobs.db') as con:
            cursor = con.cursor()
            query = f"select * from jobs where {column} = '{search_key}'"
            values = cursor.execute(query).fetchall()
    except:
        pass
    return values

column = input("Filter by (company_name, location): ")
search_key = input(f"Input the search value: ")

results = filter_by(search_key, column)
print("You can see your results in search_results.csv file.")

with open(current_dir/'serach_results.csv', 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(["Job Title",
                    "Company Name",
                    "Location",
                    "Job Description",
                    "Application Link"])
    writer.writerows(results)

