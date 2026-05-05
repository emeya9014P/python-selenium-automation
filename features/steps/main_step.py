from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("Open Target main page")
def open_target_main(context):
    context.app.main_page.open_main()

# test