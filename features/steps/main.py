from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://target.com")
    context.wait.until(
        EC.presence_of_element_located((By.ID, 'search')),
        message=f'Target main page is not opened'
    )
# context.wait.until(EC...(By.ID, "ID name"))