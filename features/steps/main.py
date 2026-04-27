from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://target.com")
    sleep(3)