<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
=======
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
>>>>>>> master
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

<<<<<<< HEAD
# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('table')
=======
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')
>>>>>>> master

# wait for 4 sec
sleep(4)

<<<<<<< HEAD
# click search button
driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'table'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
=======
# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
>>>>>>> master
print('Test Passed')

driver.quit()
