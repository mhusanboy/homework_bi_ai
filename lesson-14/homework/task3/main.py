from pathlib import Path
import json 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

current_dir = Path(__file__).resolve().parent


safari_options = Options()


url = 'https://www.demoblaze.com'
driver = webdriver.Safari(safari_options)
driver.maximize_window()

driver.get(url)
laptops_button = driver.find_element(By.XPATH, '//*[@id="itemc"][2]')
laptops_button.click()
time.sleep(1)

laptops = []


while True:
    infos = driver.find_elements(By.CLASS_NAME, 'h-100')
    for info in infos:
        name = info.find_element(By.CLASS_NAME, 'hrefch').text.strip()
        price = info.find_element(By.TAG_NAME, 'h5').text.strip()
        description = info.find_element(By.ID, 'article').text.strip().replace('\n', '')
        laptops.append({'name' : name, 'price' : price, 'description' : description})
    next_button = driver.find_element(By.ID, 'next2')
    if next_button.value_of_css_property('display') == 'none':
        break
    next_button.click()
    time.sleep(1)

with open(current_dir/'laptops.json', 'w') as f:
    json.dump(laptops, f, indent=4)

