from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# Target
# Open https://www.target.com/
driver.get('https://www.target.com/')
sleep(2)

# Click Account button
driver.find_element (By.XPATH, "//span[@class='sc-1a162949-3 iuQwR display-name h-margin-r-x3']").click()
sleep(3)

#  Click SignIn btn from side navigation
driver.find_element (By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(4)

# verify SignIn page opened
# “Sign in or create account” text is shown,
# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
expected_result = 'Sign in or create account'
actual_result = driver.find_element (By.XPATH, "//*[contains(text(),'Sign in or create account')]").text
assert expected_result == actual_result, f"Expected {expected_result} not in actual {actual_result}"

print("Test Passed")
# driver.quit()

# [Optional] Build a test case yourself from scratch to search for a product on Target (same as shown in the class), make sure it works and you remember selenium commands.
driver.get('https://www.target.com/')
driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
sleep(3)

driver.find_element(By.XPATH, "//*[contains(text(), 'Your cart is empty')]")
sleep(3)

expected_result = 'Your cart is empty'
actual_result = driver.find_element (By.XPATH, "//*[contains(text(), 'Your cart is empty')]").text
assert expected_result == actual_result, f"Expected {expected_result} not in actual {actual_result}"

print("Test Passed")
driver.quit()

