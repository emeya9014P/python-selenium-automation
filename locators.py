from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
sleep(2)

# By ID
element = driver.find_element(By.ID, 'twotabsearchtextbox')
print(element)

# By XPATH
driver.find_element(By.XPATH, '//input[@placeholder="Search Amazon"]')
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")

# By XPATH, any tag
driver.find_element(By.XPATH, '//*[@placeholder="Search Amazon"]')

# By XPATH, multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @spellcheck='false']")
driver.find_element(By.XPATH, "//input[@spellcheck='false' and @tabindex='0' and @type='text']")

# By XPATH, text()
driver.find_element(By.XPATH, "//h2[text()='Designer gifts for Mom']")
driver.find_element(By.XPATH, "//h2[text()='Designer gifts for Mom' and @class='.....']")

# By. XPATH, contains()
driver.find_element(By.XPATH, "//h2[contains(text(), 'Designer gifts')]")
driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search A')]")

# By XPATH, from parent => child node
driver.find_element(By.XPATH, "//div[@id='nav-search']//input[@aria-label='Search Amazon']")

# CSS selectors
# By ID
driver.find_element(By.CSS_SELECTOR, 'id_name')

# By Css selector, using id
driver.find_element(By.CSS_SELECTOR, '#id_name')
driver.find_element(By.CSS_SELECTOR, 'tag_name#id_name')

# By CSS selector, class /
driver.find_element(By.CSS_SELECTOR, '.class_value')
driver.find_element(By.CSS_SELECTOR, '.class_value.class_value.class_value')
driver.find_element(By.CSS_SELECTOR, 'tag_name.class_value')

# By CSS selector, tag + id + 2 classes
driver.find_element(By.CSS_SELECTOR, 'tag_name#id_name.class_value.class_value')

# By CSS selector, attributes - [attribute='value']
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")

# By CSS selector, multiple attributes - [attribute='value'][attribute='value']
driver.find_element(By.CSS_SELECTOR, "[attribute='value'][attribute='value']")

# By CSS selector, multiple attributes - tag + [attribute='value'][attribute='value']
driver.find_element(By.CSS_SELECTOR, "tag[attribute='value'][attribute='value']")

# By CSS selector, multiple attributes - tag + class + [attribute='value']
driver.find_element(By.CSS_SELECTOR, "tag.class_name[attribute='value']")

# By CSS selector, contains *=
driver.find_element(By.CSS_SELECTOR, "tag.class_name[attribute*='values']")
driver.find_element(By.CSS_SELECTOR, "input.hamberger[placeholder*='search']")

# By CSS selector, contains *= in class (instead of using period,use [attribute='value'] as the class is also attribute  contains *=
driver.find_element(By.CSS_SELECTOR, "[class*='partial_class_value']")


