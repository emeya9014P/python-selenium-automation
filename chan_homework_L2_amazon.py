from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.amazon.com/ax/claim?arb=cd0d6058-69c8-42f6-9c4e-fe1e365be482')
sleep(3)

# By ID
# element = driver.find_element (By.ID, '')

# Amazon logo
driver.find_element (By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Email field
driver.find_element (By.XPATH, "//input[@type='email']")

# Continue button
driver.find_element (By.XPATH, "//input[@aria-labelledby='continue-announce']")

# Conditions of use link
driver.find_element (By.XPATH, "//a[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element (By.XPATH, "//a[text()='Privacy Notice']")

# Need help link
driver.find_element (By.XPATH, "//a[contains(text(), 'Need help?')]")

# The following items are not found on the page.
# Forgot your password link
# Other issues with Sign-In link
# Create your Amazon account button


