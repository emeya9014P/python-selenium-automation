from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://stackoverflow.com/questions")
sleep(4)

# click Sign up button
driver.find_element(By.CSS_SELECTOR, "[data-gps-track='signup.topbar.click']").click()
sleep(4)

# find Join Stack Overflow
driver.find_element(By.XPATH, "//strong[contains(text(), 'Join Stack Overflow')]").text
sleep(3)

# expected_result = 'Join Stack Overflow'
# actual_result = driver.find_element (By.XPATH, "//strong[contains(text(), 'Join Stack Overflow')]").text
# assert expected_result == actual_result, f"Expected {expected_result} not in actual {actual_result}"
#
# print("Test Passed")
# driver.quit()

# click Sign up with Google button
# driver.find_element(By.XPATH, "//button[@data-testid='signup-google']").click()
# sleep(3)

# click Sign up with GitHub button
# driver.find_element(By.XPATH, "//button[@data-provider='GitHub']").click()
# sleep(3)

# enter email in the Email section: $$("#signup-modal-email")
driver.find_element(By.CSS_SELECTOR, "#signup-modal-email").send_keys("abc@mail.com")
sleep(3)

# enter password in the Password section: $$("#signup-modal-password")
driver.find_element(By.CSS_SELECTOR, "#signup-modal-password").send_keys("23456789")
sleep(5)

# click the Sign up button: $$("#signup-modal-submit-button")
driver.find_element(By.CSS_SELECTOR, "#signup-modal-submit-button").click()
sleep(3)

# click the view icon: $$(".svg-icon.iconEyeOff")
driver.find_element(By.CSS_SELECTOR, ".svg-icon.iconEyeOff").click()
sleep(3)

# click Log in button: $x("//a[@href='/users/login']")
driver.find_element(By.XPATH, "//a[@href='/users/login']").click()
sleep(3)




