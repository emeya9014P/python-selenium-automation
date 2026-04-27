from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
    expected_result = 'Your cart is empty'
    assert 'Your cart is empty' in actual_result
    print("Test Passed")

