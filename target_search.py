from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.target.com/")
sleep(2)

driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(7)

# Verification (assertion)
driver.find_element(By.XPATH, "//*[@data-module-type='ListingPageResultsCount']")

expected_result = 'tea'
actual_result = driver.find_element(By.XPATH, "//div[contains(@class, 'styles_resultCount')]").text
assert expected_result in actual_result, f'Expected "{expected_result}" not in actual "{actual_result}"'

print('Test case PASSED')
driver.quit()