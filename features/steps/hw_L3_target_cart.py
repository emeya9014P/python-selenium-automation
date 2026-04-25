from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://target.com")
    sleep(3)


@when("Click on Cart icon")
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(3)


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element (By.XPATH, "//h1[text()='Your cart is empty']").text
    assert 'Your cart is empty' in actual_result
    print("Test Passed")

